---
title: "In Spec-Driven Development, `plan` is where specification turns into execution strategy"
date: '2026-04-06T10:00:00-05:00'
slug: no-spec-driven-development-plan-e-onde-a-especificacao-vira-estrategia-de-execucao
lang: en
translationKey: no-spec-driven-development-plan-e-onde-a-especificacao-vira-estrategia-de-execucao-2026-04-06
tags:
  - ai
  - spec-driven-development
  - plan
  - planning
  - software-engineering
draft: false
description: "After defining principles and specifying the problem, comes the time to plan execution. In this text, I explain why the `plan` stage is the one that transforms clear specification into a viable implementation path."
---

# In Spec-Driven Development, `plan` is where specification turns into execution strategy

In the text [In Spec-Driven Development, Everything Starts with Principles](/en/2026/04/06/1-no-spec-driven-development-tudo-comeca-pelos-principios/), I talked about the `constitution` stage, where I define the criteria that will guide the project.

Then, in [In Spec-Driven Development, `specify` is where ambiguity starts to die](/en/2026/04/06/2-no-spec-driven-development-specify-e-onde-a-ambiguidade-comeca-a-morrer/), I entered the stage where demand stops being vague intention and starts having clearer expected behavior.

But an important bridge is still missing between understanding the problem and going out implementing.

This bridge is the `plan` stage.

And, for me, it exists to answer a simple question: given that now I know what needs to be done, what is the best way to cross this work without turning execution into an expensive improvisation?

Because one thing is to have a good specification. Another thing is to know how to execute that specification with order, criteria, and sense of dependency.

That's where many demands start to get lost.

## The Error of Thinking Good Specification Is Already Enough

When specification is clear, it gives a somewhat deceptive feeling that the work is already practically solved.

The reasoning usually goes like this:

> now that everything is clear, it's just implementing  
> AI already understood what needs to be done  
> let's go breaking into prompt and deliver quickly

In very small projects, sometimes this even works. But, as demand grows a little, this leap starts to charge a price.

Because understanding what needs to be built doesn't automatically solve:

- where to start
- what depends on what
- what can be done in parallel
- which part concentrates more risk
- where it's worth validating early
- how to avoid rework between stages

Without this reasoning, implementation turns into a sequence of locally plausible actions, but globally disorganized.

In the short term, it seems like speed.

In the medium term, refactoring, decision collisions, crooked scope, and that famous sensation that the work walked a lot and consolidated little appear.

## What the `plan` Stage Solves

I don't see `plan` as a pompous schedule. Nor do I see it as the obligation to assemble a document full of little boxes just to seem like process.

For me, `plan` solves one very practical thing: transform specification into execution strategy.

It's the moment when I try to organize:

- the order of work
- dependencies between parts
- blocks that make sense to separate
- risks that deserve attention early
- sequence that reduces rework
- validation points along the way

In other words, if `specify` answers "what needs to happen," `plan` starts to answer "how do I organize the crossing of this work."

This doesn't mean descending to code yet. It means giving operational shape to the path.

## `Plan` Isn't Distributing Tasks on Impulse

There's a common error here.

Many people understand planning as simply breaking the demand into several smaller items:

- make backend
- make frontend
- create database
- add tests
- review

This is better than nothing, but can still be too superficial.

Because planning isn't just fragmenting. It's organizing with intention.

A good work break needs to consider dependency, risk, and logical sequence. Otherwise I just trade a big block for several confusing little blocks.

For example, if there's a structural decision that impacts API, interface, and persistence, maybe the first step isn't "make screen." Maybe it's validating the main flow, the data model, or the central rule first. If I ignore this, I spread implementation before locking the solution's axis.

Good planning, for me, isn't the longest list. It's the most defensible order.

## What I Try to Capture in a Good `plan` Stage

I don't follow a rigid template, but normally I want to leave this stage with some things relatively clear.

Something along these lines:

- what is the safest execution path
- which parts unlock the others
- which blocks can be treated separately
- where is the biggest technical or understanding risk
- at what point is it worth validating before continuing
- how to avoid redundant work or bad sequence

If I still can't see this, the demand may even be well specified, but still not well planned.

## The Questions I Usually Use in `plan`

If in `constitution` I talked about the `5 Qs`, and in `specify` I used another set to reduce ambiguity, in `plan` I tend to ask questions that force order and strategy.

Normally I want to answer something like:

- `Q1.` What is the smallest viable sequence to put this delivery on its feet?
- `Q2.` What depends on what?
- `Q3.` Where is the biggest risk or uncertainty?
- `Q4.` What needs to be validated before expanding?
- `Q5.` How to break this without losing coherence?

### `Q1.` What is the smallest viable sequence to put this delivery on its feet?

This question helps me not start with the most visible place, but with the most useful one.

Not always the first step is the most visible. Sometimes the work needs to start with a minimum base that allows the rest to exist with less friction.

When I answer this, I try to think something like:

- what is the main flow that needs to exist first
- what minimum foundation sustains the next stages
- what do I need to have standing to stop speculating and start consolidating

This helps a lot to avoid ornamental planning, in which several parallel pieces advance without the problem's nucleus really being resolved.

### `Q2.` What depends on what?

This is the question that prevents the plan from becoming wishful thinking.

There are demands where almost everything seems to be able to happen in parallel, until the moment when one decision changes and drags half the work along.

I like to make explicit:

- which parts are prerequisites for others
- which decisions need to be made early
- what can advance in parallel without high risk of collision
- where there is enough coupling to demand sequence

This is especially important when execution involves AI, because it's very easy to open several fronts at the same time and only later realize that they were sharing different assumptions.

### `Q3.` Where is the biggest risk or uncertainty?

Planning is also deciding where I don't want to discover a problem too late.

Every demand has some more sensitive point:

- business rule still somewhat nebulous
- more unstable external integration
- modeling decision that affects the rest
- technical restriction that can block implementation

If I identify this early, I can pull this risk closer to the beginning. Not necessarily to completely resolve it right away, but at least to validate it before the rest of the plan is built on top of a weak assumption.

For me, this is one of the biggest gains of `plan`: it reduces the chance of a beautiful sequence on top of a wrong premise.

### `Q4.` What needs to be validated before expanding?

Not everything needs to be implemented to the end before learning something useful.

Sometimes I just need to validate:

- if the central flow closes
- if the main rule sustains itself
- if integration responds as expected
- if initial modeling isn't crooked

This question helps me insert validation milestones within the plan, instead of pushing all learning to the end.

This is especially valuable in work with agents, because production speed can mask a structural problem for several consecutive interactions. When I create validation points, I better control this risk.

### `Q5.` How to break this without losing coherence?

Breaking work is necessary. Breaking it poorly is very dangerous.

If I separate too much, I create fragmentation and overhead. If I separate too little, I return to the big and difficult-to-control block.

So I try to look for a decomposition that preserves sense. Something in which each block has a clear responsibility, a reasonable completion criterion, and an understandable relationship with the greater objective.

In practice, this usually means:

- break by flow or capability, not by arbitrary layer
- avoid dividing too early something that still depends on central decision
- separate what can be validated in isolation
- keep each part connected to an observable result

When this is well done, the next stage gains a lot. Because execution starts walking on more stable tracks.

## A Practical Example of Difference

Clear specification:

- internal operators need to manually register orders
- each order must be associated with an existing client
- order items need to inform quantity and price
- the system should calculate total automatically
- orders cannot be finalized without at least one item
- in this first version there will be no online payment nor tax issuance

Up to here, I know what needs to be built.

But this still isn't a plan.

A weak break could be:

- make orders screen
- create orders endpoint
- save to database
- add tests

This seems organized, but is still a generic list.

Now look at a more planned version:

- validate minimum order model and mandatory relationship with client
- implement order creation with automatic total calculation
- prevent order finalization without valid item
- only then build listing and visualization for operators
- finally, cover critical flows and adjust error messages

Notice the difference.

In the second version, I'm not just dividing work. I'm choosing an order that respects dependency, reduces rework, and prioritizes the rule's nucleus before the layers around it.

## Planning Isn't Bureaucratizing

It's worth saying this because many people turn up their nose when they hear the word "planning."

I also don't have patience for process that exists just to generate document.

But the `plan` stage I'm defending here is another thing. It doesn't serve to rigidify work. It serves to increase the chance of clean execution.

Before AI, much of development energy was consumed by coding itself. There was much more operational hours going to write, adjust, refactor, connect parts, and carry implementation on the back.

With AI, that coding time dropped drastically.

And, if that time dropped, it shouldn't be automatically reinvested in producing even more code on impulse.

For me, a relevant part of that time needs to be reallocated to planning.

Not in the sense of transforming developer into PM or PO.

It's not about substituting who defines priority, business context, product objective, or demand direction.

It's about something else: once the demand has already arrived, someone still needs to think about what is the best way to execute it.

Someone still needs to understand:

- what is the best order
- where it's not worth improvising
- what needs to be validated early
- how to divide the work without losing the thread

Before, a lot of inefficiency was hidden inside manual implementation effort. Now that implementing became cheaper, the weight of poorly thought-out execution became more visible.

If I receive a good demand and still go out coding without a plan, the chance isn't just to err. It's to err quickly, on several fronts, with a false sense of productivity.

So, for me, planning well became an even more important skill in the AI context.

Not because the process became more bureaucratic.

But because coding stopped being the main bottleneck. And, when that happens, thinking better about execution starts to have much higher return.

## Closing

If `constitution` defines principles, and `specify` reduces ambiguity about what needs to be built, then `plan` is the stage that transforms that clarity into coordinated movement.

It's where I stop looking only at the demand and start looking at the crossing.

Because execution isn't just doing. Execution is also choosing the right order to do.

And, in the end, much bad implementation isn't born from bad specification. It's born from bad sequence.

In the next text, I want to enter the `tasks` stage, which is when this plan starts to turn into concrete work units.
