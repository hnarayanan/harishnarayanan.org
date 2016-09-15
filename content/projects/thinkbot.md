---
date: 2013-03-15
title: thinkbot
short_title: thinkbot
thumbnail: /images/projects/thinkbot/thinkbot.svg
description: A modern platform for computational science.
category: website
start_date: 2013
featured: yes
includes_video: yes
---

[thinkbot](http://thinkbot.net/) has been a labour of love of mine for
some years now. Since it's currently being rebuilt from scratch (as it
often seems to be), I am going to leave you with a story instead of
pointing you to something you can play with.

The idea for the project began at a simple place: To make a tool that
allows people to easily solve differential equations online.

{{< video src="Ey-jSRveWJQ" width="720" height="540" title="An online tool for solving differential equations." >}}

The motivating utility of this tool was to allow students to simulate
simple mechanical systems right in the browser. I wanted them to be
excited to learn concepts in mechanics, and teach students practical
skills in computational science along the way.

---

As I worked on the idea, thinkbot morphed into a [general purpose
API](https://github.com/thinkbot-project/api) to solve a set of
mathematical problems in Python, Octave and R. This API served as the
computational backend of a mechanics education site called [Mechanics
Academy](http://mechanicsacademy.org).

{{< figure src="/images/projects/thinkbot/thinkbot-api-mechanics-academy.png" title="thinkbot backing a calculation on Mechanics Academy." >}}

It also served as the backend to a [numerical simulation
component](https://github.com/hnarayanan/thinkbot-xblock) built for
the [edX Platform](https://open.edx.org).

{{< figure
src="/images/projects/thinkbot/thinkbot-api-edx-xblock.png"
title="thinkbot serving up calculations in edX Xblocks." >}}

At some point I even wrote an iOS app as a client!

{{< video src="pCM2wC-Tw5Q" width="720" height="540" title="The thinkbot viewer iOS application in action." >}}

---

As I've gone through all this experimentation, my vision for the
project has morphed yet again. But this time, *it's starting to feel
fully formed*. What follows is a bit of a manifesto for the next
incarnation of thinkbot.

> At its core, thinkbot will be a platform that allows computational
scientists to easily package and run their code on the cloud. This
makes high performance computing a commodity, and has obvious
implications for the reproducibility and collaborative evolution of
computational science.

> The project will be developed in the open, and released under a
liberal open source license. It will have a strong code of
conduct that encourages a helpful, inclusive and kind community around
it.

> thinkbot's technical design is heavily inspired by projects like Deis
and openshift, and will leverage Kubernetes at its core. Atop this
core platform, there'll exist a general purpose REST/RPC/WebSockets
layer that easily allows for things like iOS UIs.

It'll be awesome, and I'm excited.
