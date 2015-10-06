---
date: 2010-01-03
title: Adaptive multiphase flow through porous media
short_title: Multiphase flow in porous media
thumbnail: /img/research/porous-flow/adaptive-water-snake.gif
featured: yes
period: 2010
---

From the transport of dissolved nutrients through biological tissue to
the extraction of petroleum from underground deposits, there are
numerous systems in which it of interest to study the flow of multiple
fluids through porous media. In many useful cases, the physics of the
flow is characterised by coupled governing equations that are
nonlinear and transient, and the problem is further complicated by
material heterogeneity and irregular geometries.

The goal of this work is to devise and implement general numerical
algorithms for such systems. Our specific focus is on robustness
through adaptive error-control and normal-human-readable
implementation. (How many buzzwords can you cram into a sentence?)

The following animation presents the results from a simple (yet
non-trivial!) calculation involving the flow of water and oil through
fluid-saturated clay. The flow is driven from left to right by a
pressure gradient. Because of the specific choice of a [single,
winding crack][dealiiexample] that snakes through the domain, it is in
this high-permeability region that the greatest flow rates are set up.

{{< figure src="/img/research/porous-flow/adaptive-water-snake.gif" title="Water snaking through oil-rich clay!" >}}

The model for the above example contains an elliptic equation and a
nonlinear hyperbolic transport equation. This system is solved at each
time-step using a mixed finite element formulation for the total
velocity, pressure and water saturation in the BDM(q) x DG(q-1) x DG(q
-1) space. The Crank-Nicholson scheme is used for progressing through
time, and the mesh is adapted using a dual-weighted residual strategy
to concentrate the degrees of freedom in interesting parts of the
domain.

This research was carried out in collaboration with Garth N. Wells at
the University of Cambridge from November 2009 to February 2010\. The
[code for this effort][src] comprises entirely of a few hundred lines
of human-readable Python sitting atop the [FEniCS Project][fpo]. It is
released as Free Software under the GNU GPL.

[dealiiexample]: http://www.dealii.org/6.2.1/doxygen/deal.II/step_21.html#plain-Singlecurvingcrackpermeability
[src]: http://localhost/files/projects/adaptive-porous-flow/adaptive-porous-flow.zip
[fpo]: http://fenicsproject.org/
