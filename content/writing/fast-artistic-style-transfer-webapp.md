---
date: 2016-10-31T21:00:00+01:00
draft: true
title: Fast neural style transfer with Django and TensorFlow
category: machine-learning
tags:
   - image-processing
   - convolutional-neural-networks
   - webapp
   - keras
   - tensorflow
   - django
includes_code: yes
includes_math: yes
---

## Incorporating this model into a webapp

- TODO: Explain the general architecture of the webapp, with a
  figure.

- TODO: Point out that solving the entire optimisation problem is not
  feasible as part of the request-response cycle.

### A faster approach to neural style transfer

- TODO: Introduce the Johnson paper and discuss its core idea:
  Replacing the optimisation problem with an *image transformation*
  CNN, which in turn uses the VGG as before to measure losses. When
  this transformation network is trained on many images given a fixed
  style image, we end up with a fully feed-forward CNN that we can
  apply for style transfer. This gives us a 1000x speed up over Gatys'
  implementation, which makes it suitable for a webapp.

- TODO: Architecture notes, introducing a new residual block.

| Layer                       | Activation Size |
| ----------------------------|---------------- |
| Input                       | 3 × 256 × 256   |
| 32×9×9 conv, stride 1       | 32 × 256 × 256  |
| 64×3×3 conv, stride 2       | ...             |
| 128×3×3 conv, stride 2      |                 |
| Residual block, 128 filters |                 |
| ...                         |                 |


- TODO: A figure showing off the algorithm, and how it differs from
  Gatys.

- TODO: Point to our (Keras) implementation of this paper on
  GitHub. This is one significant contribution of this work.

### Serving a learnt model

- TODO: Explain the theory behind exporting a learnt model from Keras
  (as TensorFlow data structures?) and serving it (with TensorFlow
  serving?)
- TODO: Step through important aspects of the implementation of the
  Django webapp. Key models, using generic views.
- TODO: Point to the project source for the complete webapp.

## Selected references and further reading

1. [Perceptual Real-Time Style
   Transfer][fast-neural-style-johnson-etal] and [supplementary
   material][fast-neural-style-johnson-etal-supp]
2. TensorFlow: [Serving][tensorflow-serving]

[fast-neural-style-johnson-etal]: https://arxiv.org/abs/1603.08155
[fast-neural-style-johnson-etal-supp]: https://cs.stanford.edu/people/jcjohns/papers/fast-style/fast-style-supp.pdf
[tensorflow-serving]: https://tensorflow.github.io/serving/
