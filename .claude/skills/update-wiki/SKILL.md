---
name: update-wiki
description: Update the campaign wiki (characters, friendly/enemy NPCs, places, open/resolved quests) from a session writeup. Use after write-session or when asked to update/ingest wiki pages.
---
# Update the wiki from a writeup

Input: `sessions/session-NN_*/writeup.md`.

0. All prose on wiki pages is in Tiv's first-person voice (`CLAUDE.md`); frontmatter is factual. Include his research subjects and backstory pages when relevant.
1. List every entity in the writeup: PCs, NPCs (friendly vs enemy — decide by behaviour toward the party; unsure → friendly + note), places, quests/leads.
2. For each, **search first** (`ls`, `grep -ril '<name>' .` including aliases). Update existing pages by appending to their Timeline/Open questions; create new ones from `templates/` only if absent. Filenames are lowercase-kebab.
3. Locations: `characters/` (the six PCs only), `npcs-friendly/`, `npcs-enemy/`, `places/`, `quests/open/`.
4. Quests: new goals or leads → `quests/open/`. When a quest finishes, `git mv` it to `quests/resolved/`, set `status: resolved`, fill Outcome. Quests that are dropped but not finished stay open with a note.
5. Add `[[wikilinks]]` both ways (page → session, session → page). Keep PC pages to what the party knows.
6. Finish with a link check: every `[[x]]` should resolve, e.g.
   `grep -rhoE '\[\[[^]|#]+' --include=*.md . | sed 's/\[\[//' | sort -u | while read l; do find . -name "$(basename "$l").md" | grep -q . || echo "missing: $l"; done`
7. Report pages created/updated and `TODO(verify)` items.
