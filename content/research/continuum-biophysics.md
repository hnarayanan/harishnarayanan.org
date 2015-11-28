---
date: 2004-06-01
title: Understanding the physics of biology
short_title: Tissue growth and development
thumbnail: /img/research/continuum-biophysics/constricted-ecf-flow.png
description: 
category: primary
featured: yes
start_date: 2002
end_date: 2007
---

## Recent resplendent results!

First, since alliterations are always fun:

<div class="pure-g">
  <div class="pure-u-1 pure-u-lg-1-2">
    <img class="pure-img" src="http://localhost/files/images/research/continuum-biophysics/highlights/constrict-top-face-displacement.png" alt="">
  </div>
  <div class="pure-u-1-2">
    <img class="pure-img" src="http://localhost/files/images/research/continuum-biophysics/highlights/medicate-solute-concentration.png" alt="">
  </div>
  <div class="pure-u-1-2">
    <img class="pure-img" src="http://localhost/files/images/research/continuum-biophysics/highlights/remodelling-example.png" alt="">
  </div>
</div>


## An index of sorts

*   [An introduction](#introduction)
*   [General formulation for growth in tissues](#formulation)
*   [Mechanics of growing tissue](#mechanics)
*   [Drug delivery and wound healing](#applications)

## <a id="introduction">An introduction</a>

Prompted by compelling clinical reports evidencing the pervasive role of mechanical factors influencing biological growth, our modelling work is aimed at gaining a deeper understanding of the biophysical bases underlying these influences.

<div class="showcase">“All science is either physics or stamp collecting.”  
— [Ernest Rutherford](http://en.wikiquote.org/wiki/Ernest_Rutherford "Need more quotations?") (1871 – 1937)</div>

The utility of the resulting mathematical and computational framework extends across disciplines by helping steer and interpret experimental work, both under physiological and pathological cases of interest. Currently, our focus is directed toward a better understanding of the mechanics of growing soft tissue, specifically tendon.

![Engineerd construct](http://localhost/files/images/research/continuum-biophysics/one-construct.jpg "One of Sarah’s engineered tendon constructs")

Our biological model: Sarah’s engineered tendon constructs.

This web page contains some highlights of our modelling effort. For more detailed expositions, the interested reader is directed toward more [formal articles](http://localhost/writing/).

## <a id="formulation">General formulation for growth in tissues</a>

![Continuum potatoes](http://localhost/files/images/research/continuum-biophysics/tissue-continuum.png "The tissue as a continuum potato")

The tissue as a continuum potato.

_Growth_ in biological tissue is a direct outcome of cascades of complex, intracellular, biochemical reactions involving numerous species, their diffusion across cell membranes, and transport through the extra-cellular matrix. Both reaction and diffusion/transport are influenced by mechanics in a number of ways. Our modelling effort proposes a general continuum field formulation for growth capable of simulating this rich observed behaviour, and proceeds to specialise it incorporating different modelling assumptions—such as the use of an enzyme kinetics-based growth law—to better represent cases of interest.

![Enzyme kinetics](http://localhost/files/images/research/continuum-biophysics/enzyme-kinetics.png "Enzyme kinetics-based growth law")

Enzyme kinetics-based growth law.

Recognising that a growing tissue is an open system undergoing irreversible thermodynamics, the model incorporates the physics of multi-phase reacting systems, and deduces balance laws and a constitutive framework obeying the Second Law of Thermodynamics.

![The balance of mass and momenta for all species](http://localhost/files/images/research/continuum-biophysics/balance-laws.png "The balance of mass and momenta for all species")

Reference configuration statements of the balance of mass and momenta for all species.

Notably, the transport of the extracellular fluid relative to the matrix is shown to be driven by the gradients of stress, concentration and chemical potential—a coupling of mass transport and mechanics that emerges directly.

![Driving forces](http://localhost/files/images/research/continuum-biophysics/driving-force.png "Constitutive relationship for fluid flux")

A constitutive relationship relating the fluid flux to various driving forces.

Assumptions central to existing mechanics theories, such as the nature of the split of deformation maps across the different species involved, and those on momentum transfers between interacting species, are revisited, analysed and carefully revised in cases where they limit the biophysical correctness of predicted growth phenomena.

Coupled, non-linear partial differential equations arise from the theory to describe the complex physics. These differential equations are solved using a finite element scheme based on _operator-splits_; incorporating non-linear projection methods to treat incompressibility, energy-momentum conserving algorithms for dynamics, and mixed methods for stress gradient-driven fluxes.

![FEM Mesh](http://localhost/files/images/research/continuum-biophysics/mesh.png "A representative mesh used in the finite element calculations")

A representative mesh used in the finite element calculations.

One highlight of the numerical methods is a rigorous treatment of numerical stability issues that arise with any operator-splitting scheme. This analysis is critical to the ability to distinguish physical instabilities, such as unbounded growth of tumours, from those that are artifacts of the numerical methods. Another key feature is the reformulation of the reaction-transport equations to embed the incompressibility constraint on the fluid phase, enabling a straightforward implementation of numerical stabilisation in the advection-dominated limit.

![Stabilisable form of the solute transport equation](http://localhost/files/images/research/continuum-biophysics/stabilisable-form.png "The solute transport equation in classical, stabilisable form")

The solute transport equation in classical, stabilisable form.

## <a id="mechanics">Mechanics of growing tissue</a>

![Kinematics of growth](http://localhost/files/images/research/continuum-biophysics/growth-kinematics.png "The kinematics of growth")

The kinematics of growth.

Using model geometries and imposing classes of initial and boundary conditions approximating experiments in our laboratory, the computational framework developed is used to demonstrate aspects of the coupled phenomena as the tissue grows. In these foundational calculations, only two phases—fluid and collagen—are included. The collagen phase is modelled by the anisotropic worm-like chain model, and the fluid phase is modelled as ideal and nearly incompressible. The interconversion between these two phases is modelled using first-order chemical kinetics.

For a tissue undergoing finite strains, the transport equations can be formulated, mathematically, in terms of quantities with respect to either the reference or current (deformed) configuration. However, the physics of fluid-tissue interactions, and the imposition of relevant boundary conditions, is best understood and represented in the current configuration.

<div class="comment">[![Video icon](http://localhost/layout/images/icons/darkgrey/video-x-generic.png "View the video (MPG)")](http://localhost/files/video/research/continuum-biophysics/pinch_cont4.mpg) Watch the [unbounded build-up of fluid](http://localhost/files/video/research/continuum-biophysics/pinch_cont4.mpg) due to the (unphysical) specification of constant reference fluid concentration boundary conditions, while attempting to simulate a loaded tendon immersed in a bath.</div>

<div class="comment">

### Having difficulty viewing a video?

[![Help icon](http://localhost/layout/images/icons/darkgrey/help-browser.png "Download the required codecs for Windows")](http://sourceforge.net/projects/ffdshow/) In order to make their sizes more palatable for download, the videos on this page have been compressed using different algorithms. If you are having difficulty viewing any of them, please follow the following instructions on acquiring the necessary [codecs](http://en.wikipedia.org/wiki/Codec):  

» Windows users need to download and install the [ffdshow codec pack](http://sourceforge.net/projects/ffdshow/). Upon installation, you should be able to play the videos using any installed video player, including Windows Media Player.  

» GNU/Linux and Mac OS X users need to download and install either [VLC Media Player](http://www.videolan.org/vlc/) or [MPlayer](http://www.mplayerhq.hu/design7/news.html) (with a complete set of codecs) to play the videos.</div>

When a tendon having an initially-uniform distribution of collagen is immersed into a nutrient-rich bath, nutrient-rich fluid is transported into the tissue, and growth occurs due to the formation of additional collagen.

![Final distribution of collagen](http://localhost/files/images/research/continuum-biophysics/swell-after-growth.png "Distribution of collagen after growth")

Distribution of collagen after growth.

<div class="comment">[![Video icon](http://localhost/layout/images/icons/darkgrey/video-x-generic.png "View the video (DivX AVI)")](http://localhost/files/video/research/continuum-biophysics/swell_cont5.avi) The infusing nutrient-rich fluid causes the tendon to grow. Watch the [collagen concentration increase](http://localhost/files/video/research/continuum-biophysics/swell_cont5.avi) over half-an-hour.</div>

There is a rapid, fluid transport-dominated swelling of the tendon initially as it is immersed into the fluid bath. This is followed by a slower, reaction-driven growth phase.

![Volume evolution](http://localhost/files/images/research/continuum-biophysics/swell-volume-evolution.png "Rapid swelling of a tendon immersed in a bath")

Rapid swelling of a tendon immersed in a bath.

<div class="comment">[![Video icon](http://localhost/layout/images/icons/darkgrey/video-x-generic.png "View the video (MPG)")](http://localhost/files/video/research/continuum-biophysics/swell_cont4.mpg) Pay close attention to observe the initial, [fluid transport-dominated swelling of the tissue](http://localhost/files/video/research/continuum-biophysics/swell_cont4.mpg), followed by much slower reaction-driven growth.</div>

On performing a uniaxial tension test on the tendon before and after growth, it is observed that the grown tissue—having a higher concentration of collagen—is stiffer and stronger; which is in accordance with experiment.

![Uniaxial stress-strain curves](http://localhost/files/images/research/continuum-biophysics/swell-growth-mechanics.png "The grown tissue is stiffer and stronger")

The grown tissue is stiffer and stronger.

Upon subjecting the tendon to a load-unload cycle, a stress-strain curve characteristic of viscoelastic tissue is observed. Here, the area between the loading and unloading paths is the hysteretic energy loss due to viscous dissipation.

![Viscoelastic effects](http://localhost/files/images/research/continuum-biophysics/tendon-viscoelasticity.png "Viscoelastic effects observed in the model")

Viscoelastic effects observed in the model.

<div class="comment">[![Video icon](http://localhost/layout/images/icons/darkgrey/video-x-generic.png "View the video (FFMPEG AVI)")](http://localhost/files/video/research/continuum-biophysics/cyclic-sin.ffmpeg.avi) Observe the [induced fluid flow](http://localhost/files/video/research/continuum-biophysics/cyclic-sin.ffmpeg.avi) as the tendon is subjected to a cyclically varying load. Friction between the solid and fluid phases results in energy dissipation.</div>

Qualitatively, this viscoelastic behaviour compares favourably with our corresponding experimental tests on two-week-old tibialis anterior tendons in the laboratory.

![Hysteresis in tendon](http://localhost/files/images/research/continuum-biophysics/hysteresis-experiment.png "Hysteresis observed in experiments on TA tendons")

Hysteresis observed in experiments on tibialis anterior tendons.

Application of a constrictive radial load—where the maximum strain in the radial direction is experienced half-way through the height of the tendon—to a tendon immersed in a fluid-filled bath results in a stress-gradient induced fluid flux. This drives fluid away from the central plane.

![Vertical fluid flux in a constricted tendon](http://localhost/files/images/research/continuum-biophysics/constrict-vertical-flux.png "Vertical fluid flux in a constricted tendon")

Vertical fluid flux in a constricted tendon.

<div class="comment">[![Video icon](http://localhost/layout/images/icons/darkgrey/video-x-generic.png "View the video (DivX AVI)")](http://localhost/files/video/research/continuum-biophysics/constrict_total_flux_3_4.avi) The constrictive radial load sets up a [fluid flux in the vertical direction](http://localhost/files/video/research/continuum-biophysics/constrict_total_flux_3_4.avi), driving fluid away from the central plane toward the top and bottom faces of the tendon.</div>

This pressure wave set up in the fluid travels toward the top and bottom faces, and as the fluid leaves these surfaces, we observe that the tendon relaxes.

![Displacement of the top face](http://localhost/files/images/research/continuum-biophysics/constrict-top-face-displacement.png "Relaxation of the top face of a constricted tendon")

Relaxation of the top face of a constricted tendon.

<div class="comment">[![Video icon](http://localhost/layout/images/icons/darkgrey/video-x-generic.png "View the video (DivX AVI)")](http://localhost/files/video/research/continuum-biophysics/constrict_ref_conc_3.avi) The stress gradient-driven fluid flux causes a [decrease in the reference fluid concentration](http://localhost/files/video/research/continuum-biophysics/constrict_ref_conc_3.avi) near the central plane. Pay close attention to observe the relaxation of the top face as the fluid leaves the surface.</div>

## <a id="applications">Drug delivery and wound healing</a>

Having established the fundamental behaviour of the formulation, we now turn to more sophisticated applications.

In order to model localised, bolus delivery of regulatory chemicals to the tendon while accounting for mechanical effects, we introduce additional species: a solute, and a distribution of fibroblasts that are characterised by their cell concentration. Both concentration gradient-driven mass transport and stress gradient-driven fluid flow are incorporated into this illustration, which demonstrates the use of the formulation in studying the efficacy of drug delivery mechanisms. Michaelis-Menten enzyme kinetics is used to determine the rates of solute consumption and, consequently, collagen production.

![Michaelis-Menten enzyme kinetics](http://localhost/files/images/research/continuum-biophysics/michaelis-menten.png "Michaelis-Menten enzyme kinetics")

Michaelis-Menten enzyme kinetics.

In addition to subjecting the tendon immersed in the bath to the constrictive radial load described earlier, a solute-rich bulb with its centre on the axis of the tendon is introduced. The relatively small magnitude of the fluid mobility—with respect to the diffusion coefficient for the solute through the fluid—results in a relatively small stress gradient-driven flux, and the transport of the solute is diffusion dominated. Consequently, as time progresses, the solute primarily diffuses locally, and as the solute concentration in a region increases, the enzyme-kinetics model predicts a small source term for collagen, and we observe nominal growth.

![Collagen concentration at an early time](http://localhost/files/images/research/continuum-biophysics/medicate-solute-concentration.png "Collagen growth localised to regions of medication")

Collagen growth localised to regions of medication.

The following computation demonstrates the capability of the formulation in studying the self-healing of damaged tissue. Incorporating a cell-signalling parameter into the chemical kinetics, the formation of collagen is spatially biased toward damaged regions of the tissue.

![Chemical kinetics with damage healing](http://localhost/files/images/research/continuum-biophysics/damage-healing-source.png "Chemical kinetics with a damage-healing parameter")

Chemical kinetics with a damage-healing parameter.

Turning to damaged skin as our tissue of interest, we begin by delineating the damaged regions—characterised by a sudden reduction in the concentration of collagen—from the rest of the tissue.

![Damaged region of skin](http://localhost/files/images/research/continuum-biophysics/damaged-region.png "Damaged region of skin demarcated by green")

Damaged region of skin demarcated by green.

This damaged tissue is introduced to a nutrient-rich environment, and the cell-signalling parameter induces preferential growth in these damaged regions. We allow this healing process to evolve under two different conditions—under no load and under uniaxial stress—to study the influence of mechanics on the properties of healed tissue.

The anisotropic nature of these tissues arises from the microstructural alignment of their constituent collagen fibers, and the directionality of newly-deposited fibers are determined by the eigenvectors of the applied stress field. When the healing process is carried out under uniaxial stress, with the orientation of the stress being defined by the initially-stiff directionality of the tissue, the newly-deposited collagen has anisotropic properties which are identical to collagen in the undamaged tissue. This results in a healed tissue indistinguishable from the undamaged tissue.

However, when the healing process is carried out under no load, the newly-deposited collagen consists of arbitrarily-directed fibers, resulting in a formation of isotropic tissue in the damaged regions as the tissue heals. This results in a healed tissue being more compliant than the undamaged tissue along the originally-stiff direction of the tissue. Thus, upon being subjected to a load, these compliant healed regions experience a reduced stress.

![Vertical stress in skin](http://localhost/files/images/research/continuum-biophysics/damaged-vertical-stress.png "Vertical stress in skin recovering from damage")

Vertical stress in skin recovering from damage.

This result is analogous to the experimentally observed hypertrophic scarring of skin as it recovers from damage under no applied load.

{{< figure src="/img/research/automated-mechanics/fishy.gif" title="Hyperelastic dolphin in a flow field." >}}

[hyperelastic]: https://en.wikipedia.org/wiki/Hyperelastic_material
