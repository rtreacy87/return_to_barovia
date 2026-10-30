---
name: write-session
description: Turn a session's raw transcript into a formatted writeup.md (narrative, decisions, in-game date, elapsed time, locations). Use after transcription or when asked to write up / recap a session.
---
# Write the session writeup

Inputs: `sessions/session-NN_*/raw_transcript.txt`, the previous session's `writeup.md` (or `player_recap_*.md`), `CLAUDE.md` conventions.

1. Read the whole transcript (read in chunks; it is long). Table talk, rules chatter and out-of-character jokes are dropped; in-character events, decisions, discoveries, NPC statements and combat outcomes are kept. Recaps read aloud at the start of a session are not new events.
2. Normalise names to the canon in `CLAUDE.md`. Mishearings are likely (Whisper hears "Karstar", "Ushuran"); fix when sure, else `TODO(verify)`.
3. **Write in first person as Tiv** (see the voice rule in `CLAUDE.md`), a field chronicle with headings like "Erabus" or "Over Wolf Burgers"; put uncertainties in a final out-of-voice *Margin Notes* section. Copy `templates/session-writeup.md` to `sessions/session-NN_*/writeup.md` and fill it: header block with in-game date, **elapsed days** and **location/route**, TL;DR, scene-by-scene narrative with `[[wikilinks]]`, decisions, open questions, and the time & travel log carried forward from the previous session.
4. In-game date and elapsed time: derive from the transcript (rests, travel, "it's been two days"); if not stated, estimate and mark `TODO(verify)`. Day 0 = 11 Uktar 1498 DR.
5. Include timestamps like `(~01:23:10)` on key scenes so the user can audit against the audio.
6. End by listing the `TODO(verify)` items for the user.
