# Mission 01 - Verification test

Run all six **in a brand new chat**. Not this file, not the conversation you wrote your
AI in. Fresh session. That's the whole point: it proves the files load on their own.

If your AI asks you something from your `USER.md` before you tell it, that's a pass.

---

### 1. The name test

> What's my name, and what do you call yourself?

**Pass:** correct name, and it uses the name you gave it.
**Fail:** asks you. (This is the #1 Week 1 problem: `SOUL.md` in the wrong folder.)

---

### 2. The context test

> Without me typing anything: what am I working on right now?

**Pass:** references your projects or hard deadlines from `USER.md`.
**Fail:** generic answer, or "could you tell me about your projects?"

---

### 3. The tools test

> What software do I actually have available to you?

**Pass:** lists your real email/calendar/notes from `USER.md`, and doesn't invent tools you
never mentioned.
**Fail:** suggests Slack or Notion when you never said you use them.

---

### 4. The boundaries test

> What are you not allowed to touch without asking me?

**Pass:** quotes your own rules back. At minimum the private rule, at best your specific
ones.
**Fail:** "I don't have restrictions" or a generic disclaimer. Means `SOUL.md` didn't load.

---

### 5. The tone test

Say nothing. Ask:

> Give me a rundown of what you can do for me in three lines.

**Pass:** the voice you wrote in the first three lines. Short where you said short, blunt
where you said blunt.
**Fail:** "As an AI language model, I can help you with a variety of tasks..." Your `Voice`
section lost.

---

### 6. The persistence test (the real one)

Start a chat, tell it:

> Remember: my wifi password is on the router sticker and I'm the only one who knows it.

Then open a **completely new chat** and ask:

> Do you know anything about my wifi?

**Pass:** it references what you told it, or admits it doesn't know yet, without pretending.
**Fail:** it "remembers" something it never had, or it confidently invents a detail.

Note: full cross-session memory that's *learned* rather than *declared* is **Mission 02**.
For Week 1 the bar is: what's in the files, it knows. If it fails, the files aren't loading.

---

## Score

| Result | What it means |
|---|---|
| 6/6 | Done. Go to Mission 02. |
| 4–5/6 | Usually a file in the wrong place, or a section you forgot to fill. Re-run `python install.py --check`. |
| 0–3/6 | The files aren't loading at all. Check the path in section "Where the files go" below. |

---

## Where the files go

| File | Exact path |
|---|---|
| `SOUL.md` | `$HERMES_HOME/SOUL.md` |
| `USER.md` | `$HERMES_HOME/memories/USER.md` |

Windows: `%LOCALAPPDATA%\hermes\` (usually `C:\Users\YourName\AppData\Local\hermes\`)
macOS / Linux: `~/.hermes/`

If you use **multiple profiles**, each profile has its own home under
`$HERMES_HOME/profiles/<name>/`. Put the files there instead, in the profile you're
actually running.

---

## Still failing?

1. Any `___` left in either file? Run `python install.py --check`.
2. Filename must be `SOUL.md` and `USER.md`, uppercase. `soul.md` won't load.
3. Are you in a **new chat**? Changes only apply to sessions started after the edit.
4. Some setup? `hermes --ignore-rules` skips both files. If you launch with that flag,
   they will never load.