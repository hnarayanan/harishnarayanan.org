---
date: 2015-09-07T21:12:08+01:00
draft: true
title: Scalable and resilient Django with Kubernetes
category: devops
---

If things work out as you’ve envisioned, there will be a time in your
webapp’s lifecycle where it’s going to be serving a large number of
users. By the time things get to this point, it’s ideal if you’ve
architected your webapp to both scale gracefully to meet this load,
and also be resilient to arbitrary failures of underlying compute
resources.

This article is about how you can use containers and Kubernetes to
help your Django webapp achieve these architectural goals. While it
meanders a bit through theory and philosophy, it does work up to a
concrete example to solidify concepts.

## Caveats

Before we get too deep into the weeds, I’d like to note that the ideas
expressed in this piece don’t have anything particular to do with
Django. I’ve simply chosen it as an example because it is a framework
I’m familiar with. You can easily repurpose these principles for other
software stacks.

I’d also like to point out that this article juggles many moving
pieces --  some quite immature. If you can avoid this level of
complexity at the current stage of your webapp’s lifecycle, you
should. Instead, focus your efforts on building and testing features
with your users until you’re happy with the traction you’re seeing. No
one is going to know or complain that you’re running your app on a
single server until enough people care to use your app regularly.

With that out of the way, let’s get started.

## What are we trying to do?

Break your Django ++ app into pieces (and containerise them). Replace
each individual piece with a load-balancer encompassing a collection
that you can replication manage.

Why and when in an application’s lifecycle would you want to do this?

A brief introduction to containerised Django + cohorts

Orchestrating them together with Kubernetes

Explaining some tricks with the sample code to show how the app can be
(manually) scaled to meet known traffic demands. Hit with ab bench (or
whatever it is called), knock a server out and see how it behaves.
