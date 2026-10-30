# Return to Barovia — Campaign Knowledge Wiki

A D&D (Curse of Strahd–style) campaign wiki, kept from the point of view of **Tivwick "Tiv" Bramblequill**
(the user's character): a Candlekeep scholar and researcher in positive-energy necromancy. Session audio goes in,
a transcript, writeup, wiki updates, a letter to Gregor and a private journal entry come out.

## Layout
| Path | Contents |
|---|---|
| `recordings/` | Session audio (git-ignored, never commit) |
| `scripts/transcribe.py`, `glossary.txt` | faster-whisper transcription; glossary seeds proper nouns |
| `sessions/session-NN_YYYY-MM-DD/` | `raw_transcript.txt/.json` (never edit), `writeup.md`. Date = real-world date. Sessions 4–5 hold player recaps (`player_recap_*.md`) plus a reconstructed `writeup.md` in Tiv's voice |
| `characters/` | The six PCs, one page each (see canon below) |
| `npcs-friendly/` | One page per friendly/neutral NPC |
| `npcs-enemy/` | One page per important enemy NPC |
| `places/` | Places of interest |
| `quests/open/`, `quests/resolved/` | One page per quest; move the file when resolved |
| `correspondence/` | Tiv ↔ Gregor letters, one file per letter, named `<YYYY-MM-DD>_letter-NN_tiv-to-gregor.md` (legacy files keep their in-game-date names) |
| `journal/` | Tiv's private journal — ideas, experiments, plot hooks. One entry per session |
| `templates/` | Page templates; copy them, don't invent new shapes |
| `assets/` | Maps/images |

Python env: `source .venv/bin/activate` (git-ignored). Dependencies in `requirements.txt` (`av` is pinned <16 because faster-whisper 1.2.x breaks on newer PyAV).

## PC canon (spelling in filenames → aliases seen in notes)
- `tivwick-bramblequill` — Tiv, "the little curious one", Necromancer card. The user's character.
- `gynlian-glo` — Gwynlian / Gwen, Vistani, Mist card (lost her ability to traverse the mist)
- `ismakr-der-kleiner` — Ismark, rightful Burgomaster of Barovia, wields a Vorpal Sword
- `iolas-palestrider` — Artifact card, carries a sword tied to Barovia
- `aldric-duskmore` — Innocent card, follower of the Morninglord
- `kethri` — Tempter card, monk-like fighter, hunted by "the Clenched Hand"
Verik Morgain / Vardik / Vardak → always **Vardak**. Whisper will mangle names; always normalise to these. Other aliases: Erabus/Erebus, Karstark/Carstark, Usheron/Ushuran, Rod Barchetta (old notes and Whisper say Rob or Rød; the monk is **Rod**, full name Rod Barchetta; his book writes to Gregor) — always write Rod, never Rob. The DM is not a character.

## Conventions
- Link with Obsidian wikilinks to the filename without extension: `[[ubral]]`, `[[tivwick-bramblequill]]`. Filenames are lowercase-kebab. Every new entity gets a page; every page mentions the sessions it appears in (`[[session-06_2026-10-29/writeup|Session 6]]`).
- Pages start with YAML frontmatter (`type`, `aliases`, `first_seen`, `status`) — see `templates/`.
- **Update, don't duplicate.** Before creating a page, search for it (`ls`, `grep -ril`), including aliases. Append to its "Timeline" section.
- **Never invent.** If the transcript is unclear, write `TODO(verify): …`. Facts come from the transcript or earlier notes; label speculation as speculation. Raw transcripts are never edited.
- Keep player-knowledge vs. Tiv-knowledge in mind: the wiki records what the party has learned.

## Time and place tracking (required in every writeup, letter, journal entry)
Open each with this header block:
```
**In-game date:** 12 Uktar, 1498 DR
**Elapsed:** +1 day since previous entry (Day N since arrival in Barovia)
**Location:** where the party is now · Route: A → B → C
```
Arrival in Barovia (via the Candlekeep mist ritual) was **11 Uktar, 1498 DR** = Day 0. Keep a running table in each `writeup.md` and carry it forward from the previous session's writeup.

## Voice rule: everything is written by Tiv
**All prose in the wiki — session writeups, wiki pages, letters, journal — is written in first person by Tiv** ("I", "we"), as field notes of a Candlekeep scholar. Not a neutral summary. Facts stay accurate; the voice is Tiv's: wry, precise, curious, fond of understatement ("Remarkable specimen."), occasionally vain about his research, frightened in a restrained way. Page headings state *what Tiv thinks of it*. Frontmatter and the final **Margin Notes for the Player (out of character)** section (uncertainties, `TODO(verify)`) are the only out-of-voice parts.

## Tiv's backstory and research subjects (source of truth: `characters/tivwick-bramblequill.md`)
Apprenticed to Archmage Halvoryn Vexis (destroyed, with Grathok the Remembered); friend Edrin Vale is pursuing lichdom; goal: *redeem* undeath with positive energy. Six research subjects: Craig (writing; only one currently animated), Mirel (arcane recall), Dobb (obedience control), Serra (dexterity), Kett (failure states), Bram (physical baseline). All except Craig are **positive-energy spirits** Tiv resummons into bodies. Positive-energy spirits **love taking damage and dying** (no death on their plane); established ones no longer seek it immediately, but new spirits must be **negotiated with**. The vampire sorcerer ([[vardak]]) has had his intelligence banished already; the negative-energy spirit left in the body hates the material plane, so the swap is just a matter of Tiv finding time. Keep these facts consistent.

## Tiv's voice (letters and journal)
An adventurer-scholar who *loves* danger and the writing-up of it: he goes into dangerous places on purpose in order to write about them, and his accounts are as much travelogue as research. Formal, curious, a little vain about being the best magical researcher in the room, proud of Candlekeep, thrilled by undeath-as-theory. Letters go to **Gregor, Head Archivist of Candlekeep**, signed with the full block, always: "— Tivwick Bramblequill / Scholar of Candlekeep / Researcher in Applied Positive-Energy Necromancy". Letters end with a numbered **Research requests** list. Each letter has a **Recap** and **Hypotheses** section: this is the channel through which the DM leaves clues about where to go next, so make hypotheses concrete and falsifiable. The journal is private and is written like pages from the **book Tiv is writing about his adventures**: narrative, atmospheric, scene-setting prose (a story, not notes), followed by his experiments and loose threads. The book's **working title changes constantly**: each entry, `scripts/book_title.py roll` decides (90% new title, 2% keep, 8% revert to an earlier one), and `journal/book_titles.md` stores the history. It is never framed as "what I did not tell Gregor". Its content: ideas, experiments with a method/expected result, and "loose threads" to pull next session, written in Tiv's own voice (never a meta checklist). Rod's book can also be written in, so Tiv distrusts it (Erabus can wear faces).

## Processing a new session
Use the skills (`.claude/skills/`), or `/process-session` to run them all:
`transcribe-session` → `write-session` → `update-wiki` → `gregor-letter` → `tiv-journal`.
Ask the user for anything the recording cannot tell you (session number, real date, in-game date, what Tiv is up to). Tell the user about every `TODO(verify)` you left.
