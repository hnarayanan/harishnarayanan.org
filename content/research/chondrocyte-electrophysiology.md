---
date: 2011-09-19
title: An electrophysiological model for the chondrocyte
short_title: Chondrocyte physiology
description: Better understanding the cell type responsible for the synthesis of cartilage.
thumbnail: /images/research/chondrocyte-electrophysiology/chondrocyte-micrograph-cropped.jpg
category: primary
start_date: 2010
end_date: 2011
---

Cartilage is the soft tissue that cushions bones at joints and usually
allows for bones to slide past each
other. [Osteoarthritis][Osteoarthritis] is a debilitating disorder
that's caused when cartilage starts to wear out, resulting in painful
and reduced mobility for sufferers of the condition. There exist no
drugs that slow down the progression of the disease.

In this work, we use computer models to better understand the cell
responsible for the synthesis of cartilage: *the chondrocyte*.

{{< figure src="/images/research/chondrocyte-electrophysiology/chondrocyte-micrograph.jpg" title="Electron micrograph of a typical articular chondrocyte (Archer & Francis-West, 2003)." >}}

Chondrocytes seem to be at the crux of our story because they are the
single cell type found in cartilage. They are extremely active cells
capable of responding to a range of mechanical and chemical
stimuli. Research indicates that these responses are crucial to their
creation and maintenance of viable cartilage, though the details of
these processes are poorly understood.

In our study, we use computer models of the chondrocyte to study its
response to its constantly changing environment. In particular, we
look at how the cell’s [resting membrane potential][RMP] (RMP)
evolves, as abnormal regulation of the RMP in these cells is linked to
abnormal volume regulation when loaded, altered signaling and cell
death.

Focussing our attention on a single chondrocyte cell residing in deep
regions of cartilage, we construct an ordinary differential equation
(ODE) system model that links the membrane potential of the cell with
the flux of various ions in and out of the cell membrane through ion
channels. Our solver for this equation system is implemented in
Octave, and [a current version is available][Source] as Free Software
under the GNU GPL.

{{< figure src="/images/research/chondrocyte-electrophysiology/chondrocyte-model.png" title="A schematic of the ion channels in a single chondrocyte." >}}

When our computer model of the chondrocyte is subjected to several
different clinically-relevant environments, we begin to gain an
understanding of the underlying behavior of the cell.

{{< figure src="/images/research/chondrocyte-electrophysiology/model-experiment-comparison.png" title="Comparing the model behaviour (blue) with experiment (red)." >}}

 Our research suggests ideal conditions that the cell must be
 subjected to as it relates to the synthesis of viable cartilage, and
 circumstances where this might be disrupted. We envision that the
 insight gained from this work will help in multiple ways. First, it
 will help clinicians and biochemists design better drugs to treat the
 condition of osteoarthritis. Second, it will help suggest to patients
 subtle changes to their lifestyle which could help reduce the
 degradation of cartilage resulting from age, greatly improving their
 quality of life.

[Osteoarthritis]: https://en.wikipedia.org/wiki/Osteoarthritis
[RMP]: http://en.wikipedia.org/wiki/Resting_potential
[Source]: https://github.com/hnarayanan/chondrocyte-electrophysiology
