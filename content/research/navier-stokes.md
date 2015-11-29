---
date: 2008-06-01
title: Some thoughts on the Navier-Stokes equations
short_title: Navier-Stokes formulation
thumbnail: /img/research/navier-stokes/navier-stokes.png
description: Theoretically equivalent formulations aren’t always equal in practice.
category: curiosity
start_date: 2008
includes_math: yes
---

## A tale of two formulations

It is common in the literature to start with the _Laplacian
formulation_ of the Navier-Stokes equations,

<p>
\begin{align}
\mathrm{div}(v) &= 0  \\
\rho \frac{\partial v}{\partial t} + \rho \left(\mathrm{grad}(v)\right)v &= -\mathrm{grad}(p) + \mu\; \mathrm{lap}(v)\;,
\end{align}
</p>

when going about deriving numerical methods to simulate incompressible
viscous flow. When considered in this strong form, the above
formulation is equivalent to the following _divergence formulation_
arising from continuum mechanics:

<p>
\begin{align}
\mathrm{div}(v) &= 0  \\
\rho \frac{\partial v}{\partial t} + \rho \left(\mathrm{grad}(v)\right)v &= \mathrm{div}(\sigma),
\end{align}
</p>

where, for our Newtonian fluid, $\sigma = -p\; I\ + \mu\;
\left(\mathrm{grad}(v) + \mathrm{grad}(v)^{T} \right)$.

Even though these two points of view are equivalent in the strong
form, there are a few things one should keep in mind in practice. When
integrated by parts to construct a weak form suitable for the finite
element method, the two formulations above return different Neumann
boundary terms. The divergence formulation introduces a boundary term
with the traction, $\sigma\; n$, whereas the Laplacian formulation
introduces a term with the normal derivative of the velocity,
$\frac{\partial v}{\partial n}$. This means:

1. You probably want to pick the formulation based on the kind of
boundary conditions you wish to impose. e.g., If you are considering a
fully-developed channel flow, you know that there is a pressure and an
(unknown, non-zero) shear stress at the outlet. Since you cannot set
an unknown stress condition, the natural choice for this case is the
Laplacian formulation with conditions $\frac{\partial v}{\partial n}
= 0$ and $\int p = 0$. On the other hand, if you were
considering free surface flow, you need to set the traction at the
surface to a known value (usually 0). In this case, the divergence
formulation is the logical choice.

2. You need to be aware of some subtleties involved in impementing
the Laplacian formulation, or you may end up [violating
objectivity](http://dx.doi.org/10.1002/fld.1480) (as this formulation
does not introduce the notion of a symmetric Cauchy stress).

3. In accordance with the formulation you choose, you must pay
attention to how you implement boundary conditions. Otherwise you will
(obviously) not see the flow you want.

{{< figure src="http://localhost/files/images/research/navier-stokes/channel-flow-proper.png" title="Channel flow with proper boundary conditions." >}}

{{< figure src="http://localhost/files/images/research/navier-stokes/channel-flow-improper.png" title="Divergence formulation with (improper) “do nothing” traction boundary conditions." >}}

## Some analytical solutions

The following are some analytical solutions for the Navier-Stokes
equations, useful in [benchmarking](https://launchpad.net/nsbench)
numerical algorithms.

* [A 2D solution](http://localhost/files/projects/navier-stokes/analytical-ns-2d.pdf) generated in Mathematica.
* [A 3D solution](http://localhost/files/projects/navier-stokes/analytical-ns-3d.pdf) generated in Mathematica.
* A SymPy script used to [test analytical fluid-structure-interaction solutions](http://localhost/files/projects/navier-stokes/analytical_fsi.py).
