---
title: "Graphify: Transforming your project into a knowledge graph that AI agents understand"
date: '2026-05-10T10:00:00-03:00'
slug: graphify-transformando-seu-projeto-em-grafo-de-conhecimento-para-agentes-de-ia
lang: en
translationKey: graphify-transformando-seu-projeto-em-grafo-de-conhecimento-para-agentes-de-ia-2026-05-10
tags:
  - ai
  - knowledge-graph
  - graphify
  - claude-code
  - codex
  - opencode
draft: false
description: "How to transform any folder of code, documents, PDFs, and even videos into a queryable knowledge graph. A skill for Claude Code, Codex, OpenCode, and other AI agents."
---

# Graphify: Transforming your project into a knowledge graph that AI agents understand

Working with large projects using AI agents has a classic problem: context. You open the chat, ask a question about how authentication works in your system, and the agent starts grepping around, opening random files, wasting time with irrelevant code. When your project has thousands of files, this "searching in the dark" approach doesn't scale.

I've been through this many times. And the truth is that agents are good at understanding code but bad at understanding the **structure** of code. They don't have a mental map of the project. They don't know what's connected to what, they don't see architectural patterns, they don't capture design decisions scattered in comments and documentation.

That's when I discovered [**Graphify**](https://github.com/safishamsi/graphify).

## What is Graphify?

Graphify is a skill for code agents (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, VS Code Copilot Chat, Aider, and more) that transforms any folder of content into a **queryable knowledge graph**.

And when I say "any folder," I'm talking about:
- Code in 28 languages (Python, TypeScript, Go, Rust, Java, etc.)
- SQL schemas
- Shell scripts
- Documentation (Markdown, HTML, TXT)
- Office files (docx, xlsx)
- PDFs
- Images (PNG, JPG, WebP)
- Video and audio (MP4, MOV, MP3, WAV)
- YouTube URLs
- Google Workspace documents

The idea is simple: instead of letting the agent mine files in the dark, you create an intelligent map of the project that it can navigate.

## How it works

Installation is straightforward:

```bash
uv tool install graphifyy && graphify install
# or: pipx install graphifyy && graphify install
# or: pip install graphifyy && graphify install
```

Then, just run it in your project:

```
/graphify .
```

Done. Graphify will generate three files:

```
graphify-out/
├── graph.html       # Interactive visualization — open in browser
├── GRAPH_REPORT.md  # Executive summary with highlights and suggested questions
└── graph.json       # Complete graph for programmatic queries
```

The `graph.html` is particularly useful. You can click on nodes, filter, search. It's a visual way to understand how the pieces of your project connect.

## What's in the report

The `GRAPH_REPORT.md` is where things get interesting. It includes:

- **God nodes** — the most connected concepts in the project. Everything goes through them.
- **Surprising connections** — links between things that live in different files or modules, ranked by how unexpected they are.
- **The "why"** — inline comments (`# NOTE:`, `# WHY:`, `# HACK:`) and docstrings extracted as separate nodes.
- **Suggested questions** — 4-5 questions the graph is positioned to answer.
- **Confidence tags** — each relation is marked as `EXTRACTED` (found in code), `INFERRED` (inferred), or `AMBIGUOUS` (ambiguous).

This means you can ask the agent: "what connects authentication to the database?" and it will query the graph instead of grepping around.

## Integration with agents

Graphify has native integration with several platforms:

| Platform | Command |
|------------|---------|
| Claude Code | `graphify install` |
| Codex | `graphify install --platform codex` |
| OpenCode | `graphify install --platform opencode` |
| Cursor | `graphify cursor install` |
| VS Code Copilot Chat | `graphify vscode install` |
| GitHub Copilot CLI | `graphify install --platform copilot` |
| Gemini CLI | `graphify install --platform gemini` |
| Aider | `graphify install --platform aider` |

After installing, you can make the agent always use the graph:

```bash
graphify claude install
```

This writes a configuration file that tells the assistant to read the `GRAPH_REPORT.md` before answering questions about your codebase. On platforms that support hooks (Claude Code, Codex, Gemini CLI), a hook triggers automatically before each file read call.

## Querying the graph

Besides letting the agent use it automatically, you can query the graph directly:

```
/graphify query "what connects auth to the database?"
/graphify path "UserService" "DatabasePool"
/graphify explain "RateLimiter"
```

Or via terminal:

```bash
graphify query "show the auth flow"
graphify query "what connects DigestAuth to Response?" --graph graphify-out/graph.json
```

For MCP (Model Context Protocol) integration, you can expose the graph as a server:

```bash
python -m graphify.serve graphify-out/graph.json
```

This gives your assistant structured access via functions like `query_graph`, `get_node`, `get_neighbors`, `shortest_path`.

## Team and versioning

Graphify was designed for teamwork. The `graphify-out/` directory is meant to be committed to git. The recommended workflow:

1. One person runs `/graphify .` and commits `graphify-out/`
2. Everyone pulls — their assistants read the graph immediately
3. Run `graphify hook install` for auto-rebuild on every commit
4. When docs or papers change, run `/graphify --update`

There's even a merge driver to avoid conflicts in `graph.json` when two devs commit in parallel.

## Privacy

One thing I care about is privacy. Here's how it works:

- **Code files** — processed locally via tree-sitter. Nothing leaves your machine.
- **Video/audio** — transcribed locally with faster-whisper. Nothing leaves your machine.
- **Docs, PDFs, images** — sent to your AI assistant for semantic extraction (using your IDE session's model).

No telemetry, no tracking, no analytics.

## Why this matters

For me, Graphify's value is in three places:

**First, efficiency.** Instead of letting the agent open dozens of files looking for context, it navigates a structured graph. Less tokens spent, faster responses.

**Second, discovery.** The graph shows connections you might not have noticed. That utility function used in 15 different places. That module that bridges two seemingly disconnected domains.

**Third, onboarding.** When someone new joins the project, the graph is a map. Instead of reading thousands of files, you explore the graph. See the god nodes, understand the architecture, discover the patterns.

## Final considerations

Graphify is one of those tools that seems obvious after you use it. Transforming code into a knowledge graph makes total sense when you work with AI agents. It's like giving them a map instead of letting them explore in the dark.

If you work with large projects and use code agents regularly, it's worth trying. The learning curve is practically zero — install, run `/graphify .`, and start using.

The repository has 45k+ stars and an active community. It's constantly evolving with support for new platforms and file formats.

---

**Links:**
- [Graphify on GitHub](https://github.com/safishamsi/graphify)
- [Complete documentation](https://github.com/safishamsi/graphify/blob/v7/docs/how-it-works.md)
- [Official website](https://graphifylabs.ai)
