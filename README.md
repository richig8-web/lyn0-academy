# LYN_0 Academy

**Build your own personal AI agent, one mission at a time.**

Most people use an AI that starts every conversation at zero. It doesn't know your name, your
job, your files, or what you told it last Tuesday. An *agent* is different: it has an identity
and a memory of its owner, both loaded before it ever sees your message.

This repository holds the mission packs. One folder per week. Install it, run it, and your
agent becomes measurably less generic every week.

---

## Mission 01 — Your AI learns who it's working for

**Status: free and complete.** This is the whole pack, nothing held back.

| File | What it is |
|---|---|
| `mission.md` | The mission itself: why it matters, the mechanism, the 5 steps |
| `questionnaire.md` | 11 questions. Fill it in once, properly |
| `files/SOUL_TEMPLATE.md` | Who your AI **is**: name, voice, boundaries, what it decides alone |
| `files/USER_TEMPLATE.md` | Who your AI **works for**: job, tools, constraints, off-limits files |
| `install.py` | Finds your Hermes home, backs up what's there, installs the templates |
| `test.md` | 6 checks to run in a **fresh session**, so you know it loaded on its own |

**Time:** about 45 minutes, once.

### Quick start

```bash
cd 01-know-your-owner
python install.py            # installs SOUL.md and memories/USER.md
# now edit both files and replace every ___ with your own answers
python install.py --check    # tells you what's still blank or missing
```

Then open `test.md` and run the six checks **in a new chat**.

`install.py --force` overwrites without asking. Existing files are backed up to
`<hermes-home>/backups/` automatically, with a timestamp, every time.

### Requirements

- [Hermes Agent](https://hermes-agent.nousresearch.com/) installed and running on your own
  machine.
- Python 3.9 or newer for the installer. Nothing else. No dependencies, no network calls.

On Windows the Hermes home is `%LOCALAPPDATA%\hermes`, on macOS and Linux it's `~/.hermes`.
`install.py` resolves it for you, or pass `--home` to point somewhere else.

---

## What this actually gives you

`SOUL.md` and `USER.md` are not documentation. They are injected into the system prompt on
**every single turn**. That means:

- what you write there is what your agent knows, forever, starting now
- an agent with a name stops feeling like a tool
- "never touch this folder" in the file is worth more than saying it again next week

The next missions add memory that survives, hands, documents, automations and a way to check
its own work. Mission 01 is the part everything else assumes.

---

## Roadmap

| Week | Your AI learns to |
|---|---|
| **01** | **know its owner** ← this repo |
| 02 | build its own memory |
| 03 | read and organize your documents |
| 04 | use email and messages |
| 05 | navigate the web on its own |
| 06 | use your programs and tools |
| 07 | create automations |
| 08 | work with files, PDFs and data |
| 09 | run recurring tasks |
| 10 | check what it did |
| 11 | create new skills |
| 12 | become a real personal agent |

Missions 02 to 12 ship weekly. Mission 01 stays free.

**Week 2 is out: [Mission 02 — memory that survives](https://richig8-web.github.io/lyn0-memory-pack/),
$9, one payment.** A memory file the agent writes itself, the rules for what goes in it, and a
review skill that proposes a diff before it changes anything. It assumes you finished week 1.

One piece of week 2 is free on its own, because it is useful even if you never open the pack:
[`hermes-memory-audit`](https://github.com/richig8-web/hermes-memory-audit) reads both memory
files, prints every entry against its character budget, and flags what is rotting.

---

## Feedback wanted

Run the six checks and tell me where it breaks. The failure I'm most curious about is the
agent contradicting the file you just wrote. Open an issue with what you wrote in `SOUL.md`
and `USER.md` (redact anything private) and what the agent did instead.

---

## License

MIT. See [LICENSE](LICENSE). Use it, fork it, ship it, sell whatever you build with it.
