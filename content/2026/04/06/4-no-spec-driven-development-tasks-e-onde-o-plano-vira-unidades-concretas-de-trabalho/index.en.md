---
title: "In Spec-Driven Development, `tasks` is where the plan turns into concrete work units"
date: '2026-04-06T10:00:00-06:00'
slug: no-spec-driven-development-tasks-e-onde-o-plano-vira-unidades-concretas-de-trabalho
lang: en
translationKey: no-spec-driven-development-tasks-e-onde-o-plano-vira-unidades-concretas-de-trabalho-2026-04-06
tags:
  - ai
  - spec-driven-development
  - tasks
  - tarefas
  - software-engineering
draft: false
description: "After defining principles, specifying the problem, and planning execution, comes the time to break the work into concrete parts. In this text, I explain why the `tasks` stage is the one that transforms strategy into executable units."
---

# In Spec-Driven Development, `tasks` is where the plan turns into concrete work units

In the text [In Spec-Driven Development, Everything Starts with Principles](/en/2026/04/06/1-no-spec-driven-development-tudo-comeca-pelos-principios/), I focused on the `constitution` stage, where I define the criteria that will guide the project's decisions.

Then, in [In Spec-Driven Development, `specify` is where ambiguity starts to die](/en/2026/04/06/2-no-spec-driven-development-specify-e-onde-a-ambiguidade-comeca-a-morrer/), I entered the stage where demand stops being vague intention and starts having clearer expected behavior.

In sequence, in [In Spec-Driven Development, `plan` is where specification turns into execution strategy](/en/2026/04/06/3-no-spec-driven-development-plan-e-onde-a-especificacao-vira-estrategia-de-execucao/), I talked about the stage that organizes the work crossing with order, dependency, and sense of risk.

But plan, by itself, still isn't executable work.

Between knowing the strategy and starting to implement, there's still an important question: how do I transform this path into concrete execution blocks without losing coherence?

That's where the `tasks` stage enters.

And, for me, this stage matters a lot because it's in it that planning stops being a good narrative about execution and starts becoming work parts that someone can really pick up, understand, and complete.

## The Error of Thinking Breaking Work Is Just Making a Checklist

When someone hears "tasks," it's common to imagine something very simple:

- create backend
- create frontend
- make tests
- review
- deliver

This even seems like organization, but many times it's still too generic.

A list like this can give a sense of structural progress without solving the main thing: each item continues too broad, too ambiguous, or too mixed to guide execution well.

In practice, poorly broken tasks usually generate some well-known problems:

- blocks too big to validate early
- parts with confusing responsibility
- items that mix several decisions at the same time
- hidden dependencies
- false sense that work is well distributed

When this happens, execution starts to slip back into improvisation. The difference is that now improvisation comes packaged as a checklist.

## What the `tasks` Stage Solves

I don't see `tasks` as the obligation to produce a huge list to seem methodical. Nor do I see it as simple conversion of plan into subtitles.

For me, `tasks` solves one very concrete thing: transform execution strategy into clear, limited, and verifiable work units.

It's the moment when I try to decide:

- which piece of work deserves to become its own task
- what does each task need to deliver
- where does one task end and the next begin
- what dependencies need to be explicit
- what criterion makes a task be considered complete

If `plan` organizes the crossing, `tasks` defines the steps.

And this matters a lot because, without this translation, implementation continues too big, too diffuse, or too dependent on local interpretation.

## `Tasks` Isn't Fragmenting for the Sake of Fragmenting

There's a curious risk here.

When the person realizes they need to better break the work, they can exaggerate to the other side and turn everything into microtasks:

- create model
- create migration
- create service
- create controller
- create route
- create unit test
- create integration test

This can work in some contexts, but many times produces an artificially excessive break.

Because a good task isn't just a small task. A good task is a task with sense.

If I separate work using only technical or mechanical cuts, I run the risk of losing the bond with the behavior I wanted to deliver. And, when that happens, I start optimizing implementation pieces instead of real units of result.

For me, the question isn't just "how to divide?". The question is "how to divide without destroying delivery coherence?".

## What I Try to Capture in a Good `tasks` Stage

I don't follow rigid template, but normally I want to leave this stage with some things very clear.

Something along these lines:

- each task needs to have an understandable objective
- each task should produce an observable result
- the boundary between tasks can't be confusing
- dependencies need to be explicit
- the size of each block should allow reasonable validation
- sequence should continue respecting the plan

If I look at a task list and still feel that "anything can mean anything," then this stage hasn't closed right yet.

## The Questions I Usually Use in `tasks`

If in `constitution` I used the `5 Qs`, in `specify` another set of questions and in `plan` questions of order and risk, here I usually force operational clarity.

Normally I want to answer something like:

- `Q1.` What work unit produces a real result?
- `Q2.` Where does one task end and the next begin?
- `Q3.` What dependencies need to be explicit?
- `Q4.` What can I validate when completing each task?
- `Q5.` Does this break help execution or just seem organized?

### `Q1.` What work unit produces a real result?

This question exists to prevent ornamental tasks.

A good task, for me, needs to point to some result that makes sense by itself. Not necessarily a final result for the user, but at least something with clear function within the delivery.

Examples:

- structure the minimum order flow with mandatory client relationship
- validate automatic total calculation in backend
- allow operator to view already registered orders

Notice the difference.

These items may still involve several internal changes, but remain connected to an understandable result. This is much better than a list of technical pieces without context.

### `Q2.` Where does one task end and the next begin?

This question helps me avoid overlap.

When the boundary between tasks is bad, several things start to happen:

- two tasks mess with the same central problem
- completion criteria become vague
- a task seems "almost ready" for too long
- review gets confused because no one knows what that block should have solved

I like to try to make the separation more honest. If one task depends on another to make sense, this needs to be clear. If two tasks are solving the same nucleus, perhaps the break is wrong.

In other words: a good task has contour.

### `Q3.` What dependencies need to be explicit?

Not every task is born isolated.

Some need previous decision, minimum base ready, or completed validation to make sense. When this stays too implicit, execution tends to open fronts too early.

So I try to make visible:

- which tasks unlock others
- what can walk in parallel without high conflict
- which items depend on model or rule already stabilized
- where there's still too sensitive a point to separate early

This is especially important when work involves AI, because opening multiple parallel executions without clear dependency is an efficient way to produce collision with the appearance of productivity.

### `Q4.` What can I validate when completing each task?

This question brings `tasks` very close to healthy execution.

For me, a task gets much better when there's some clear way to verify if it fulfilled what it promised. This doesn't mean that every task needs to have a formal battery of tests at the same instant, but it means that it needs to touch some observable criterion.

Something like:

- order can be created with client and valid item
- total is calculated correctly
- system blocks finalization without item
- listing shows recently created orders

When the task doesn't offer any clear verification point, usually it's too broad or poorly defined.

### `Q5.` Does this break help execution or just seem organized?

This is the question I like the most because it dismantles a lot of false sophistication.

There are task lists that look beautiful on paper but hinder more than help. Sometimes because they created too many blocks. Sometimes because they turned each technical layer into its own item. Sometimes because they separated things that should walk together.

So I try to be pragmatic.

If the break:

- improves execution clarity
- facilitates validation
- reduces rework
- preserves coherence with the plan

then it's helping.

If it just increases the feeling of control without improving the real work crossing, it's probably overdoing it.

## A Practical Example of Difference

Suppose the same orders demand I've been using in the other texts:

- internal operators need to manually register orders
- each order must be associated with an existing client
- order items need to inform quantity and price
- the system should calculate total automatically
- orders cannot be finalized without at least one item
- in this first version there will be no online payment nor tax issuance

After specifying and planning, I still need to transform this into executable work.

A weak break could be:

- make orders backend
- make orders frontend
- create tests

This is little useful. Each item continues too big.

Now look at a better break:

- define and validate the minimum order structure with mandatory link to client
- implement order creation with automatic total calculation
- block order finalization without valid item
- make listing and basic query of orders available to operators
- cover critical flows and adjust error messages

Here there's already much more ground.

Not because the list got longer, but because each item points to a more concrete delivery unit.

## In the End

If I had to summarize the function of `tasks` in one sentence, I would say this: it's the stage where the plan stops being just intelligent sequence and starts becoming graspable work.

For me, this matters because good execution doesn't just depend on knowing where to go. It also depends on knowing which piece makes sense to attack now, with clear boundary and minimally honest completion criterion.

When this break is well done, implementation gains rhythm without losing coherence.

In the next text, I want to enter the `implement` stage, which is when this whole chain finally turns into code.
