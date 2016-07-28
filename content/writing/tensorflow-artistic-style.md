---
date: 2016-07-24T11:50:55+01:00
draft: true
title: Hosted artistic style transfer with TensorFlow
category: machine-learning
tags:
   - image-processing
   - neural-networks
   - tensorflow
   - kubernetes
---

TODO: What we're going to do (attempt to reproduce Prisma) and why
it's cool. Mention the corresponding project functioning on GitHub.

## General theory behind Convolutional Neural Networks

- TODO: Historical and from-first-principles mathematical context from
  Stanford CS231n.

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

## Make into a web service with TensorFlow Serving and Kubernetes

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
