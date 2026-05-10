---
title: "In Spec-Driven Development, `implement` is where everything else turns into code"
date: '2026-04-06T10:00:00-07:00'
slug: no-spec-driven-development-implement-e-onde-todo-o-resto-vira-codigo
lang: en
translationKey: no-spec-driven-development-implement-e-onde-todo-o-resto-vira-codigo-2026-04-06
tags:
  - ai
  - spec-driven-development
  - implement
  - implementation
  - software-engineering
draft: false
description: "After defining principles, specifying the problem, planning execution, and breaking the work into tasks, comes the time to implement. In this text, I explain why implementing can even be the most straightforward part, but the real work is in reviewing and validating what was delivered."
---

# In Spec-Driven Development, `implement` is where everything else turns into code

In the text [In Spec-Driven Development, Everything Starts with Principles](/en/2026/04/06/1-no-spec-driven-development-tudo-comeca-pelos-principios/), I talked about the `constitution` stage, where I define the principles that will govern the project's decisions.

Then, in [In Spec-Driven Development, `specify` is where ambiguity starts to die](/en/2026/04/06/2-no-spec-driven-development-specify-e-onde-a-ambiguidade-comeca-a-morrer/), I showed the point where demand gains clearer expected behavior.

In sequence, in [In Spec-Driven Development, `plan` is where specification turns into execution strategy](/en/2026/04/06/3-no-spec-driven-development-plan-e-onde-a-especificacao-vira-estrategia-de-execucao/), I entered the stage that organizes the crossing with order, dependency, and sense of risk.

After that, in [In Spec-Driven Development, `tasks` is where the plan turns into concrete work units](/en/2026/04/06/4-no-spec-driven-development-tasks-e-onde-o-plano-vira-unidades-concretas-de-trabalho/), I talked about the break that transforms strategy into executable blocks.

But, at some point, all this needs to turn into code.

That's where `implement` enters.

And here I think an important simplification is worth making: yes, in a certain sense, `implement` is just implementing.

If the previous work was well done, this stage shouldn't carry a great methodological drama. The objective now is to take an already delimited task and transform that into code.

Except that doesn't mean the work is done.

In the AI context, many times the act of implementing became cheap. The agent writes quickly, suggests structure, connects parts, and returns a plausible solution in a short time.

That's why, for me, the main point of `implement` isn't to romanticize code writing.

The main point is another: after the code was generated, someone still needs to review what was delivered.

## Implementing Can Be the Easiest Part

Depending on context, implementation itself almost becomes an operational stage:

> pick up the task  
> generate the code  
> adjust what's necessary  
> move forward

If `constitution`, `specify`, `plan`, and `tasks` did the job right, this is even expected.

The problem starts when the person treats the agent's output as if it were already the final delivery.

Because one thing is to generate code.

Another thing is to verify if that code:

- solved exactly the task
- respected the scope
- didn't invent things outside what was agreed
- didn't distort the specified behavior
- continues coherent with the project's principles

That's where, for me, the real work lives.

## What Really Matters After Implementing

I tend to look at `implement` less as an epic construction moment and more as a transition point.

The code appeared. Now it needs to be confronted with what came before.

In practice, I want to review if the delivery:

- corresponds to the task that was asked for
- remains faithful to the specification
- didn't trample the plan
- didn't bring unnecessary complexity
- can be accepted with reasonable confidence

If I finish this stage only with the feeling that "it seems like it turned out good," it's still little.

## A Practical Example of Difference

Let's go back to the orders example.

Suppose the current task is this:

- implement order creation with automatic total calculation

If I look only at the generation stage, maybe it's enough to ask the agent to do this and receive a block of code back.

But the relevant work starts right after:

- did it only create the flow or did it invent more things?
- is the total being calculated the right way?
- does order without item continue to be blocked?
- was the relationship with existing client respected?
- did the solution stay compatible with the simplicity the project wanted?

Notice the difference.

The act of implementing can even be straightforward.

What can't be automatic is accepting what was implemented.

## In the End

After the delivery is finalized, there's still an important responsibility in your hands: ensuring that everything that was defined as a requirement was really met. It's not enough to look at the code and feel that it seems ready. It's also not enough to trust just because the implementation came out clean, organized, or plausible.

If there are `requirements.md` files involved in that work, it's up to you to check one by one and ensure that all items listed there were, in fact, resolved and marked as complete. This matters because, in the end, what validates the delivery isn't just the existence of code, but the adherence between what was asked for and what was actually delivered.

And there's another point here that I think is important: not everything will be validated automatically. In several cases, manual checking will still exist. Interface flow, behavior in specific scenario, integration that depends on real context, experience detail, or anything else not fully covered by automated tests still needs to be verified by you.

That is: the `implement` stage doesn't exactly end when code appears. It ends when the delivery was reviewed, confronted with requirements, and validated in a minimally responsible way.

But, in the end, the flow doesn't end like someone who closes a rigid process and leaves. It ends and restarts.

If a new demand emerges, the natural path is to return to `specify` and start again from there, with a new clear specification for what needs to be built now. And, if along that path you realize that some principle from `constitution` needs to change, be refined, or even be substituted, that's also part of the process.

I like this structure precisely because it isn't rigid in the bad sense. It's atomic. Each part exists with a clear function, but none of them needs to be treated as a sacred or immutable piece. If the project evolves, the structure can evolve along. If context changes, principles can change along. If the way of executing improves, the flow can also be adjusted.

For me, this is one of the strongest points of this approach: it organizes work without pretending that the project will remain the same forever.

Thanks for reading this far.
