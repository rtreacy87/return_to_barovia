---
name: tiv-journal
description: Write Tiv's private journal entry for a session — ideas, experiments he wants to run, and loose threads. Use after write-session or when asked for Tiv's journal/ideas/experiments.
---
# Tiv's private journal

Inputs: the session writeup, earlier `journal/` entries (carry open experiments forward, tick off finished ones), and the goals the user states for Tiv this session.

0. **Pick the working title of Tiv's book.** He cannot leave it alone. Run `python scripts/book_title.py roll` (do not choose by feel; the script applies the odds: 90% change, 2% keep, 8% go back to an earlier title). Then:
   - `CHANGE`: invent a *new* title that is not in `journal/book_titles.md`.
   - `KEEP <title>`: use the current title.
   - `REVERT <title>`: use that earlier title, and have Tiv remark on it (he thinks the old one was better all along).
   Record the result: `python scripts/book_title.py set <session> "<title>"`. The history lives in `journal/book_titles.md`. In the chapter header, if the title changed, Tiv may grumble about the old one in a line.
1. Copy `templates/journal.md` to `journal/session-NN_<date>.md`. Header: in-game date, elapsed time, location and route (same as the writeup).
2. **Experiments** are the core: each has hypothesis, method, expected result if true/false, and what it needs (spells, components, allies). Make them testable with the party's actual resources.
3. **Loose threads** (heading: "Loose Threads I Mean to Pull") are things Tiv resolves to do next, written as in-character intentions, never as a meta checklist or "plot hook" language; note which old threads are tied off.
4. Open with a narrative passage written as a chapter of the **book Tiv is writing** (headed `*From the book I am writing, working title:* **<title>**`, using the title chosen in step 0) about his adventures: scene-setting, story-telling, his sense of adventure and wonder. Never a heading like "what I did not put in the letter". Then the experiments and loose threads.
5. Separate what Tiv *knows* from what he *suspects*.
