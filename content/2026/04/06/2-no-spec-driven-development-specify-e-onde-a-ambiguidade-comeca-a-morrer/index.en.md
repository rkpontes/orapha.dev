---
title: "In Spec-Driven Development, `specify` is where ambiguity starts to die"
date: '2026-04-06T10:00:00-04:00'
slug: no-spec-driven-development-specify-e-onde-a-ambiguidade-comeca-a-morrer
lang: en
translationKey: no-spec-driven-development-specify-e-onde-a-ambiguidade-comeca-a-morrer-2026-04-06
tags:
  - ai
  - spec-driven-development
  - specify
  - specification
  - software-engineering
draft: false
description: "After principles comes the time to say clearly what needs to be built. In this text, I explain why the `specify` stage is the one that transforms vague intention into executable work."
---

# In Spec-Driven Development, `specify` is where ambiguity starts to die

In the text [In Spec-Driven Development, Everything Starts with Principles](/en/2026/04/06/1-no-spec-driven-development-tudo-comeca-pelos-principios/), I focused on the `constitution` stage, where I define the criteria that will guide the project.

But principles alone don't deliver system.

After saying how the project should think, comes the time to say what it needs to build.

That's where the `specify` stage enters.

And, for me, this is one of the most important parts of the entire flow. Because, in practice, it's here that the work of a new demand begins.

Before planning, breaking into tasks, or implementing, I need to specify what that demand really asks for.

It's precisely at this point that we start exchanging generic desire for operational expectation.

## The Problem of Asking for Solution Too Early

When someone works with a code agent frequently, there's a very strong temptation to skip directly to implementation.

The conversation usually starts like this:

> create a CRUD for clients  
> add login  
> make a dashboard  
> integrate with payment  
> add notification

Again: this isn't necessarily useless. In some cases, it can even produce good things.

The problem is that this way of asking mixes intention, solution, and expectation in one big ball.

I say "make a dashboard," but I don't make clear:

- who this dashboard is for
- what problem it solves
- what needs to appear there
- what's mandatory in this first version
- what's explicitly out of scope
- how I'll know if that turned out right

When this isn't clear, the agent does what it was trained to do: complete the gap with a plausible solution.

Except plausible isn't the same as correct.

## What the `specify` Stage Solves

I don't see `specify` as "writing a pretty requirement." Nor do I see it as the moment to assemble heavy documentation just because the process asks for an artifact.

For me, `specify` serves for one very concrete thing: reduce ambiguity enough so that execution doesn't have to guess the problem.

It's the moment when I try to make explicit:

- what problem needs to be solved
- who is affected by this problem
- what behavior the system should have
- what restrictions matter
- what goes in and what stays out
- what criteria define if the delivery is acceptable

That is, I stop talking about "idea" and start talking about expected behavior.

This changes everything.

Because, when specification is well done, the agent stops inventing context. It starts working on more delimited terrain. Interpretation continues to exist, of course. But now interpretation happens within more controlled margins.

## `Specify` Isn't Detailing Implementation

This point matters a lot.

A bad specification isn't just one that's too vague. It can also be one that descends too early to the solution level.

Example of bad request:

- create endpoint `POST /users/register`
- use Redis for session
- create table X with columns Y and Z
- implement service `UserOnboardingService`

Notice that this is almost at implementation level.

Sometimes this is inevitable, especially when there's already very clear technical restriction. But, in many cases, I still don't want to answer "how." I want to first nail down "what" needs to happen.

Something like:

- a new user needs to be able to create their account
- the system should validate mandatory data
- duplicate emails cannot be accepted
- after successful registration, the user should be able to access the authenticated area

Now yes I have behavior.

And behavior is a much better starting point than premature technical structure.

## What I Try to Capture in a Good Specification

I don't follow a rigid template in every situation, but I almost always try to answer a similar set of questions.

I don't think of this as an official framework. I think more like a filter to know if the request is clear enough to turn into real work.

Normally I want to leave the `specify` stage knowing these things:

- what is the problem
- who is it for
- what expected result matters
- what is the scope of the first delivery
- what restrictions or rules cannot be ignored
- how to validate if the delivery met the objective

If I can't answer this with some objectivity, the request is still raw.

## The Questions I Usually Use in `specify`

If in `constitution` I talked about the `5 Qs`, here I tend to use another set of simple questions to force clarity.

Something along these lines:

- `Q1.` What real problem does this delivery solve?
- `Q2.` Who is this behavior for?
- `Q3.` What does the system need to do, exactly?
- `Q4.` What stays out of this specification?
- `Q5.` How do I recognize that this is done?

### `Q1.` What real problem does this delivery solve?

This question exists to prevent ornamental features.

Many demands arrive with the face of solution, but without explaining the pain being attacked. When this happens, the risk is building something functional and still irrelevant.

If I can't describe the problem with clarity, I usually still don't have specification. I have just impulse.

A useful answer here usually looks something like:

- today the team loses time consolidating data manually
- the user cannot complete an important step without operational support
- there is rework because certain information is scattered

This type of formulation already takes the conversation out of "would be nice to have" territory and puts it in "needs to solve this here" territory.

### `Q2.` Who is this behavior for?

This question helps prevent too-generic specification.

When I just say "the user," I'm usually hiding important detail. Internal user, end customer, operator, administrator, finance, support: each of these roles changes what makes sense to build.

Defining this early helps because several decisions depend on who is on the other side:

- acceptable level of complexity in the interface
- volume of information displayed
- tolerance for manual steps
- need for audit
- type of error that needs to be treated

Sometimes the same functionality seems obvious until the moment you ask "for whom?".

## `Q3.` What exactly does the system need to do?

Here I try to get out of generic language and describe observable behavior.

It's not enough to say "have client management." That's still too nebulous. I prefer to break down into more concrete actions and responses, for example:

- allow registering client with defined mandatory fields
- list clients with search by name or document
- prevent duplication by main identifier
- allow editing data without erasing relevant history

This type of writing helps because it's already born closer to validation.

If I can imagine someone testing that sentence, it's a good sign.

If I read the sentence and still don't know what would be considered correct behavior, the specification is still loose.

### `Q4.` What stays out of this specification?

This point is very underestimated.

Scope isn't just what goes in. Scope is also what I decide not to solve now.

When I don't make this explicit, the agent tends to complete the package. And, in its head, completing the package can mean:

- create advanced permissions
- add pagination, filters, and export
- prepare multitenancy
- structure internationalization
- leave everything ready for mobile

None of this is absurd in itself. The problem is when these expansions appear because no one said "this isn't part of this delivery."

So I like to write scope exclusions without any shame:

- at this stage there will be no fine permission control
- analytical reports stay for a next phase
- offline support won't be treated
- batch import is out of the first version

Saying "no" is part of specifying well.

### `Q5.` How do I recognize that this is done?

For me, this is the question that most approximates specification to executable work.

If I don't know which criteria close the delivery, I open space for two bad things: infinite implementation or false sense of completion.

I like to think of this in terms of acceptance criteria. Not necessarily in an ultra-formal format, but in a way that allows verifying the result without depending too much on subjective interpretation.

Examples:

- given an already registered email, the system should reject new creation with appropriate message
- after saving a valid record, it should appear in the listing
- only authenticated users can access a certain area
- external error should be displayed without breaking the entire flow

When I have this level of clarity, the next stage becomes much safer.

## Good Specification Doesn't Need to Be Huge

It's worth saying this because, when someone hears "specify," they might imagine a huge document, full of formal sections and corporate text.

That's not what I'm defending.

A specification can be lean and still be very good, as long as it answers the essential with clarity.

What I try to avoid isn't lack of volume. It's lack of precision.

Between a short and clear text versus a long and nebulous text, I prefer a thousand times the short and clear one.

## A Practical Example of Difference

Generic request:

> create orders module

This opens too much space.

Now look at a more specified version:

- internal operators need to manually register orders
- each order must be associated with an existing client
- order items need to inform quantity and price
- the system should calculate total automatically
- orders cannot be finalized without at least one item
- in this first version there will be no online payment nor tax issuance
- the delivery is ready when it's possible to create, view, and query valid orders without manual calculation

I still haven't described architecture. I still haven't talked about database, framework, queue, service, or class naming.

But now there's enough ground to plan, implement, and review.

## In the End

If I had to summarize the function of `specify` in one sentence, I would say this: it's the stage where intention stops being vague enough to become conversation and becomes clear enough to become work.

For me, this is the point where ambiguity really starts to lose space.

Because, in the end, specifying well isn't producing bureaucracy. It's making the problem understandable enough so that implementation, review, and validation work on the same reality.

In the next deep dive, the natural path is to enter the stage that takes this specification and transforms it into an execution plan.
