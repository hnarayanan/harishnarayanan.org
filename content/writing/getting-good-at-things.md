---
date: 2023-01-02T12:00:00+01:00
draft: true
title: How to get good at things
category: learning-advice
tags:
   - imposter-syndrome
   - creative-process
   - failure
includes_video: yes
---

I often run into people (especially those early in their learning
journeys) who suffer from massive imposter syndrome and feelings of
being mediocre. I find myself giving the same versions of the
following advice, so I thought I’d take the time to write it down with
a bit more coherency in one place.

There is no great shortcut to getting good at something. You need to
work hard at it, make a ton of mistakes, and learn from those
mistakes. That's it, this is the entire playbook.

But this playbook is really hard to follow for one very specific
reason. And this is that your ability to critique things is vastly
better than your ability to create things. It’s easy to gauge your
early work as mediocre, get dejected and quit. Ira Glass expresses
this beautifully in the following video.

{{< video src="1u1PSj8FEls" width="720" height="540" title="Time-dependent phase separation into Li-rich and Li-poor phases." >}}

The way around this conundrum is to truly internalise a couple of
facts.

The first of these is that you are not especially mediocre (even
though it can often feel this way when you compare yourself to
others). Most people are pretty mediocre at most things and literally
everything you see around you was made up by someone no smarter or
capable than you. You can create and improve upon anything.

{{< video src="1u1PSj8FEls" width="720" height="540" title="Time-dependent phase separation into Li-rich and Li-poor phases." >}}

The second thing—and this is perhaps more important—is that
experiencing failures as you try and giving your brain time to learn
from them is the only way to mastery. I’m not saying this in some
philosophical sense, I am expressing this as a scientific fact.
Research indicates that errors trigger neuroplasticity. i.e. they
trigger chemicals that inform your neural circuitry that they have to
change.

So summarising these two facts, my advice to you is this. Instead of
comparing yourself to others and thinking of them as exceptional (and
yourself as mediocre), use them as an existence proof to see that if
they can do it, so can you. Then, try to cast experiencing (many,
many) failures as a positive part of your learning journey. This will
keep you going as you get better and better at whatever you are
attempting.

Don’t let your fear of being imperfect stop you from getting good at
things you care about.



## Selected references and further reading

1. [Accompanying IPython notebooks on GitHub][notebooks]
2. [The Stanford course on Convolutional Neural
   Networks][cs231n-course] and [accompanying notes][cs231n-notes]
3. [Deep Learning Book][deep-learning-book]
4. [Deep Visualization Toolbox][deep-visualization-toolbox]
5. [A Neural Algorithm of Artistic Style][arxiv-neural-style-gatys-etal],
   the seminal article
6. [Very Deep Convolutional Networks for Large-Scale Image
   Recognition][arxiv-vgg-simonyan-etal]
7. [Perceptual Real-Time Style
   Transfer][arxiv-fast-neural-style-johnson-etal] and [supplementary
   material][arxiv-fast-neural-style-johnson-etal-supp]
8. TensorFlow Website: MNIST digit classification tutorial [for
   beginners][tensorflow-tutorial-mnist] and [for
   experts][tensorflow-tutorial-mnist-pros], [Deep
   CNNs][tensorflow-tutorial-cnn], [playground][tensorflow-playground]
9. [Keras as a simplified interface to TensorFlow][keras-tensorflow]

[section-introduction]: #so-what-is-prisma-and-how-might-it-work
[section-image-classification-problem]: #the-image-classification-problem
[section-convnets]: #and-finally-convolutional-neural-networks
[section-neural-style-algorithm]: #returning-to-the-style-transfer-problem
[section-neural-style-implementation]: #notebook-6-concrete-implementation-of-the-artistic-style-transfer-algorithm
[notebooks]: https://github.com/hnarayanan/artistic-style-transfer
[notebook-1]: https://github.com/hnarayanan/artistic-style-transfer/blob/master/notebooks/1_Linear_Image_Classifier.ipynb
[notebook-2]: https://github.com/hnarayanan/artistic-style-transfer/blob/master/notebooks/2_Neural_Network-based_Image_Classifier-1.ipynb
[notebook-3]: https://github.com/hnarayanan/artistic-style-transfer/blob/master/notebooks/3_Neural_Network-based_Image_Classifier-2.ipynb
[notebook-4]: https://github.com/hnarayanan/artistic-style-transfer/blob/master/notebooks/4_Convolutional_Neural_Network-based_Image_Classifier.ipynb
[notebook-5]: https://github.com/hnarayanan/artistic-style-transfer/blob/master/notebooks/5_VGG_Net_16_the_easy_way.ipynb
[notebook-6]: https://github.com/hnarayanan/artistic-style-transfer/blob/master/notebooks/6_Artistic_style_transfer_with_a_repurposed_VGG_Net_16.ipynb
[wiki-convnet]: https://en.wikipedia.org/wiki/Convolutional_neural_network
[wiki-softmax]: https://en.wikipedia.org/wiki/Softmax_function
[wiki-cross-entropy]: https://en.wikipedia.org/wiki/Cross_entropy
[wiki-gradient-descent]: https://en.wikipedia.org/wiki/Gradient_descent
[wiki-stochastic-gradient-descent]: https://en.wikipedia.org/wiki/Stochastic_gradient_descent
[wiki-relu]: https://en.wikipedia.org/wiki/Rectifier_(neural_networks)
[wiki-automatic-differentiation]: https://en.wikipedia.org/wiki/Automatic_differentiation
[wiki-universal-approximation-theorem]: https://en.wikipedia.org/wiki/Universal_approximation_theorem
[wiki-imagenet]: https://en.wikipedia.org/wiki/ImageNet
[wiki-munch-scream]: https://en.wikipedia.org/wiki/The_Scream
[cs231n-course]: http://cs231n.stanford.edu
[cs231n-notes]: http://cs231n.github.io
[cs231n-softmax-classifier]: http://cs231n.github.io/linear-classify/#softmax-classifier
[cs231n-gradient-descent-family]: http://cs231n.github.io/neural-networks-3/#update
[cs231n-activation-functions]: http://cs231n.github.io/neural-networks-1/#actfun
[arxiv-neural-style-gatys-etal]: https://arxiv.org/abs/1508.06576
[arxiv-vgg-simonyan-etal]: https://arxiv.org/abs/1409.1556
[arxiv-fast-neural-style-johnson-etal]: https://arxiv.org/abs/1603.08155
[arxiv-fast-neural-style-johnson-etal-supp]: https://cs.stanford.edu/people/jcjohns/papers/fast-style/fast-style-supp.pdf
[tensorflow-tutorial-cnn]: https://www.tensorflow.org/tutorials/deep_cnn
[tensorflow-tutorial-mnist]: https://www.tensorflow.org/get_started/mnist/beginners
[tensorflow-tutorial-mnist-pros]: https://www.tensorflow.org/get_started/mnist/pros
[tensorflow-truncated_normal]: https://www.tensorflow.org/api_docs/python/tf/random/truncated_normal
[tensorflow-playground]: http://playground.tensorflow.org/
[keras]: https://keras.io
[keras-mnist-web]: https://transcranial.github.io/keras-js/#/mnist-cnn
[keras-neural-style]: https://github.com/fchollet/keras/blob/master/examples/neural_style_transfer.py
[keras-applications]: https://github.com/fchollet/keras/tree/master/keras/applications
[keras-tensorflow]: https://blog.keras.io/keras-as-a-simplified-interface-to-tensorflow-tutorial.html
[keras-in-tensorflow]: https://www.youtube.com/watch?v=UeheTiBJ0Io
[prisma]: https://prisma-ai.com
[edtaonisl]: https://www.artic.edu/artworks/80062/edtaonisl-ecclesiastic
[imagenet]: http://image-net.org
[imagenet-ilsvrc-2014]: http://image-net.org/challenges/LSVRC/2014/results
[mnist-dataset]: http://yann.lecun.com/exdb/mnist/
[cross-entropy-reason]: https://jamesmccaffrey.wordpress.com/2013/11/05/why-you-should-use-cross-entropy-error-instead-of-classification-error-or-mean-squared-error-for-neural-network-classifier-training/
[universal-approximation-proof]: http://neuralnetworksanddeeplearning.com/chap4.html
[perceptron-animation]: https://appliedgo.net/perceptron/
[deep-visualization-toolbox]: http://yosinski.com/deepvis
[deep-learning-book]: http://www.deeplearningbook.org
[neural-style-demo-project]: https://github.com/hnarayanan/stylist
[github-neural-style-torch]: https://github.com/jcjohnson/neural-style
