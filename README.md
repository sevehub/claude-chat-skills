# Claude chat skills

One-chat skills for [Claude](https://claude.ai): instructions that apply to a single conversation and are never installed. Paste one into the first message of a chat, work, and close the chat. The next chat starts clean.

Browse and copy them at **<https://sevehub.github.io/claude-chat-skills/>**.

## Skills

| Skill | What it does | Text |
|---|---|---|
| `ai-work-log` | Turns a chat into a short card (title, goals status, takeaways, signed findings) for the [AI Work Log](https://www.amazon.com/dp/B0HMNZ53ZZ) paper logbook, exports cards to Logseq markdown, and builds a weekly tally. | [ai-work-log.txt](https://sevehub.github.io/claude-chat-skills/skills/ai-work-log.txt) |

More will be added over time, always as one-chat skills.

## Use a skill

1. Open the [listing](https://sevehub.github.io/claude-chat-skills/) and tap **Copy text** on the skill.
2. In a chat where Claude can open links, send the skill's `.txt` link with the words "apply this skill for this whole chat".
2. Or paste it as the first message of a new Claude chat, followed by your task.

These are not uploaded in Claude's Skills settings. Pasting keeps a skill scoped to one chat, and a pasted copy never goes stale.

## Add a skill

Put a Markdown file in `skills/` that starts with front matter:

```
---
name: my-skill
description: One sentence on what it does and when to use it.
---
```

then run `python gen.py` and commit `docs/`.

## Layout

```
skills/    one .md file per skill
gen.py     builds docs/ from skills/
docs/      generated site served by GitHub Pages
```

Edit `skills/` only, never `docs/`. Publish with Settings, Pages, Deploy from a branch, `main`, folder `/docs`.

## Feedback

Feedback goes through [issues](../../issues/new/choose). Pull requests are switched off. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Not affiliated

An independent project, not affiliated with, sponsored by, or endorsed by Anthropic. Claude is a trademark of Anthropic.

## License

[MIT](LICENSE)
