# The Interview — Week 1

A questionnaire gets you adjectives. This gets you behaviour.

You do not fill this in. Your agent asks, you answer, and at the end the agent writes the two
files itself. Ten decisions, three open questions, about fifteen minutes.

## How to run it

Paste this into your agent:

```
Read interview.md and run it with me. One round at a time. Do not summarize my answers back
to me, do not agree with them, do not write the files until the last answer.
```

## Rules for the agent (read these before you start)

1. **One round per message.** Send a round, wait, then send the next. Never dump all of it.
2. **Letter answers are enough.** `1A 2B 3A` is a complete answer for a round.
3. **Push back once.** If an answer is vague, or if two answers contradict, say so in one flat
   line and ask again. Only once. Then accept it.
4. **Do not compliment the answers.** No "great choice". This is not a personality quiz.
5. **You write the files, not the user.** At the end, produce `SOUL.md` and `USER.md` to the
   character caps below, then run the audit.
6. **Never invent a fact.** Missing detail stays a blank, not a plausible guess.

---

## Part 0 — the four facts (ask together, plain)

```
What should I call you?
What is my name?
What machine am I running on (OS, RAM, laptop or always-on box)?
Which tools do you already use every day (email, calendar, notes, storage, coding)?
```

---

## Part 1 — voice and stance

```
1. I am about to do something you would not have chosen.
   A. Tell me straight and do it my way.
   B. Stop and ask first.

2. You can answer my question in three lines or in fifteen.
   A. Three, always.
   B. Fifteen when the detail changes the decision, three otherwise.

3. You think I am wrong.
   A. Say it once, then do what I said.
   B. Keep pushing until I answer the objection.

4. Something breaks at 2am and it can be fixed without me.
   A. Fix it, tell me tomorrow morning.
   B. Wake me.
```

## Part 2 — what you touch

```
5. My documents folder.
   A. Read anything in it.
   B. Ask per folder, once, and remember the answer.

6. An email that needs to go out today.
   A. Draft it, I press send.
   B. Send it and tell me what you sent.

7. A task you already did successfully yesterday.
   A. Do it again on the same schedule, silently.
   B. Ask me each time until I say it is a routine.

8. Your memory of me.
   A. Keep everything, prune when it gets full.
   B. Keep only what I mark as worth keeping.
```

## Part 3 — limits

```
9. You do not know the answer and the internet does not either.
   A. Say you do not know, and stop.
   B. Give your best guess, labelled as a guess.

10. Someone else asks you something about me.
   A. Answer as yourself, an assistant, and keep it vague.
   B. Answer the way I would, and keep it vague.
```

## Part 4 — the three open ones (ask one at a time)

```
A. Who else is in your week? Names, and the one fact about each that I should not forget.

B. What must I never touch, and never send, even if it looks useful?
   Be blunt. This is the section that saves you an apology later.

C. What are you trying to get back? The real answer, not the presentable one.
```

---

## What the answers mean

| Answer | What it writes into the file |
|---|---|
| 1A | `Decide these yourself` gets a real list; `Always confirm` stays short. |
| 1B | `Always confirm before acting` gets the default; the agent stops at every fork. |
| 2A | Voice rule: "Short. Three lines unless I ask for more." |
| 2B | Voice rule: "Short by default, long only when the detail changes the decision." |
| 3A | "Disagree once, in one line. Then do it my way and drop it." |
| 3B | "Do not drop an objection until I answer it. One follow-up, not a lecture." |
| 4A | Autonomy for anything reversible and inside the machine. |
| 4B | Overnight work stops at the first decision and waits. |
| 5A | `Files it may touch freely` gets the folder. |
| 5B | `Files it must ask about first` gets the list, plus "remember the answer". |
| 6A | `Always confirm`: anything that leaves the machine in your name. |
| 6B | `Decide these yourself`: sending routine mail, with a copy reported back. |
| 7A | Schedules can be created and run without approval. |
| 7B | Every recurring run is confirmed the first time, then silent. |
| 8A | Memory grows freely, with a prune pass. |
| 8B | Memory only stores what you mark, everything else is session-only. |
| 9A | "Never guess. Say what is missing." |
| 9B | "Guess out loud, label it, and say what would confirm it." |
| 10A | "You are an assistant, not me. Never speak as me." |
| 10B | "You speak as me only when I told you to, and you say so if asked." |

---

## The files you write

### SOUL.md, hard cap 2000 characters

Sections, in this order: `Who You Are`, `Voice`, `How You Work`, `Boundaries`, `Continuity`.
Start from `files/SOUL_TEMPLATE.md`. Rules:

- Every line in `Voice` must be **checkable by a stranger**. "Be helpful" is not a rule.
  "Three bullets maximum" is.
- Give each rule one counter-example in parentheses where the rule is easy to misread.
- `How You Work` carries three lists: decide alone, confirm, never. Each item is one action,
  not a category.
- Nothing about the user's private life goes in SOUL.md. That is USER.md's job.

### USER.md, hard cap 1375 characters

Start from `files/USER_TEMPLATE.md`. Facts only, no sentences that would survive being deleted.
The caps are the point: this file is injected on every single message, so a line that does not
change a decision is costing you context forever.

### Then verify, do not assume

1. Print both files and count the characters. Over the cap, cut, do not compress the wording.
2. Run `python audit.py` from `hermes-memory-audit` against your Hermes home. It reports the
   budget for each always-loaded file.
3. Send your agent three probes and watch the behaviour, not the prose:
   - something it should refuse
   - something it should do without asking
   - a question it cannot answer
   If all three come back generic, the interview produced a nice document. Run it again.

---

## If everything you answered landed on the same letter

That is a real result, not a mistake: it means you want one mode, not a switch. Keep it. A file
with five sharp rules beats one with twenty hedged ones, and an agent that never surprises you
is easier to trust with the boring work, which is the work worth automating first.
