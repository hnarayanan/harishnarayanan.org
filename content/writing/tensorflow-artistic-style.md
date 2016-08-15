---
date: 2016-08-31T21:00:00+01:00
title: Convolutional neural networks for artistic style transfer
category: machine-learning
tags:
   - image-processing
   - neural-networks
   - tensorflow
   - kubernetes
---

We're going to be looking at a branch of machine learning called
convolutional neural networks (or convnets for short). And in order to
motivate and focus our journey through the world of convnets from
theory to practice, we're going to reproduce the code ideas underlying
a really popular app at the moment called Prisma.


TODO: What we're going to do (attempt to reproduce Prisma) and why
it's cool. Mention the corresponding project functioning on GitHub.

## Introducing Prisma and motivating the problem

So what is Prisma? Prisma is an iPhone app (which will likely soon be
ported to other platforms) that allows you transfer the style of one
image, say a renaissance painting, onto the content of another, say a
picture of your baby. Here's a demo of it in action.

(animated gif, for example)

Like many people, I find much of the output of this app very pleasing,
and I got curious as to how it achieves its effect. At the outset you
can start to imagine that it's somehow extracting low-level features
from one image (that we'll call the style image) -- things like the
colour and texture of the brush strokes -- and applying it to more
semantic, higher level features on another image (that we'll call the
content image) -- things like a face.

How would one even begin to do something like this? You can imagine
doing some image analysis on the style image to get things like
average colours or maybe even texture, but how would you apply these
in a non-homogeneous way to the content image? And what about the
existing style of the content image? How do we first subtract that
before we apply the new style?

I was stumped by many of these questions really early on and, as every
one of you would do, turned to Google for help. It turns out there is
a really popular paper that explains exactly how this is done: we'll
call it Gatys et al's neural style paper. So that's where we start our
journey.

## General theory behind Convolutional Neural Networks

The paper essentially describes the use of a class of deep neural
networks called Convolutional Neural Networks (convnets) that are
particularly well suited to processing images. Before we get to the
specifics of the algorithm described in the paper, let’s first learn a
bit about (convolutional) neural networks in general.

- TODO: Historical and from-first-principles mathematical context from
  Stanford CS231n tying back to why convolutions might work.

{{< figure src="/images/writing/tensorflow-artistic-style/neural-network.svg" title="An example neural network image." >}}

## Theory behind particular algorithm we're going to use

- TODO: Summarise the Gatys, et al. paper for the core idea.
- TODO: Summarise the Simonyan, et al. paper for the technicalities of
  image recognition.

## Implementation of the model in TensorFlow

- TODO: Step through the more crucial portions of the implementation
  on GitHub.
- TODO: Talk about how hyperparameters are tuned to improve aesthetic
  quality of the output. Show examples of things that work and things
  that do not.

But we want to make a near real time web service out of this, and so
we look for extensions of this algorithm.

## Make into a web service with TensorFlow Serving and Kubernetes

- TODO: Introduce the Johnson paper.
- TODO: Step through important aspects of the implementation.
- TODO: Optimisation of and shortcuts to the implementation above to
  make it suitable for a user-facing app.
- TODO: Explain the theory behind serving a learnt model.

## Conclusion

- TODO: Repeat what we saw with some examples relating back to first
  motivating examples from Prisma.
- TODO: Talk about ideas for extension and improvement.


## Selected references and further reading

- TODO: Link to 8--10 references and related sample project.

## Appendix

- TODO: Explain how to setup the project (+ serving).
- TODO: Explain how to get TensorFlow working with GPU support on
  macOS.
