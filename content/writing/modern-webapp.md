---
date: 2015-09-12T15:25:19+01:00
draft: true
title: Architecting a modern webapp with Django and AngularJS
category: development
---

![Imagining a new webapp](/images/blog/computer-sketchbook-camera.jpg "Imagining a new webapp")

## A brief history of time

In the elder days, most websites were simply collections of static files. All you needed to do was to write a few pages of HTML in your favourite text editor (or heaven forbid, Frontpage) and toss it up on a web server. Then, the three people browsing the Internet would be thankful that they had *something* to read. Things were uncomplicated, and life was good.

But then times changed.

Today's websites are in fact complex programs that boast a remarkable level of functionality and polish. And as daunting as it is to think about the number of moving parts in something like an [Airbnb](https://www.airbnb.com/) or [GitHub](https://github.com/), sites like these have come to define the level of sophistication that people now expect.

In this sequence of articles, we'll explore some of the key ingredients going into such modern webapps, in particular those that are driven by a lot of data. I've needed to learn a lot of this stuff from different corners of the web in the past year, and these articles are my way of collating all this knowledge in one place. Please let me know if you find it helpful, and do [let me know](mailto:mail@harishnarayanan.org) if you need me to clarify anything.

## What we're going to learn

I've decided to split the topics we'll be covering over the subsequent weeks into the following four broad themes. Our story begins with the user and progressively works its way deeper into the technology stack.

Along our journey, I'm going to draw upon ideas from software engineering to guide broad design decisions. I'm also going to make specific software choices that simplify each of our steps. And to make things really concrete, we'll work through a [comprehensive example]() that ties all these ideas together.

### Frontend app

Using a powerful client-side JavaScript framework that presents the user with an intuitive interface for solving their problem.

1. **Identifying need:** Finding an interesting problem to solve, and using [behaviour-driven development]() to validate user requirements.

2. **Starting with AngularJS:** Getting our AngularJS app off the ground with the help of Yeoman.

3. **Building our frontend app:** Go from our design sketches and ideas to a working AngularJS app with the help of (but without abusing) Bootstrap.

### Getting the frontend and the backend talking to each other

1. Auth. + JWT

2. Resource handling with smart wrappers of AngularJS's Resource service.

### Backend API

Determining a clean way of representing and storing data, and exposing this data to the world using a well-tested [REST API]().

1. Data modelling

2. TDD

3. Django + Django REST Framework


### Meta and system administration

Understanding the benefits of modern tools and workflows when developing, testing and deploying webapps.

1. Layout of our repositories

2. Fabric for deployment (and Ansible for provisioning)

3. Server-side config (nginx, uwsgi, postgres etc.)




<!-- ## SaaS architecture

## User Stories

## Verification: Test-driven development

## Agile Methods

## Performance, upgrades and practical security -->

<!--

API: Django (REST Framework) + Elasticsearch
Webapp: AngularJS, Bootstrap

1. Going from broad problem requirements to a sketch
2. Converting the sketch to a Bootstrap template
   - Proper usage of Bootstrap
   - Using Yeoman to scaffold it
   - Using BDD to define its spec
3. Using mock data in templates to guide corresponding API endpoints and functionality
4. Using TDD to develop the core API using Django (REST Framework)
5. Communicating between the API and the webapp
   - Authentication
   - Other security: CORS, etc.
6. Search

-->
