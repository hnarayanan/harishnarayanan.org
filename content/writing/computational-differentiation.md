---
date: 2024-01-31T21:00:00+01:00
title: Differentiation by computer
category: computational-maths
tags:
   - symbolic-differentiation
   - numerical-differentiation
   - automatic-differentiation
   - scheme
includes_code: yes
---

[Derivatives][wiki-derivative] are ubiquitous concepts that lie at the
heart of analysing and modelling change. Their systematic rules and
recursive nature make them perfectly matched to the capabilities of
computers. In this article, we'll start from an early calculus
understanding of derivatives and first bring them to the computer in a
naïve way. Then, motivated by real-world challenges and needs, we'll
systematically evolve this implementation to be more sophisticated.
Before you know it, we'll arrive at state-of-the-art techniques that
serve as the backbone of modern AI and scientific computing.

Oh, and we'll be doing all this in [Scheme][scheme].

## Why do derivatives matter?

Derivatives are a measure of how much one quantity changes relative to
another. They show up *everywhere*. In basic geometry, the derivative
of a curve at a point is the slope of the tangent line at that point.
In higher dimensions, the derivative gives us the *curvature of level
sets*. In physics, the derivative of the displacement relative to time
is the instantaneous velocity. Derivatives of potential energy
relative to distance gives you force. In chemistry, rates of chemical
reactions are derivatives of concentration. In economics, the
derivative of supply and demand curves gives us market sensitivity. In
biology, population growth rates are time derivatives of population
size.

I could go on and on, but I won't. Derivatives help us analyse and
model change. And what's more, they serve as the core basis

[scheme]: https://www.scheme.org
[wiki-derivative]: https://en.wikipedia.org/wiki/Derivative
