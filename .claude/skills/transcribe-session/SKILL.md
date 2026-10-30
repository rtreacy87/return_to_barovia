---
name: transcribe-session
description: Transcribe a D&D session recording (wav/mp3/m4a) into sessions/session-NN_date/raw_transcript.txt using faster-whisper in the project venv. Use when the user gives or mentions a new session audio file.
---
# Transcribe a session recording

1. Confirm with the user (ask only what you can't infer): audio path, **session number**, **real-world date** (YYYY-MM-DD). Audio lives in `recordings/` (git-ignored); move it there if not.
2. Run from the repo root:
   ```
   source .venv/bin/activate && python scripts/transcribe.py recordings/<file> --session N --date YYYY-MM-DD
   ```
   Run it in the background for long files (~3 h audio); it prints progress. Test a snippet first with `--clip 120 --out-dir <scratch dir>`.
3. If the venv is missing: `python3 -m venv .venv && .venv/bin/pip install -r requirements.txt nvidia-cublas-cu12 nvidia-cudnn-cu12`.
4. Verify the output exists, skim the first and last lines, and report the segment count. Never edit `raw_transcript.*`.
5. Add newly heard proper nouns to `glossary.txt` for future runs.
