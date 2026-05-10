---
title: "Get Shit Done: Meta-prompting and spec-driven development that actually works"
date: '2026-05-12T10:00:00-03:00'
slug: get-shit-done-meta-prompting-e-spec-driven-development-para-agentes-de-ia
lang: en
translationKey: get-shit-done-meta-prompting-e-spec-driven-development-para-agentes-de-ia-2026-05-12
tags:
  - ai
  - spec-driven-development
  - claude-code
  - meta-prompting
  - context-engineering
draft: false
description: "A lightweight yet powerful meta-prompting and spec-driven development system for Claude Code, OpenCode, Gemini CLI, and others. Solves the context rot that degrades quality in long AI sessions."
---

# Get Shit Done: Meta-prompting and spec-driven development that actually works

Long sessions with AI agents have a silent problem: **context rot**. The more you use the agent, the more quality degrades. The context fills up, the agent starts forgetting things you discussed at the beginning, responses become more generic, errors become more frequent.

I've been through this. You start a session excited, the agent delivers excellent code in the first few hours, but after about 10-15 interactions, things go sideways. It suggests solutions that contradict what you agreed on, proposes unnecessary refactors, or simply loses track of what you wanted to build.

The problem isn't the model. It's how we manage context.

That's when I discovered [**Get Shit Done (GSD)**](https://github.com/gsd-build/get-shit-done).

## What is GSD?

It's a lightweight system of meta-prompting, context engineering, and spec-driven development created by TÂCHES. The proposal is simple: solve context rot by keeping your main context clean, doing the heavy lifting in subagents with fresh contexts.

The difference from other spec-driven development tools? GSD was made for developers working alone, not for 50-person organizations with sprint ceremonies and Jira flows. The complexity is in the system, not in your workflow.

## The 6-command loop

GSD operates in a simple loop of six commands:

### 1. Initialize
```
/gsd-new-project
```
Questions → research → requirements → roadmap. You approve, then construction begins.

Already have code? Run `/gsd-map-codebase` first. It analyzes your stack, architecture, and conventions so the new project asks the right questions.

### 2. Discuss
```
/gsd-discuss-phase 1
```
Your roadmap has one sentence per phase. That's not enough to build the way *you* imagine. Discuss captures your decisions before planning: layouts, API structure, error handling, data structures — any gray area of that specific phase.

Skip this step, you receive reasonable patterns. Use it, you receive your vision.

### 3. Plan
```
/gsd-plan-phase 1
```
Research → planning → verification, in a loop until plans pass. Each plan is small enough to execute in a fresh context window.

### 4. Execute
```
/gsd-execute-phase 1
```
Plans execute in parallel batches. Each executor receives 200k tokens of fresh context. Each task receives its own atomic commit. You leave, come back, and find the work complete with a clean git history.

Your main context window stays at 30-40%. The work happens in subagents.

> PHASE is how you divide work within a milestone.

### 5. Verify
```
/gsd-verify-work 1
```
You review what was built. Anything broken receives a diagnosed correction plan — ready for immediate re-execution. You don't debug manually; just run execute again.

### 6. Repeat → Ship
```
/gsd-ship 1
/gsd-complete-milestone
/gsd-new-milestone
```

Loop discuss → plan → execute → verify → ship until the milestone ends. Then archive, create tag, and start the next one from scratch.

> SHIP is the command that creates the Pull Request with the verified phase work.

> Milestones are groupings of phases that make sense together. You define how many phases you want in each milestone.

## Why it works

Three things most AI-coding setups get wrong:

**1. Context accumulation.** The more the session grows, the more quality degrades. GSD keeps your main context clean by doing the heavy lifting in fresh subagent contexts. Researchers, planners, and executors each start from scratch with exactly what they need.

**2. No shared memory.** GSD maintains structured artifacts that survive between sessions:
- `PROJECT.md` — vision
- `REQUIREMENTS.md` — scope
- `ROADMAP.md` — where you're going
- `STATE.md` — current position and decisions
- `CONTEXT.md` — implementation decisions by phase

Every new session loads these files and knows exactly where things are.

**3. No verification.** Code that "runs" isn't code that "works." GSD's verify step guides you through what was built, diagnoses failures with dedicated debug agents, and generates correction plans before you declare a phase complete.

## Installation

Installation is simple:

```bash
npx get-shit-done-cc@latest
```

The installer asks for your runtime (Claude Code, OpenCode, Gemini CLI, Kilo, Codex, Copilot, Cursor, Windsurf, and more) and whether you want to install globally or locally.

```bash
claude --dangerously-skip-permissions
opencode --dangerously-skip-permissions
gemini-cli --dangerously-skip-permissions
# ... depending on your agent
```

GSD is made for frictionless automation. Skip-permissions is the recommended mode to run.

## Main commands

| Command | What it does |
|---------|-----------|
| `/gsd-new-project` | Questions → research → requirements → roadmap |
| `/gsd-discuss-phase [N]` | Captures implementation decisions before planning |
| `/gsd-plan-phase [N]` | Research + planning + verification |
| `/gsd-execute-phase <N>` | Executes plans in parallel batches |
| `/gsd-verify-work [N]` | Manual acceptance tests |
| `/gsd-ship [N]` | Creates PR of verified phase work |
| `/gsd-progress --next` | Auto-detects and runs the next step |
| `/gsd-complete-milestone` | Archives milestone and creates release tag |
| `/gsd-new-milestone` | Starts next version |

## Configuration

Settings are in `.planning/config.json`. Some key options:

| Config | What it controls |
|--------|----------------|
| `mode` | `interactive` (confirm each step) or `yolo` (auto-approve) |
| Model profiles | `quality` / `balanced` / `budget` — controls which model each agent uses |
| `workflow.research` / `plan_check` / `verifier` | Turn on/off quality agents that add tokens and time |
| `parallelization.enabled` | Runs independent plans simultaneously |

## What won me over

GSD has 61k+ stars on GitHub and is used by engineers at Amazon, Google, Shopify, and Webflow. What won me over was the simplicity: just a few commands that do exactly what they promise.

It's not over-engineered. It doesn't try to be an enterprise platform. It's a system that understands solo devs need something that works without bureaucracy.

The idea of maintaining structured artifacts that survive between sessions is genius. You can close the laptop, come back tomorrow, and the agent knows exactly where it left off. No need to re-explain anything.

And the verify step is something I didn't see in other tools. Most stop at "execute" and assume it worked. GSD forces you to verify, and when it finds problems, it already generates the correction plan.

## Considerations

If you use Claude Code (or another agent) regularly and feel that quality degrades in long sessions, GSD is practically mandatory. It's the difference between "the agent sometimes works" and "the agent is reliable."

The learning curve is smooth — it's six main commands — but the impact on the quality of delivered code is huge.

---

**Links:**
- [Get Shit Done on GitHub](https://github.com/gsd-build/get-shit-done)
- [Complete documentation](https://github.com/gsd-build/get-shit-done/blob/main/docs/USER-GUIDE.md)
- [Architecture](https://github.com/gsd-build/get-shit-done/blob/main/docs/ARCHITECTURE.md)
- [Community Discord](https://discord.gg/mYgfVNfA2r)
