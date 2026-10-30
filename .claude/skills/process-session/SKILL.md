---
name: process-session
description: Run the full pipeline for a new session recording — transcribe, writeup, wiki update, Gregor letter, private journal. Use when the user hands over a new recording and wants everything done.
---
# Process a full session

Ask once for: audio file, session number, real date, in-game date (if known), and what Tiv wants to pursue this session. Then run in order, following each skill's instructions:

1. `transcribe-session`
2. `write-session`
3. `update-wiki`
4. `gregor-letter`
5. `tiv-journal`

Show a short summary at the end: files created/updated, `TODO(verify)` items, and suggested next-session hooks. Do not commit unless asked.
