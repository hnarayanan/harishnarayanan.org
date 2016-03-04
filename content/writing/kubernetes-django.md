---
date: 2016-04-07T21:12:08+01:00
title: Scalable and resilient Django with Kubernetes
category: devops
tags:
   - kubernetes
   - django
---

If things work out as you've envisioned, there will be a time in your
webapp's lifecycle where it's serving a large number of users. By the
time things get to this point, it's ideal if you've architected your
webapp to both *scale* gracefully to meet this load, and also be
*resilient* to arbitrary failures of underlying compute resources.

This article is about how you can use [Docker
containers][docker-containers] and [Kubernetes][kubernetes] to help
your [Django][django] webapp achieve these architectural goals. While
it meanders a bit through theory and philosophy, it does work up to a
[concrete example][example] to help solidify concepts.

## Caveats

Before we get too deep into the weeds, I'd like to note that the ideas
expressed in this piece don't have anything particular to do with
Django. I've simply chosen it as an example because it is a popular
framework that I'm familiar with. It is straightforward to repurpose
these principles for other software stacks.

I'd also like to point out that this article juggles many moving
pieces -- some quite immature. If you can avoid this level of
complexity at the current stage of your webapp's lifecycle, *you
should*. Instead, focus your efforts on better understanding your
users' problems and testing whether your app solves them. No one is
going to know or complain that you're running your app on a single
fragile server until enough people care to use your app regularly.

*No one.*

With that out of the way, let's get started.

## What is the problem we're trying to solve?

Let's imagine that you're working on a Django webapp that's laid out
in a fairly standard fashion: All your app's data resides in a
PostgreSQL database. The app itself is written in Django-flavoured
Python, and is served up using the uWSGI application server. And in
front of all this, you have the NGINX web server acting both as a
reverse proxy and a static content server.

{{< figure src="//placehold.it/1440x960" title="Layout of a non-trivial Django application." >}}

When you're first starting out with your app and you only have a
handful of users, it makes perfect sense to run all these pieces on a
single server. So you run up to your [favourite cloud
provider][digital-ocean-referral], fire up a VPS running Debian or
whatever, and install all these individual bits of software on the
same machine.

{{< figure src="//placehold.it/1440x960" title="All pieces making up the app on a single machine." >}}

Then, as your app starts to get more popular, you begin to work on
scaling. At first, you follow the straightforward approach and simply
provision large and larger single machines to run your app in. This is
called *vertical scaling* and works well until you reach a few
thousand users.

And then your app gets *even more* popular.

Now you realise that if you were to split the components making up
your app and put them on separate machines, you can scale the
components independently. Meaning, for example, that you can run
multiple instances of your app (called *horizontal scaling*) to handle
your growing user base, while continuing to run your PostgreSQL server
on only one (but increasingly powerful) machine.

{{< figure src="//placehold.it/1440x960" title="Running many instances of the app talking to a single database." >}}



1. You're likely going to run into a scenario where you provision
multiple Django app instances trying to cope with a certain peak load,
but your normal load doesn't need nearly as many computing
resources. This is a waste of money.

2. If a computing resource fails, e.g. someone spills coffee on your
VPS, that component of your app simply stops working.

These are part of the problems Kubernetes is designed to solve.

*What is Kubernetes?* It's a container orchestration framework that
takes "containerised" applications and schedules them rationally on
clusters. *What's a containerised app?* It's a piece of software ---
like your Django app --- that's been packaged into a specific format
bundling the app, its requirements and whatever stateless content it
needs into one convenient bundle. Many people tend to describe
containers as lightweight virtual machines, but I prefer to think of
them as [fat static binaries][container-perspective] of apps.

## So how exactly does Kubernetes help solve these problems?

If we were to "containerise" the pieces of our application and run
them in a replicated way on our closuter, we get the ability to
*scale* our app with load. (If this happens automatically, all the
better.) If we were further able to monitor and heal these containers
(again, thinking of each one as one process of a static binary) ruch
that if they stopped for whatever reason (e.g. if the underlying
hardware died), they'd cleanly be restarted elsewhere, we'd then have
a system that would be *reliable*.

Kubernetes offers a user-friendly API that allows us to do just this.

It contains the following pieces

(A) To achieve our twin goals of scalability and resiliency, we're going
to follow a simple pattern:

1. We break up our Django application into atomic units that can be
easily built, tested and run anywhere.

2. We run multiple copies each kind of unit behind a corresponding
load balancer.

This becomes hard because what about load balancer ip discovery etc.,
making sure your replicas are running etc.? Container techologies like
Docker (or Rocket) offer a plan for the first point, while Kubernetes
offers a plan for the second.

If this seems a bit abstract, let's imagine what a non-trivial webapp
involving Django might look like: (probably goes to (A)):

* A Postgresql database serving as the core persistence tier.
* Memcached providing caching to prevent …
* Django + uwsgi …
* ```
  database ←-\
  search ←-> api ←-> webapps ←-> users
  workers ←-> queue ←-/
  ```

Now, it's of course possible to run all this and more on a single
Linux server, and it is … but how would you scale the pieces
independently? E.g., how can you greatly increase the computational
capacity provided by Celery without getting a larger and larger box
(whose resources aren't touched by the other components)? Furthermore,
what happens when this one server goes down for whatever reason?

… (That business from above that started this section gets moved here)

To simplify this story, we have an app that looks like the following,
or the classic Django app:

database <-> django (uwsgi) <-> nginx <-> users

Adding more pieces to this puzzle is left as an exercise for the
reader. Please submit pull-requests to the original repo. if you work
some of these out.

Break your Django ++ app into pieces (and containerise them). Replace
each individual piece with a load-balancer encompassing a collection
that you can replication manage.

Why and when in an application's lifecycle would you want to do this?

A brief introduction to containerised Django + cohorts

Orchestrating them together with Kubernetes

Explaining some tricks with the sample code to show how the app can be
(manually) scaled to meet known traffic demands. Hit with ab bench (or
whatever it is called), knock a server out and see how it behaves.

## A detour through containerization

Container technology (such as Docker or Rocket) is a really big deal
at the moment

Split your system into components -> Make each component a container
(an atomic unit that can run anywhere)

> This changes how you think about the boundaries of your
  application. Consider my case of hosting this static
  website. Typically you'd think of this blog as the collection of
  HTML, CSS, and images that make up the site.

> What you think your application is affects how you deploy it. If
  your application is a bundle of files then “deploying” means placing
  these files inside a software system that understands HTTP and can
  serve files, e.g. Apache or Nginx.

> Compare this to how I'm using Docker for this blog. Instead of using
  a global Nginx instance to serve my blog, I create a Docker image
  with Nginx and my blog's files. Which makes the resulting “blog
  application” an atomic unit that I can build, test, and run anywhere
  as many times as I want.

Container technology (such as Docker or Rocket) is a really big deal
these days. I wouldn't claim to understand completely, but here is a
rough analogy.

There is a lot of talk about containers (Docker, Rocket etc.) recently
and I won't claim to be an expert. But here is how I understand the
situation. Think of a container as a process.

You might traditionally think of a simple website as a collection of
HTML and CSS files that you store on a server somewhere. On this
server also runs a web server (such as Apache or NGINX) that serves
your files to any incoming requester

* Containerisation (and building containers)
* Orchestration with Kubernetes
* Practical example on GKE

### PostgreSQL

#### Persistence

- Create a persistent disk
- Attach to VM
- ssh into VM
- Format disk
- Log out of VM
- Detach from VM

```
gcloud compute disks create --size=500GB --zone=us-central1-a my-data-disk
```

http://kubernetes.io/v1.1/docs/user-guide/persistent-volumes.html#persistent-volumes-and-claims

> A PersistentVolume (PV) is a piece of networked storage in the
  cluster that has been provisioned by an administrator. It is a
  resource in the cluster just like a node is a cluster resource. PVs
  are volume plugins like Volumes, but have a lifecycle independent of
  any individual pod that uses the PV. This API object captures the
  details of the implementation of the storage, be that NFS, iSCSI, or
  a cloud-provider-specific storage system.

> A PersistentVolumeClaim (PVC) is a request for storage by a user. It
  is similar to a pod. Pods consume node resources and PVCs consume PV
  resources. Pods can request specific levels of resources (CPU and
  Memory). Claims can request specific size and access modes (e.g, can
  be mounted once read/write or many times read-only).

## Selected references and further reading

1. [Building Scalable and Resilient Web Applications on Google Cloud
Platform][gcp-scalable-webapps]
2. [Linux Containers: Parallels, LXC, OpenVZ, Docker and
More][linux-containers]
3. Deploying a containerised Rails app to Google Container Engine with
Kubernetes — [Part 1][kubernetes-rails-1], [Part
2][kubernetes-rails-2], [Part 3][kubernetes-rails-3]
4. Understanding Kubernetes from the ground up — [Kubelet][kubernetes-kubelet],
[API Server][kubernetes-api-server], [Scheduler][kubernetes-scheduler]
5. [Packaging Django into containers][django-container]
6. https://blog.oestrich.org/2015/08/running-postgres-inside-kubernetes/

[example]: https://github.com/hnarayanan/django-k8s
[linux-containers]: http://aucouranton.com/2014/06/13/linux-containers-parallels-lxc-openvz-docker-and-more/
[docker-containers]: https://www.docker.com/what-docker
[kubernetes]: http://kubernetes.io
[django]: https://www.djangoproject.com
[gcp-scalable-webapps]: https://cloud.google.com/solutions/scalable-and-resilient-apps
[kubernetes-rails-1]: http://www.thagomizer.com/blog/2015/05/12/basic-docker-rails-app.html
[kubernetes-rails-2]: http://www.thagomizer.com/blog/2015/07/01/kubernetes-and-deploying-to-google-container-engine.html
[kubernetes-rails-3]: http://www.thagomizer.com/blog/2015/08/18/k8s_secrets.html
[kubernetes-kubelet]: http://kamalmarhubi.com/blog/2015/08/27/what-even-is-a-kubelet/
[kubernetes-api-server]: http://kamalmarhubi.com/blog/2015/09/06/kubernetes-from-the-ground-up-the-api-server/
[kubernetes-scheduler]: http://kamalmarhubi.com/blog/2015/11/17/kubernetes-from-the-ground-up-the-scheduler/
[django-container]: http://michal.karzynski.pl/blog/2015/04/19/packaging-django-applications-as-docker-container-images/
[digital-ocean-referral]: https://m.do.co/c/e3559ea013de
[container-perspective]: http://bricolage.io/hosting-static-sites-with-docker-and-nginx/
