---
title: "In Spec-Driven Development, Everything Starts with Principles"
date: '2026-04-06T10:00:00-03:00'
slug: no-spec-driven-development-tudo-comeca-pelos-principios
lang: en
translationKey: no-spec-driven-development-tudo-comeca-pelos-principios-2026-04-06
tags:
  - ai
  - spec-driven-development
  - constitution
  - software-engineering
  - principles
draft: false
description: "Before thinking about feature, I prefer to define the principles that will command the project. In this text, I dissect the constitution stage in SDD and the 5 Qs I use to give direction to work with AI."
---

# In Spec-Driven Development, Everything Starts with Principles

In the article [How I've Been Using Spec-Driven Development with Spec Kit in My Projects](/en/2026/04/03/como-eu-tenho-usado-spec-driven-development-com-o-spec-kit-nos-meus-projetos/), I went through the flow stages in a more general way.

But I thought it was worth going back calmly to each of them, in separate texts, because there's stuff there that deserves to be properly dissected.

If the idea is to gradually deepen this flow, it makes sense to open precisely at the stage where I define the project principles.

I'm talking about `constitution`.

And I want to focus here less on the tool itself and more on the logic behind the thing. Because, honestly, the name can change, the command can change, the stack can change, but the need remains the same: before asking the agent for features, someone needs to say what the rules are that will govern that project's decisions.

For me, this is one of the most underestimated points when we talk about development with AI.

## The Error of Starting with the Feature

The most natural path, especially when the person is already used to using a code agent, is to start like this:

> create a registration screen  
> make an API for such thing  
> add authentication  
> now create tests  
> now refactor  
> now improve architecture

Notice the pattern: the conversation always starts with the visible delivery.

It's not that this is always wrong. In small projects, quick experiments, or proof of concept, it can even go in this line and accept controlled chaos. The problem is when this logic becomes a work method.

When I start directly with the feature, without declaring the project principles first, I leave an important part of the decision in the hands of improvisation. And the agent is very good at completing gaps. Good even too much. If I don't say clearly what I value, it will fill the void with generic pattern, plausible assumption, and excess of good will.

That's when things start to go sideways.

The agent creates too much abstraction in a simple project. Or makes everything too coupled in a project that needed to last. Or shoves tests where it wasn't a priority. Or ignores tests where it was mandatory. Or invents a "beautiful" architecture that no one asked for. Or makes naming, organization, and structure decisions without any alignment with what I really wanted to preserve.

In the end, the feeling is productivity. But many times it's just speed without direction.

## What `constitution` Really Solves

When I talk about `constitution`, I'm not thinking about a bureaucratic document. It's not to become a team's beautiful manifesto that no one reads later. Nor is it to write an abstract treatise about good practices.

The function of this stage is much more practical: declare the principles that will guide the next decisions.

In other words, it's the moment when I say:

- what this project values
- what this project avoids
- which criteria weigh more when there's trade-off
- how quality will be interpreted here
- what type of complexity is acceptable and which is already excess

And this isn't restricted to code style or architecture. Depending on context, I can also use `constitution` to register project operational rules, such as branch flow, test policy, and minimum security requirements. If these things change how the delivery should be built and reviewed, it makes sense for them to appear right here.

This changes the whole conversation.

Because, from there, AI stops responding only to the immediate request and starts operating within a field of more explicit restrictions and preferences. And, for me, working with AI without clear restriction is asking to receive a technically possible solution, but conceptually misaligned.

## Principle Isn't Loose Rule

There's an important difference here.

Many people, when they think about principles, write very generic things:

- use clean code
- maintain quality
- follow good practices
- make scalable code

This looks nice, but helps little.

These phrases even point in a direction, but still leave too much room for interpretation. And, when there's too much room for interpretation, the agent fills with what it knows as average pattern. The problem is that average pattern isn't context.

For me, a good principle is one that influences real decision.

For example, instead of just saying "maintain simplicity," I prefer something more concrete, like:

- prioritize direct solution before reusable abstraction
- avoid extra layers while the domain is still small
- only introduce more sophisticated pattern when there's concrete pain

Now yes there's an orientation that impacts what will be built.

Similarly, instead of just saying "ensure quality," I can say:

- every delivery must preserve readability
- names need to communicate business intention
- changes shouldn't break existing behavior without explicit reason
- automated tests are mandatory only in critical parts

This already changes the expected behavior quite a bit.

## `Constitution` Exists to Hold the Project's Axis

The more I use an agent, the more I realize that the biggest risk isn't it getting syntax wrong. That usually is the least of problems.

The bigger risk is it getting the code right and the direction wrong.

This distinction matters a lot.

A system can compile, pass the build, run locally, and still be technically misaligned with what the project needed to be. It can be too complicated, too fragile, too coupled, too generic, or simply outside the spirit of the base.

That's why I see `constitution` as a criteria alignment stage even. It's in it that I establish how the project thinks.

It might seem like a pompous way of saying this, but that's exactly the point: before deciding what to do, I need to define how decisions will be made.

Without this, each feature becomes a new improvised negotiation.

## What I Usually Define in This Stage

I don't follow a rigid formula, but I normally try to answer what, in my head, became a kind of `5 Qs` of `constitution`.

It's not a formal framework nor a patented method. It's just a simple way to not leave this stage too vague.

For me, this is a good way to get out of generic principle and arrive at something that really guides decision.

The `5 Qs` I usually answer are these:

- `Q1.` What type of solution should this project privilege now?
- `Q2.` What does this code need to look like to remain readable?
- `Q3.` What technical limits cannot be negotiated?
- `Q4.` What level of testing makes sense at this stage?
- `Q5.` How much architecture does this project really need at this moment?

### `Q1.` What type of solution should this project privilege now?

This question exists to define the degree of acceptable sophistication.

Every project lives this tension. If I simplify too much, maybe the next change hurts. If I prepare too much for the future, I run the risk of assembling a heavy structure for a small problem. So I like to say explicitly which side the project should lean.

In practice, answering this is saying things like:

- prioritize direct solution before reusable abstractions
- prepare growth only when there's concrete signal of that need
- avoid extra layers while the domain is still small

In general, I tend to favor simplicity with conscious growth. That is: make it simple now, but not any which way.

### `Q2.` What does this code need to look like to remain readable?

Not all clarity is just a matter of beautiful code. Many times, clarity has more to do with communication than with style.

In this part, I try to say how the code needs to present itself. If names should reflect domain, if organization should be direct, if reading should be more important than any clever trick, all of this fits here.

A practical way to answer is writing things like:

- names should communicate business intention
- structure should be easy to understand by someone else on the team
- readability weighs more than technical cleverness

This is important because AI can generate a lot of things quickly, but not always with the best sense of communication. Sometimes the solution even works, but the code text becomes generic, without domain vocabulary, without the face of a well-thought-out system.

### `Q3.` What technical limits cannot be negotiated?

This is the question that defines limits.

Every constitution needs to make clear what the project doesn't accept, even when that seems faster in the short term. It's here that I usually register the type of shortcut that isn't worth it, the complexity that I don't want to buy, and the type of decision that needs justification before entering.

Example answers:

- don't introduce dependency without strong necessity
- don't increase complexity just to seem scalable
- don't break compatibility without justifying
- don't sacrifice understanding in the name of technical cleverness

It's also here that I can leave very practical locks, for example:

- the project should follow a `gitflow` flow or another branch strategy defined by the team
- every change in critical flow needs to come accompanied by the type of test agreed for this project
- minimum security requirements, such as mandatory authentication, access control, secret protection, and care with dependencies, cannot be treated as optional detail

This type of principle helps a lot because it reduces the chance of the agent confusing sophistication with quality.

### `Q4.` What level of testing makes sense at this stage?

This point varies a lot from project to project. And precisely because it varies so much, it's worth being in the constitution.

There's a project where I want serious coverage from the beginning. There's a project where I accept not having automated tests in the first version to gain speed. There's context where integration is more important than unit tests. There's context where the domain demands much more rigor.

So I try to answer very objectively:

- are automated tests mandatory or not?
- if they are, where are they indispensable?
- at this stage, are unit tests, integration, or well-guided manual validation worth more?

The important thing is not to leave this implied. If tests are mandatory, say. If tests are selective, say. If at this stage it doesn't make sense to invest in this, say that too. What I try to avoid is leaving AI to guess the project's quality policy.

For me, this same logic applies to security. If the project needs to follow minimum cybersecurity requirements from the first delivery, this should be said in `constitution` with the same objectivity. Authorization, audit, secret handling, sensitive data protection, and basic hardening criteria shouldn't appear only at the end as tardy correction.

### `Q5.` How much architecture does this project really need at this moment?

This question helps me contain the temptation to turn any project into an architecture showcase.

Not every project needs complete DDD, event-driven architecture, queues, messaging, plugin system, extreme modularization, and fifteen interfaces to abstract half a dozen simple rules.

When I answer this question, I normally do it by delimiting what is acceptable now and what would be premature at this moment.

Example:

- maintain lean architecture at this stage
- avoid advanced patterns without concrete necessity
- prefer simple organization until domain complexity justifies something bigger

When I realize the project needs to remain light, I write this directly. Without ceremony. Because, if I don't write, there's a good chance of conference architecture appearing for a corner problem.

## An Example of Reasoning

Suppose a small, internal project, with a short deadline, to solve a very specific operational problem.

If I don't say anything about principles, the agent can:

- create excessive separations
- prepare the system for a scale that perhaps will never come
- suggest many libraries
- invest in generic abstractions too early

Now imagine that I define something more or less like this:

- prioritize simplicity and maintenance speed
- avoid unnecessary dependencies
- prefer direct structure while the domain is small
- ensure clarity of names and flow
- automated tests only in the most critical rules
- follow the branch flow defined by the team, without skipping review
- treat authentication, authorization, and secrets as mandatory requirements from the beginning

Notice how this already changes the terrain.

I'm not defining the feature. I'm not saying if it will be API, screen, database, or framework. I'm defining the way of thinking about that project. And this, later on, affects naming, folder organization, number of layers, validation strategy, refactoring criteria, and even the type of suggestion that AI will consider acceptable.

## This Is Also Software Engineering

There are people who look at this stage and think this is just "improved prompt." I think it's a weak reading.

For me, this is software engineering applied to a new execution context.

At its core, we're talking about the same responsibility as always:

- define criteria before building
- reduce ambiguity
- make trade-offs explicit
- protect system quality

The difference is that now this needs to be said in a way that an agent can use throughout the flow.

That is: it's not enough to have good sense in your head. You need to transform that good sense into operational instruction.

## In the End

If I had to summarize the importance of `constitution` in one sentence, I would say this: it exists to prevent execution from starting without criteria.

In SDD, this matters because the idea isn't just to produce artifact. It's to produce with intention.

And intention, when not declared, becomes assumption.

That's why I like this stage so much. Before discussing screen, endpoint, database, stack, or task, I can define what will really command decisions.

For me, this is the moment when the project stops being just a request and starts to become a system with technical identity.

In the next deep dive, the natural path is to enter the `specify` stage, which is when the conversation leaves principles and enters what really needs to be built.
