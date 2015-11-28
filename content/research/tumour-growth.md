---
date: 2008-01-01
title: Modelling the energetics of growing tumours
short_title: Energetics of tumours
description: Modelling the bio-chemo-mechanics of tumour growth.
thumbnail: /img/research/tumour-growth/tumour-growth.png
category: primary
start_date: 2006
end_date: 2010
---

Cancer is a collective term for a class of diseases that are a leading
cause of death worldwide. The [World Health Organization
reports](http://www.who.int/mediacentre/factsheets/fs297/en/) that in
2008 alone, 7.6 million deaths (about 13% of all deaths worldwide)
were the result of various kinds of cancerous tumours. The development
of a tumour is a complex phenomenon whose immediate cause is that some
specific cell type has managed to overcome the usual regulatory
signals of the cell cycle to grow, proliferate and live beyond its
normal, programmed range. These rapidly proliferating, diseased cells
proceed to invade surrounding tissue and later spread to other organs
in a process called metastasis, which is often fatal.

The processes that drive the growth and development of tumours are
numerous and intricately coupled, but the fact that they can be posed
in physical and mathematical terms allows them to be carefully studied
through computer simulation. This research considers the tumour scale
in the interest of eventually developing a system-level understanding
of the progression of cancer. Starting with our broad [continuum
physical model](http://localhost/research/continuum-biophysics/) for
studying the growth and remodelling of biological tissue, we have
developed an initial model [tuned to the bio-chemo-mechanics of tumour
growth](http://dx.doi.org/10.1088/0953-8984/22/19/194122).

{{< figure src="http://localhost/files/images/research/grad-school/continuum-physics/tumour-growth/growing-tumour.gif" title="The asymmetric growth of a constrained solid tumour." >}}

Cancer cells, like all other cells, store chemical free energy as ATP,
which they synthesize by consuming glucose in the presence of
oxygen. The cells use this chemical free energy for proliferation,
migration and intercellular or cell-ECM (extra-cellular matrix)
mechanical interactions. Both glucose and oxygen must be transported
over the length scale of the tumor. Motivated by this, our model
incorporates (a) cell proliferation, (b) cell motility, \(c) metabolism
by which the cells consume glucose and oxygen and create by-products,
(d) mechanical interactions between cancer cells, the ECM and
surrounding tissues and (e) mass transport of chemical species to and
through the tumor.

{{< figure src="http://localhost/files/images/research/grad-school/continuum-physics/tumour-growth/heterogeneous-traction.png" title="Heterogeneous cell-ECM traction due to a non-uniform distribution of tumour cells." >}}

Free energy, the energy available to do useful work, is consumed or
created in each of these processes and thus provides a universal
measure for comparison between them, and of their variation with time
and physical state of the tumour. We have used our model to compute an
initial estimate of the free energy rates associated with all the
above bio-chemo-mechanical processes that influence the tumour’s
progression. Knowing these free energy rates will give cancer
biologists a quantitative measure to compare (a) the influences of
bio-chemo and mechanical processes regulating tumour growth, and (b)
the phenotypic differences e.g., the proliferation rates versus
migration rates of comparable cancer cell types or cell lines. New
therapies may emerge by drugs targeting weaknesses so revealed.
