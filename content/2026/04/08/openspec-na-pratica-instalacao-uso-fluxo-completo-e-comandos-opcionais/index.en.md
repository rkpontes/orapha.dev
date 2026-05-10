---
title: "OpenSpec in Practice: Installation, Usage, Complete Flow, and Optional Commands"
date: '2026-04-08T10:00:00-03:00'
slug: openspec-na-pratica-instalacao-uso-fluxo-completo-e-comandos-opcionais
lang: en
translationKey: openspec-na-pratica-instalacao-uso-fluxo-completo-e-comandos-opcionais-2026-04-08
tags:
  - ai
  - openspec
  - spec-driven-development
  - software-engineering
  - development
draft: false
description: "A complete and straightforward guide to installing and using OpenSpec in daily life: prerequisites, structure, recommended flow, and optional commands worth knowing."
---

# OpenSpec in Practice: Installation, Usage, Complete Flow, and Optional Commands

If you already use a code agent in your daily life, you've already noticed the pattern: when intention is vague, output is also vague. That's why I started studying **Spec-Driven Development (SDD)** tools more closely and, on this journey, **OpenSpec** became a very interesting option.

Its proposal is simple: before going out implementing, you organize the change in clear artifacts (proposal, specs, tasks and, when necessary, design), execute with more predictability, and maintain history of what changed in the system's expected behavior.

In this article, I'll detail everything you asked for, in a practical way:

1. How to install OpenSpec.
2. How to start in a new or existing project.
3. Which flow I recommend for daily use.
4. Which optional commands are worth knowing (CLI and slash commands).

## What is OpenSpec (without beating around the bush)

OpenSpec is an open source SDD framework for working with AI assistants. It adds a specification layer in the repository to reduce improvisation and increase predictability.

The main structure stays inside `openspec/`:

- `openspec/specs/`: current source of truth of the system.
- `openspec/changes/`: proposed changes in progress.
- `openspec/changes/archive/`: changes already completed and archived.

The real value is in this separation: you can clearly see the current state and what is being proposed, without mixing everything in chat conversation.

## Prerequisites

Before installing, ensure:

- `Node.js >= 20.19.0`
- A package manager (`npm`, `pnpm`, `yarn`, or `bun`)
- A local project (can be brownfield, no problem)
- A compatible code agent (Codex, Claude Code, Cursor, Copilot, etc.)

Quick commands to validate environment:

```bash
node --version
npm --version
```

## Installing OpenSpec CLI

### With npm

```bash
npm install -g @fission-ai/openspec@latest
```

### With pnpm

```bash
pnpm install -g @fission-ai/openspec@latest
```

### With yarn

```bash
yarn global add @fission-ai/openspec@latest
```

### With bun

```bash
bun install -g @fission-ai/openspec@latest
```

After installation:

```bash
openspec --version
```

If this command returns the version, the CLI is ready.

## Initializing in the Project

In the project root directory:

```bash
cd my-project
openspec init
```

In practice, this command:

- creates the `openspec/` folder
- generates instructions for the agent (including `AGENTS.md` in the project)
- configures integrations for supported tools

After `init`, I like to run:

```bash
openspec list
```

This already confirms if the structure is active and if there are open changes.

## Generated Structure and How to Read It

A typical change flow looks like this:

```text
openspec/
├── specs/
│   └── auth/
│       └── spec.md
└── changes/
    └── add-2fa/
        ├── proposal.md
        ├── tasks.md
        ├── design.md (optional)
        └── specs/
            └── auth/
                └── spec.md
```

Practical interpretation:

- `proposal.md`: why change and what will change.
- `specs/*`: requirement/behavior deltas.
- `tasks.md`: implementation checklist.
- `design.md`: technical decisions when necessary.

## Recommended Flow for Using OpenSpec in Daily Life

This is the flow I consider most balanced between rigor and speed.

### 1) Create the change proposal

In the agent, request an OpenSpec proposal for a specific feature.

Example with shortcut (when the tool supports):

```text
/openspec:proposal Add profile search filters
```

### 2) Review and validate before implementing

In terminal:

```bash
openspec list
openspec validate add-profile-search-filters
openspec show add-profile-search-filters
```

This is where you cut ambiguity and avoid rework.

### 3) Refine proposal/specs/tasks

If clarity is lacking, ask the agent to adjust criteria, scenarios, and tasks until it becomes executable.

### 4) Implement based on tasks

```text
/openspec:apply add-profile-search-filters
```

The idea is to implement on top of `tasks.md` and not on improvisation.

### 5) Archive the completed change

In the agent:

```text
/openspec:archive add-profile-search-filters
```

Or via CLI:

```bash
openspec archive add-profile-search-filters --yes
```

When you archive, the change leaves the "in progress" state and starts composing the consolidated history.

## Main Commands (CLI)

In real use, these are the commands that matter most:

```bash
openspec init
openspec list
openspec view
openspec show <change>
openspec validate <change>
openspec archive <change> --yes
openspec update
```

Quick summary:

- `init`: initializes OpenSpec in the repo.
- `list`: lists open changes.
- `view`: interactive dashboard.
- `show`: displays proposal/tasks/spec deltas of a change.
- `validate`: validates specs format/structure.
- `archive`: archives completed change.
- `update`: updates instructions and bindings for agents in the project.

## Shortcut Commands in the Agent

They depend on the tool, but the current OpenSpec pattern in several native integrations is:

- `/openspec:proposal`
- `/openspec:apply`
- `/openspec:archive`

In some contexts/documentations you'll also find the **OPSX** (experimental) flow, with commands like:

- `/opsx:new`
- `/opsx:continue`
- `/opsx:ff`
- `/opsx:apply`
- `/opsx:archive`

The important point: check which set of commands your integration installed at `init`.

## Common Errors (and How to Avoid)

1. Skip proposal review and go straight to implementation.
2. Accept `tasks.md` without checking order and dependencies.
3. Not validate specs (`validate`) before applying.
4. Mix commands from different docs without checking your integration.
5. Not archive completed change (becomes mess quickly).

## An Example of End-to-End Execution

```bash
# 1) Install
npm install -g @fission-ai/openspec@latest

# 2) Initialize in project
cd my-project
openspec init

# 3) Check state
openspec list

# 4) In agent, create proposal
# /openspec:proposal Add profile search filters

# 5) Review in terminal
openspec validate add-profile-search-filters
openspec show add-profile-search-filters

# 6) In agent, implement
# /openspec:apply add-profile-search-filters

# 7) Archive change
openspec archive add-profile-search-filters --yes
```

## Closing

When you install, initialize, and follow a minimal flow of proposal, review, application, and archiving, the quality of execution with agents rises a lot.

And the best: you maintain real traceability of technical intention, without depending on chat memory.
