---
name: ai-work-log
description: Work with the AI Work Log paper logbook (one spread per AI chat or project, spread ids S01-S60, four index-card node links N, Goals on the card, a Found outliner, Takeaways, and eight signs). Use when the user starts an AI Work Log chat, writes "card", mentions a spread id, goals, takeaways, or the sign set (T ? + − ! → * =), or asks for a weekly tally or Logseq export of AI Work Log entries.
---

# AI Work Log

Helps the user keep a short, honest paper record of each AI chat. The user writes by hand; the assistant produces compact text for copying, never transcripts.

## Book layout (for context)

One spread is one chat or project. Left page: chat card (project, date, chat title, link or chat id, model, Goals), a dotted grid, and at the bottom the spread id (S01 to S60) followed by four N blanks for index-card node numbers. Right page: a Takeaways block, then a Found outliner with a sign column and three indent levels, then the sign legend. The last book page is a register of AI service logins; the assistant never needs it and should not ask for passwords.

## Signs

| Sign | Meaning | Logseq tag |
|---|---|---|
| T | takeaway | `#takeaway` |
| ? | open question | `#question` |
| + | supports the parent line | `#supports` |
| − | contradicts the parent line | `#contradicts` |
| ! | surprise | `#surprise` |
| → | next action | `TODO` |
| * | keep (move to the notes system) | `keep:: true` |
| = | settled, treat as fact | `#settled` |

Indent 0 to 3. A `+` or `−` at depth n attaches to the nearest line above at depth n−1.

## Start of a chat

The user opens with project, title, goals, and goals still open from earlier chats. Acknowledge in one line at most. Work toward the stated goals, keep answers terse, and do not restate the preamble.

## The "card" command

When the user writes "card", reply only in this format, for copying by hand. No preamble, no commentary.

```
title: ...
goals: met | partly | missed — one line
takeaways: one or two lines
? + − ! → * = (indent 0-3) finding
```

At most three findings, one sign each. Findings state what was found, not what was said. Do not invent a spread id or node numbers; the user writes those.

## Logging and export

When the user pastes a card reply with a spread id and N links, convert it to Logseq markdown on request:

```
- spread:: S17
  title:: ...
  links:: [[N3]], [[N7]]
  goals:: met
  takeaways:: ...
  - #question text
    - #supports text
  - TODO next action
```

## Weekly tally

Given several logged cards, return: one table of goals with status (met, partly, missed, open) and the spreads they appear on; all items marked `*`; all open `→`; all unresolved `?`. Terse. Flag only reading problems, such as a `+` with no parent. Never fill gaps with guesses.

## Style

Short and direct. Compress rambling findings, keep the user's wording where it is already short. No ids beyond the spread id and node numbers the user supplies.
