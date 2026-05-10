---
title: "How I've Been Using Spec-Driven Development with Spec Kit in My Projects"
date: '2026-04-03T10:00:00-03:00'
slug: como-eu-tenho-usado-spec-driven-development-com-o-spec-kit-nos-meus-projetos
lang: en
translationKey: como-eu-tenho-usado-spec-driven-development-com-o-spec-kit-nos-meus-projetos-2026-04-03
tags:
  - ai
  - spec-driven-development
  - spec-kit
  - software-engineering
  - development
draft: false
description: "A practical step-by-step of how I've been using Spec-Driven Development with Spec Kit to stop asking loose things to the agent and start working with more clarity and less improvisation."
---

# How I've Been Using Spec-Driven Development with Spec Kit in My Projects

If you've ever tried to build software with a code agent, you've probably been on this roller coaster. Some days things go really well. On others, the agent delivers half of what you asked for, invents a structure that makes no sense, breaks the build, or even does something that seems to work, but with a foundation that you yourself wouldn't do that way.

I've been thinking a lot about this. And, for me, the problem is almost never just in the model. Most of the time, the problem is in the way we ask. Loose request generates loose response. Poorly tied context generates crooked decision. And, when there's no clear way to say what needs to be built and how it will be validated, the chance of turning into improvisation is too high.

That's why I started looking more closely at **Spec-Driven Development**, or simply **SDD**. And, within that, a tool that caught my attention was **Spec Kit**, an open source toolkit created precisely to organize this workflow with agents.

In this text, I want to show you how I've been seeing this process in practice. Not as pretty talk, but as a more serious way of working with AI in development. The idea here is to get out of the thrown prompt in the chat and enter a flow with principles, specification, plan, tasks, and implementation.

## What bothers me about the so-called vibe coding

There's a way to use AI for programming that works really well for quick prototypes. You open the chat, send something like "create a login screen" and refine through trial and error. This has its value. I even do this at some moments.

The problem is when that same logic goes into a real project.

When the project needs to last more than an afternoon, when there's maintenance, when there's standard, when there's architecture, when there's technical responsibility, this model starts to make noise. Because the agent even recognizes pattern very well, but it doesn't guess intention. It needs direction.

That's when SDD started to make sense to me. The proposal is simple: instead of starting directly in code, I start with intention. I define project principles, describe what I want to build, organize technical decisions, and only then move to execution. Code continues to be important, of course, but it stops being the first thing in the conversation.

## What is Spec Kit

In the project's own definition, **Spec Kit** is an open source toolkit aimed at helping you focus on product scenarios and predictable results, instead of coding everything crazily.

The toolkit's central idea talks a lot with what I've been looking for in practice: transforming specification into an active part of development, and not into a dead document that only exists to fulfill a checklist.

Its main flow revolves around five stages:

1. `constitution`
2. `specify`
3. `plan`
4. `tasks`
5. `implement`

It seems simple, and indeed it is. The value isn't in inventing fashion. It's in putting the house in order.

## Before anything: what I like about this approach

What attracts me most here isn't "automating everything." It's precisely the opposite. It's creating a process in which I continue to hold the direction.

When I use this flow, I'm not outsourcing thought. I'm putting thought in order. AI enters as a partner in elaboration, refinement, and execution, but responsibility for quality continues to be mine.

This point is important because many people look at tools like this and imagine that the gain is in pressing a button and having a complete system come out. I don't see it that way. For me, the gain is in reducing noise and misunderstanding.

## Prerequisites

To use Spec Kit, you need to have some things in the environment:

- `uv` to manage CLI installation
- `Python 3.11+`
- `Git`
- A compatible agent

The project supports several agents. Among them, **GitHub Copilot**, **Claude Code**, **Codex CLI**, **Cursor**, **Gemini CLI**, and others.


## Installing the CLI

The recommended way by the project is to install the CLI with `uv tool install`.

Example:

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@vX.Y.Z
```

If you want to use the latest version from the main branch:

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
```

After that, you can already use commands like:

```bash
specify init <PROJECT_NAME>
specify check
```

If the idea is to run without installing persistently, you can also use `uvx`.

## Creating a project with Spec Kit

After installation, I initialize the project with `specify init`.

Example to create a new project:

```bash
specify init my-project --ai copilot
```

If I want to use it in the current directory:

```bash
specify init . --ai copilot
```

In the case of **Codex CLI**, I would use something like this:

```bash
specify init . --ai codex --ai-skills
```

If I were to do the same with **Claude Code**, it would be like this:

```bash
specify init . --ai claude
```

The `--ai-skills` detail matters because, in Codex, Spec Kit works as a skill instead of traditional slash command.

After `init`, the toolkit mounts the project structure base. Among files and folders, you'll typically see things like:

- `.specify/memory/constitution.md`
- `.specify/templates/`
- `.specify/scripts/`
- `.specify/specs/<feature>/`

In addition, it installs the commands that will guide the process.

After this base is ready, you can touch this flow the way that makes most sense in your daily life: in your preferred IDE's chat, in the agent via terminal, or in the tool you're using.

## Stage 1: defining principles with `constitution`

This is a part that I think is really good. Before talking about the feature, I define the principles that will command the project.

In the traditional Spec Kit flow, the command is:

```bash
/speckit.constitution
```

In Codex with skills, it would be equivalent to:

```bash
$speckit-constitution
```

Here I don't describe screen or endpoint. I describe quality rule and decision criterion.

Depending on context, this stage can also register operational rules and cross-cutting project requirements, such as test policy, branch flow, and minimum security requirements. If this changes how the work should be built and reviewed, it makes sense to declare it already in the `constitution`.

For example:

```text
Create principles focused on clean code. The project should be small and simple. Should not have automated tests in this first version.
```

The result of this goes to the project's constitution file. And what I like is that this pulls the next stages. The agent starts carrying these principles as reference.

This helps prevent something that bothers me a lot: the agent starting to invent fashion in a simple project.

## Stage 2: describing what I want to build with `specify`

After principles, I move to functional specification.

Here the focus is on **what** and **why**, not on stack. This separation makes a difference. If I mix functional requirement with technical detail too early, I myself tangle the conversation.

Example of command:

```bash
/speckit.specify
```

Or in Codex:

```bash
$speckit-specify
```

And then I pass something along these lines:

```text
Build an application that helps me manage my tasks and track daily activities. Tasks should have title, description, completion date, priority, and status. Include filters to view tasks by priority, status, or date.
```

From this, Spec Kit generates a specification with user stories, requirements, and acceptance checklist.

This is a part that I recommend reviewing carefully. Don't treat it as final just because the text looks neat. Read it for real. See if the stories make sense, if the scope didn't walk on its own, if the checklist is coherent.

## Stage 3: clarifying gaps with `clarify`

This stage is optional in the flow, but I'd say it helps a lot whenever the specification was vague at some point.

Command:

```bash
/speckit.clarify
```

The function here is simple: identify poorly defined points before technical planning. This avoids rework down the line.

I like this stage because it forces a more honest conversation with the problem. Sometimes we think we know what we want to build, but discover we haven't even decided basic behavior things.

If the feature is small, maybe I'll skip it. But, if there's any relevant ambiguity, I prefer to spend energy here than to screw up further ahead, in the middle of implementation.

## Stage 4: creating the technical plan with `plan`

Only here do I enter stack, architecture, and technical decisions.

Command:

```bash
/speckit.plan
```

Or:

```bash
$speckit-plan
```

Example prompt:

```text
The application should use TypeScript, React Native with Expo to run on Expo Go, with as few libraries as possible and Expo Router for navigation. Store data in SQLite with Expo SQLite. For this version, don't include automated tests.
```

What I find interesting about this stage is that the toolkit doesn't just stay in a generic summary. It tends to break the plan into more concrete things, such as:

- `plan.md`
- `research.md`
- `data-model.md`
- contracts
- quickstart
- architecture decisions

If the chosen stack changes quickly, this is a stage where it's worth researching version, compatibility, and specific detail a lot. Spec Kit's own documentation suggests deepening research when the technology is very dynamic.

## Stage 5: breaking the plan into tasks with `tasks`

After the plan, I generate the decomposition into tasks.

Command:

```bash
/speckit.tasks
```

Or:

```bash
$speckit-tasks
```

This stage transforms the plan into an executable list. And this is important because good implementation doesn't just depend on knowing what to build. It also depends on knowing **in what order** to build.

The `tasks.md` usually organizes work into phases, generally aligned with user stories, technical dependencies, and checkpoints.

This stage helps me see if the plan is really implementable. If the task list comes out weird, it's already a sign that the plan might still be poorly resolved.

## Stage 6: implementing with `implement`

With everything ready, then yes I ask to implement.

Command:

```bash
/speckit.implement
```

Or:

```bash
$speckit-implement
```

This stage picks up what was defined before and executes the implementation following what was tied in previous stages.

This is where many people get excited and think the work is done. For me, it's exactly the opposite. It's where the most important part begins: reviewing what was done with rigor and without covering up.

Because an implementation can follow the plan and still come out bad. It can come out with crooked UX, unnecessary structure, poorly placed abstraction, or half-finished pieces.

This is a great reminder. The process greatly improves consistency, but doesn't eliminate human review.

## A practical example of flow

If I were to summarize a real usage flow, it would look something like this:

```bash
specify init . --ai codex --ai-skills
```

Then, within the agent in **Codex**:

```text
$speckit-constitution
$speckit-specify
$speckit-clarify
$speckit-plan
$speckit-tasks
$speckit-implement
```

If I were to do the same in **Claude Code**, I would start like this:

```bash
specify init . --ai claude
```

Then, within the agent:

```text
/speckit.constitution
/speckit.specify
/speckit.clarify
/speckit.plan
/speckit.tasks
/speckit.implement
```

## What changes in practice when I work this way

For me, the main change is this: I stop negotiating with loose response and start working with something more tied up.

Instead of repeating "it wasn't this," "this was missing," "I didn't like the structure," I start to have intermediate stages where I can correct the route with much more clarity:

- principles
- specification
- clarifications
- technical plan
- tasks
- implementation

This reduces friction and also reduces that feeling that I'm fighting with the agent all the time.

## What I review at each stage

I don't blindly trust any stage. What I do is review each one with a different focus:

### In constitution

I look to see if the principles really reflect how I want the project to be conducted.

### In specification

I see if the problem was correctly described and if the requirements didn't escape the scope.

### In clarification

I look for nebulous points that can still become rework.

### In plan

I evaluate if the stack makes sense, if there wasn't excess, and if technical decisions are coherent with the constitution.

### In tasks

I observe if the implementation order is logical and if there isn't an obvious hole in the middle.

### In implementation

I verify real behavior, structure, adherence to principles, and technical finishing.

## Where this connects with how we work in companies

One important thing: I don't see SDD as a direct substitute for how teams already organize themselves in daily life.

In most companies, we work with some format of **Scrum**, **Kanban**, **Scrumban**, or some own mixture that was born from the team's reality. There's planning, refinement, daily, review, board card, priority changing in the middle of the week, and that controlled chaos that every team knows.

For me, SDD enters another layer.

It doesn't substitute backlog.
It doesn't substitute sprint.
It doesn't substitute board.
It doesn't substitute alignment with product.

What it does is improve the quality of the passage between intention and implementation.

In a team with **Scrum**, for example, I can very well imagine a story entering the sprint and being detailed with this flow of constitution, specification, plan, and tasks before heavy implementation begins.

In a team more pulled toward **Kanban**, this also makes sense, because you can use SDD as a way to leave each item that enters execution less nebulous and less dependent on loose interpretation in chat.

And in the case of **Scrumban**, which is the reality of many places, this fits perhaps even better, because you can maintain cadence, priority, and continuous flow without giving up specifying better what is being done.

So, at least today, I see SDD much more as a process complement than as a process substitution. It sits well alongside practices that most teams already use. The difference is that now there's a stronger way to structure the conversation between requirement, technical decision, and agent execution.

To be more concrete, imagine a common company task.

The card arrives more or less like this:

```text
Add status filter to the orders listing in the admin panel.
The user needs to be able to view orders by status: pending, paid, shipped, and cancelled.
```

In real life, this often enters the board just like this. Maybe it comes with a comment from product, maybe it comes with a Figma print, maybe it comes with half a dozen messages on Slack or Jira explaining superficially. Then the dev picks this up, interprets it their way, opens the project, and starts implementing.

It's exactly there that a lot of things go sideways.

Because questions start appearing that no one answered properly:

- can this filter be combined with text search?
- does the status come from backend or will it be mapped in frontend?
- does the filter need to persist in the URL?
- when there's no result, what state does the screen show?
- does this need to change pagination?
- is there performance impact or index in the database?

Without a better process, these answers end up scattered in card comment, daily conversation, chat message, and decision made on the fly during implementation.

---

Liking the article?


If this type of content makes sense to you, check out my YouTube channel:

[youtube.com/@o.raphadev](https://www.youtube.com/@o.raphadev)

Over there I talk about software engineering, AI applied to development, architecture, career, and these changes that are messing with our way of building software.

And, if you work with SaaS product and security is a real concern in your context, it's also worth knowing **BetaCoding**:

[betacoding.com.br](https://betacoding.com.br)

At BetaCoding, we work with a focus on **cybersecurity for SaaS**, looking at product protection in a way closer to the reality of those who build and maintain real software.

---

It's at this point that I see SDD entering.

Instead of coding on top of the raw card, I can take this task and go through a more organized flow:

1. In `specify`, I transform the loose request into a clearer description of expected behavior.
2. In `clarify`, I raise the questions that are still open.
3. In `plan`, I define how this enters the project's current stack.
4. In `tasks`, I break this into smaller, implementable steps.
5. In `implement`, then yes I execute.

If I were to do this in practice, it could look something like this.

### Example of task in current flow

```text
Task: add status filter to the orders listing in admin.

Acceptance criteria:
- filter by pending, paid, shipped, and cancelled
- allow clearing filter
- maintain current listing layout
```

### The same task entering SDD

In the `specify` stage, I would write something along these lines:

```text
Add to the orders listing screen in the admin panel the ability to filter orders by status. The user should be able to view pending, paid, shipped, and cancelled orders, in addition to removing the filter and viewing all orders again. The goal is to facilitate the administrative team's operation without altering the main listing layout.
```

In the `clarify` stage, I would probably raise questions like:

- can this filter be combined with the existing search?
- does the filter need to survive page refresh?
- does the backend already support this parameter or will it need adjustment?
- what should the behavior be when no orders are found?

In the `plan` stage, I would describe something more technical, for example:

```text
Implement the status filter reusing the current orders listing in admin. In frontend, add a simple selector above the table. Persist the filter in query string to allow URL sharing and maintain state after refresh. In backend, accept the status parameter in the listing endpoint, validating only allowed values. Don't alter the API response contract beyond supporting the new input parameter.
```

After that, in the `tasks` stage, the decomposition might come out more or less like this:

```text
1. Update orders listing specification with new filter behavior by status
2. Adjust listing endpoint to accept status parameter
3. Validate allowed values in backend
4. Update database query to filter by status
5. Add status selector in admin interface
6. Sync filter with query string
7. Display empty state when no orders match the filter
8. Manually validate the four statuses and clearing the filter
```

Look at the difference: the task continues to be the same, but now it stops being just a loose card on the board and starts to have intention, explicit doubt, technical decision, and implementation path.

It's this kind of thing that makes me look at SDD with real interest within a company. Not because it will kill Scrum, Kanban, or any other practice, but because it helps reduce that hole between "the card arrived" and "someone started coding."

## Where I think Spec Kit really helps

There are three points where I see very clear value.

The first is **coherence**. Since each stage inherits context from the previous one, the agent tends to maintain a more stable line of decision.

The second is **decision trail**. It becomes easier to understand where a choice came from, because it's usually anchored in some previous stage.

The third is **less mess**. Not in the sense that everything will come out perfect, but in the sense that the process leaves less room for pure improvisation.

## Where I think you need to be careful

I also don't think this approach is magic. There are some important caveats.

### 1. It can seem bureaucratic in small projects

If the feature is tiny, this entire flow might seem too heavy. And sometimes it is. Not everything needs to become ceremony.

### 2. Specifying well is difficult

Writing good specification isn't simple. Separating functional intention from technical decision takes practice. At first, it's normal to mix things up.

### 3. The agent can still exaggerate

Even with the whole process, there's still a risk of overengineering. The plan might come more complex than necessary. The implementation might bring things you didn't ask for.

### 4. Implemented doesn't mean solved

If the agent marked a task as complete, that doesn't mean the final experience was good or that all requirements were really delivered.

## What I've learned so far

If I had to summarize my practical reading of SDD with Spec Kit, it would be this: **specification quality became a much more central part of AI development work**.

This doesn't diminish the programmer's role. On the contrary. It demands more maturity.

I need to understand more about product to describe intention.
I need to understand more about architecture to choose technical direction.
I need to understand more about quality to review what was produced.
I need to understand more about scope to not let the tool run off alone.

In the end, using AI this way doesn't transform me into someone less technical. It just changes where rigor appears.

## If you want to start without complicating

If I were to suggest a simple path for you to test this in your next project, I would do it like this:

1. Choose a small but real feature.
2. Define short and objective principles.
3. Describe what you want to build without talking about stack.
4. Clarify gaps before planning.
5. Only then give technical decisions.
6. Review tasks before implementation.
7. Treat implementation as a serious draft, not as final truth.

This flow is already enough for you to feel the difference between asking "just do it" and conducting the agent with method.

## Closing

I'm still learning to use this type of approach in my daily life. I don't think SDD will substitute every and any flow, nor that Spec Kit is the only possible tool for this. But I really think there's something important here.

When I specify better, the agent works better.
When I structure the process, review gets better.
When I leave improvisation, code tends to come out less crooked.

And, for me, that's the point.

It's not about outsourcing development to AI.
It's about creating a process in which I continue to think as an engineer, but using AI to gain arm without letting go of judgment.

## Deep Dive Series

If you want to follow the texts in which I deepen each stage separately, this is the sequence:

- [In Spec-Driven Development, everything starts with principles](/en/2026/04/06/1-no-spec-driven-development-tudo-comeca-pelos-principios/)    
  
- [In Spec-Driven Development, `specify` is where ambiguity starts to die](/en/2026/04/06/2-no-spec-driven-development-specify-e-onde-a-ambiguidade-comeca-a-morrer/)  

- [In Spec-Driven Development, `plan` is where specification turns into execution strategy](/en/2026/04/06/3-no-spec-driven-development-plan-e-onde-a-especificacao-vira-estrategia-de-execucao/)  

- [In Spec-Driven Development, `tasks` is where the plan turns into concrete work units](/en/2026/04/06/4-no-spec-driven-development-tasks-e-onde-o-plano-vira-unidades-concretas-de-trabalho/)  

- [In Spec-Driven Development, `implement` is where everything else turns into code](/en/2026/04/06/5-no-spec-driven-development-implement-e-onde-todo-o-resto-vira-codigo/)  
