#!/usr/bin/env python3
"""Transcribe a session recording with faster-whisper.

Usage: python scripts/transcribe.py <audio> --session 6 --date 2026-10-29 [--clip SECONDS]
Writes sessions/session-NN_YYYY-MM-DD/raw_transcript.{txt,json}. Never edit the output by hand.
"""
import argparse
import ctypes
import glob
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def preload_cuda_libs():
    """Load pip-installed cuBLAS/cuDNN so CTranslate2 finds them without LD_LIBRARY_PATH."""
    import site
    for base in site.getsitepackages():
        for pattern in ("nvidia/cublas/lib/libcublas.so*", "nvidia/cudnn/lib/libcudnn*.so*"):
            for lib in sorted(glob.glob(os.path.join(base, pattern))):
                try:
                    ctypes.CDLL(lib, mode=ctypes.RTLD_GLOBAL)
                except OSError:
                    pass


def stamp(seconds):
    s = int(seconds)
    return f"{s // 3600:02d}:{s % 3600 // 60:02d}:{s % 60:02d}"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("audio")
    ap.add_argument("--session", type=int, required=True)
    ap.add_argument("--date", required=True, help="real-world date, YYYY-MM-DD")
    ap.add_argument("--model", default="large-v3")
    ap.add_argument("--device", default="cuda")
    ap.add_argument("--glossary", default=str(ROOT / "glossary.txt"))
    ap.add_argument("--clip", type=float, help="only transcribe the first N seconds (testing)")
    ap.add_argument("--out-dir", help="override output directory")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    out = Path(args.out_dir) if args.out_dir else ROOT / "sessions" / f"session-{args.session:02d}_{args.date}"
    txt, js = out / "raw_transcript.txt", out / "raw_transcript.json"
    if txt.exists() and not args.force:
        sys.exit(f"{txt} exists; use --force to overwrite")
    out.mkdir(parents=True, exist_ok=True)

    if args.device == "cuda":
        preload_cuda_libs()
    from faster_whisper import WhisperModel

    prompt = None
    if Path(args.glossary).exists():
        prompt = "D&D Curse of Strahd session. Names: " + Path(args.glossary).read_text().strip()

    model = WhisperModel(args.model, device=args.device,
                         compute_type="float16" if args.device == "cuda" else "int8")
    kwargs = dict(vad_filter=True, initial_prompt=prompt, language="en",
                  condition_on_previous_text=False)
    if args.clip:
        kwargs["clip_timestamps"] = [0, args.clip]
    segments, info = model.transcribe(args.audio, **kwargs)
    total = args.clip or info.duration
    print(f"audio {stamp(info.duration)} long; transcribing {stamp(total)}", flush=True)

    rows = []
    with open(txt, "w") as f:
        for seg in segments:
            line = seg.text.strip()
            rows.append({"start": round(seg.start, 2), "end": round(seg.end, 2), "text": line})
            f.write(f"[{stamp(seg.start)}] {line}\n")
            f.flush()
            if len(rows) % 50 == 0:
                print(f"  {stamp(seg.end)} / {stamp(total)} ({100 * seg.end / total:.0f}%)", flush=True)
    js.write_text(json.dumps({"audio": os.path.basename(args.audio), "model": args.model,
                              "duration": info.duration, "segments": rows}, indent=1))
    print(f"wrote {txt} ({len(rows)} segments)")


if __name__ == "__main__":
    main()
