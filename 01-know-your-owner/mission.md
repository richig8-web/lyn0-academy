# Mission 01 — Your AI learns who it's working for

> **Week 1 of 12.** By the end of this mission your AI is no longer a stranger with a blank
> memory. It knows your name, your job, your setup, your deadlines, and what you want it to
> do. Everything in Week 2 onward assumes this one worked.

**Time:** about 45 minutes, once.
**You'll need:** Hermes Agent installed and running on your own machine.

---

## Why this matters (read this before you touch a file)

Every generic AI you use today starts every conversation at zero. It doesn't know you. It
can't tell if you said something last Tuesday or three years ago. That's why you re-explain
yourself, your job, your projects, every single time.

An **agent** is different. An agent has a **soul** (who it is) and a **memory of its owner**
(who it works for). Those two files get loaded into its brain before every message it ever
receives. Set them once, and it stops being a chatbot.

Here's the actual mechanism, so nothing here is magic:

| File | Lives at | What it does |
|---|---|---|
| `SOUL.md` | `$HERMES_HOME/SOUL.md` | Who your AI **is**. Name, voice, boundaries, style. Always loaded. |
| `USER.md` | `$HERMES_HOME/memories/USER.md` | Who your AI **works for**. Name, job, tools, goals, pet names. Always loaded. |

These two files are not documentation. They're injected into the system prompt on every
single turn. What you write there is what your AI *knows*, forever, starting now.

---

## Step 1 — Take the Identity Questionnaire (10 min)

Open `questionnaire.md` in this folder. Fill it in like you're writing to a person you're
hiring, not filling in a form.

Rules:
- **Real answers only.** "Runs a small business, hates mornings, uses Gmail and Excel" beats
  "I'm a professional who values efficiency."
- **Specifics over adjectives.** Your AI can act on "3 kids, school pickup at 15:30". It
  cannot act on "I'm busy".
- **Write the ugly stuff too.** Health, money, constraints, what you never want touched.
  This is the file that keeps your AI from doing something you'll hate.

Keep it open in a text editor, you'll paste pieces of it in Step 2.

---

## Step 2 — Write your AI's soul (15 min)

Open `files/SOUL_TEMPLATE.md` in a text editor. Every line with `___` is yours to write.

The minimum viable version is three lines:

```markdown
# Who You Are
Your name is ____. You are ____'s personal AI.

## Voice
- ...

## Boundaries
- Never ____ without asking first.
```

But do it properly. The sections that matter most:

- **Who You Are** — the name and the one-sentence job description. If your AI has a name,
  it will use it, and it will start feeling like a thing instead of a tool.
- **Voice** — 3 to 5 rules. Not "be friendly". Be concrete: "short answers unless I'm
  debugging", "no emojis", "push back when you think I'm wrong".
- **How You Work** — this is the part people skip and it's the part that matters. Tell it
  what to do *before* asking you: what it may decide alone, what it always confirms first,
  what it never does without you.
- **Boundaries** — the private stuff stays private rule, plus anything specific to your life.
  (Recurring medical doc folder: never open without asking. Ex's number: blocked.)

Save it as `$HERMES_HOME/SOUL.md`. On Windows that's:
`C:\Users\YOURNAME\AppData\Local\hermes\SOUL.md`

---

## Step 3 — Load the owner profile (10 min)

Open `files/USER_TEMPLATE.md`. Same deal: fill in the blanks from your questionnaire.

Save as `$HERMES_HOME/memories/USER.md`. On Windows:
`C:\Users\YOURNAME\AppData\Local\hermes\memories\USER.md`

Keep it **compact**. This file is loaded on every turn, so every wasted word is a tax you
pay forever. Facts, not essays. If you want to go deep on something, put it in a file the AI
can read on demand (that's Week 3).

---

## Step 4 — Run the installer

Rather than pasting paths by hand, run:

```bash
python install.py
```

It finds your Hermes home, checks whether `SOUL.md` and `USER.md` already exist, backs them
up, and installs the files from `files/` so you can start from the templates. If you skipped
straight to writing your own, run `python install.py --check` instead to just verify the
files landed in the right place.

---

## Step 5 — Run the test (5 min)

Open `test.md` and run all six checks **in a brand new chat**. Not the one you're reading
this in. A fresh session is the only honest test, because that proves the files load on
their own and not because you just explained everything.

Pass all six? Your AI knows you. Welcome to Week 1.

---

## What just happened

You didn't take a course. You installed an identity into a piece of software that's running
on your own hardware, with your data, that you control and can turn off.

That's the whole trick. The next 11 weeks just add hands to it.

---

## Next — Mission 02: memory that survives

Right now your AI knows what you *told* it in a file. Week 2 teaches it to remember what
*happened*: the decision you made last Tuesday, the fact you corrected it, the thing you'll
want in a month. That's the difference between an AI that knows you and an AI that has a
history with you.

The pack is out now at **$9, one payment**: [Mission 02 — memory that
survives](https://richig8-web.github.io/lyn0-memory-pack/). The memory audit script is free
either way: [`hermes-memory-audit`](https://github.com/richig8-web/hermes-memory-audit).

---

## Support

Stuck, or your agent contradicts the file you just wrote? Screenshot it and post in the
group. Include your `SOUL.md` and `USER.md` contents (with private bits redacted) — that
fixes 9 out of 10 issues in one round.