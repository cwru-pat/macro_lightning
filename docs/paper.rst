====================================================================
Paper : Straight Lightning as a Signature of Macroscopic Dark Matter
====================================================================

:Author: Nathaniel Starkman, Harrison Winch
:Author: Jagjit Singh Sidhu, Glenn Starkman

.. role:: raw-latex(raw)
   :format: latex
..

.. raw:: latex

   \email{nathaniel.starkman@mail.utoronto.ca,\newline harrison.winch@mail.utoronto.ca}

.. raw:: latex

   \email{jxs1325@case.edu, gds6@case.edu}

.. raw:: latex

   \affiliation{Physics Department/CERCA/ISO Case Western Reserve University
   Cleveland, Ohio 44106-7079, USA}

.. raw:: latex

   \preprint{APS/123-QED}

.. raw:: latex

   \maketitle

.. _sec:introduction:

Introduction
============

Assuming General Relativity is the correct theory of gravity on all
scales, there is considerable evidence for dark matter
:raw-latex:`\cite{Tanabashi2018}`. Macroscopic dark matter (macros) is a
broad class of dark-matter candidates that represents an alternative to
conventional particle dark matter with wide ranges of masses :math:`M_x`
and cross sections :math:`\sigma_x` that could still provide all of the
dark matter. Macros typically refer to a broad family of composite dark
matter models arising from some early-universe phase transition, often
composed of strange quark matter.

Of particular interest would be macros of approximately nuclear density
satisfying

.. math::

   \label{eq:macro_density}
           \sigma_x \approx 2\times 10^{-10} \left(\frac{M_x}{g}\right)^{\frac{2}{3}} [\rm{cm}^2]\,,

as several models for macros describe potential candidates with
approximately that density. The idea that macros could be formed
entirely within the Standard Model was originally proposed by
:raw-latex:`\citet{Witten1984}` in the context of a first-order QCD
phase transition. Subsequently :raw-latex:`\citep{Lynn1990, Lynn2010}`
described a more realistic model for Standard-Model macros as bound
states of nucleons with significant strangeness. Nelson
:raw-latex:`\cite{Nelson1990iu}` studied the formation of nuggets of
strange-baryon matter during a second QCD phase transition – from a
kaon-condensate phase to the ordinary phase. Others have considered
non-Standard-Model versions of such objects and their formation
:raw-latex:`\cite{Zhitnitsky2003}`.

Some of us, working with colleagues, have recently explored which
regions of macro parameter space remain unprobed
:raw-latex:`\cite{jacobs2015macro, jacobs2015resonant, Sidhu2019death, Sidhu2019bolide, Sidhu2020reconsider}`.
A longstanding constraint comes from examination of a slab of ancient
mica for tracks that would have been left by the passage of a macro
moving at the typical speed of dark matter in the Galaxy. This was used
to rule out macros of :math:`M_x \leq 55\,`\ g for a wide range of cross
sections (see
:raw-latex:`\cite{Price1988ge, DeRujula1984axn, jacobs2015macro}`).
Various microlensing experiments have constrained the dark-matter
fraction for masses :math:`M_x \geq 10^{23}\,`\ g
:raw-latex:`\cite{Alcock2001, Griest2013, Tisserand2007, Carr2010,Niikura2019}`.
:raw-latex:`\citeauthor{Wilkinson2014angular}`
:raw-latex:`\citep{Wilkinson2014angular}` utilized the full Boltzmann
formalism to obtain constraints from macro-photon elastic scattering
using the first year release of Planck data. More recently, the
existence of massive white dwarfs was used to constrain a significant
region of macro parameter space :raw-latex:`\cite{Graham2018}` (as
revisited and extended by :raw-latex:`\cite{Sidhu2020reconsider}`). The
region of parameter space for which macros produce injuries similar to a
gunshot wound was recently constrained by historical analysis of a
well-monitored segment of the population
:raw-latex:`\cite{Sidhu2019death}`.

The parameter space for electrically charged macros, with the macro
charge as an additional free parameter, was recently constrained
:raw-latex:`\cite{Sidhu2020charge}` based on a variety of terrestrial,
astrophysical and cosmological measurements. The parameter space for
antimatter macros was constrained by :raw-latex:`\cite{Sidhu2020anti}`
using arguments analogous to those cited above for macros.

More work has been done recently to identify additional ways to probe
macro parameter space. With colleagues, some of us have proposed
:raw-latex:`\cite{Sidhu2018auv}` using current Fluorescence Detectors
that are designed to study High Energy Cosmic Rays, such as those of the
Pierre Auger Observatory :raw-latex:`\cite{Abraham2010}`. Separately, we
have suggested :raw-latex:`\cite{Sidhu2019granite}` that, for
appropriate :math:`M_x` and :math:`\sigma_x`, the passage of a macro
through granite would form long tracks of melted and re-solidified rock
that would be distinguishable from the surrounding granite. A
citizen-science search for such tracks in commercially available granite
slabs is planned to begin through the Zooniverse website sometime later
this year. We have also identified the region of parameter space
excluded by the null observation of fast-moving meteors ("bolides"),
which should have been produced by sufficiently large and fast-moving
macros and observed by either of two bolide-observing networks
:raw-latex:`\cite{Sidhu2019bolide}`. We determined the region of
parameter space that will be probed by planned expansion of the network
that is still operating.

In these works concerning non-anti-baryonic neutral macros, energy is
considered to be deposited in matter by the passing macro primarily
through elastic scattering. In this case, the energy deposited by a
macro transiting the atmosphere

.. math::

   \label{eq:dedx}
           \frac{dE}{dx} = \sigma_x \rho v_x^2\,,

where :math:`\rho \sim 1\,` kg m\ :math:`^{-3}` is the density of the
atmosphere at ground level, :math:`\sigma_x` is the geometric
cross-section of the macro, while :math:`v_x` is its speed.

The speed of a macro traveling through the atmosphere is thus expected
to evolve as

.. math::

   \label{eq:atmo_velocity}
           v(x) = v_{0} e^{-\langle \rho \Delta\rangle \sigma_x/{M_x}}\,,

where :math:`\langle \rho \Delta\rangle` is the integrated column
density traversed along the macro trajectory from the point of entry to
the location :math:`x`. This will determine the maximum reduced
cross-section :math:`\sigma_x/M_x` expected to deposit sufficient energy
to produce an observable signal without being slowed excessively. In
previous works e.g. :raw-latex:`\cite{Sidhu2019death, Sidhu2019bolide}`,
this limiting value for macros that are interacting at the bottom of the
atmosphere was found to be
:math:`\frac{\sigma_x}{M_x} \sim 10^{-4}\,`\ cm\ :math:`^2`\ g\ :math:`^{-1}\,`.
This will serve as an upper bound for all Earth-based projections
derived in this manuscript.

As in previous work, we consider macros of a single mass and
cross-section, even though a broad mass distribution is a reasonable
possibility in the context of a composite dark-matter candidate.

In this manuscript, we consider the possibility that a macro transiting
the atmosphere during the appropriate atmospheric conditions (e.g. a
thunderstorm) would initiate an unusual, extremely straight lightning
strike. We identify the range of macro parameter space over which that
is likely, and consider the possibility that the one documented
observation of an abnormally straight lightning strike was triggered by
the passage of a macro. We determine the range of parameter space that
could be probed by monitoring the Earth, as well as by observing the
atmospheres of Jovian planets, which could probe higher macro masses
than any terrestrial detector. The rest of this paper is organized as
follows. In Section II we present a review of our current understanding
of lightning initiation. In Section III, we discuss the formation of a
plasma trail by a passing macro. In Section IV, we calculate the rates
of a macro induced signal. In Section V, we discuss the formation of
straight lightning induced by the passage of a macro through the
atmosphere based on the observation of rocket-induced lightning
:raw-latex:`\cite{Wang1999, rocket2012, Hill2012, Hill2013}`. In Section
VI, we discuss the observation of a bright UV signal produced by the
passage of a macro through a Jovian planet atmosphere. We conclude, with
some discussion in Section VII.

.. _sec:a_lightning_review:

A Lightning Review
==================

While the detailed physics of lightning remains a matter of
investigation, the broad strokes are well understood. Lightning is an
electrical discharge between two regions of large potential difference.
Lightning is classified by the start-end point pair, and sub-classified
by the order and charges of those points. For instance, the main classes
of lightning are intra-cloud, inter-cloud, cloud-air, and cloud-ground.
All except cloud-air lightning may occur in reverse order, like
ground-to-cloud or cloud-to-ground. We restrict ourselves to
cloud-ground strikes, which are the easiest to observe. The description
that follows is almost entirely drawn from the excellent review by Dwyer
and Uman :raw-latex:`\citep{DwyerUman2014}`.

A lightning strike is actually two events: first, an ion channel is
created from point A to point B, and second, energy flows from B to A.
The latter is the lightning and is the luminous signal of the former.
The creation of the ion channel is a discrete stochastic process of the
formation of “stepped leaders," where a cylindrical atmospheric volume –
“step" – is ionized. This process is known to take at most
:math:`1 \; \mu\rm{s}`. These steps are short compared to the
cloud-ground distance – cloud-level steps are just
:math:`\sim10 \rm{m}`, while ground-level steps near :math:`50 m`. The
time between steps ranges from :math:`\sim50 \mu\rm{s}` at cloud-level
to :math:`\sim10 \mu\rm{s}` at ground. The ion channel persists long
after the leader takes its next “step".

The propagation direction and charge type of the leader determines the
lightning sub-class. For cloud-ground strikes there are four varieties:
downward / upward - negative / positive. Thunder clouds are negatively
charged at the bottom and positively charged on top. Flat ground has
regions of differently signed net charge. In a downward-positive strike
a positively charged leader starts near cloud top and steps down to a
negatively charged region of ground, 10 km below. For all cloud-ground
strikes the full channel creation process takes approximately :math:`20`
ms.

The typical stepped leader has 5 Coulombs of free electrical charge, or
:math:`\sim10^{-3} \, \rm{C/m}`. While the leader has a luminous
diameter between 1 and 10 m, it is thought to have a conducting core of
plasma a few centimeters in diameter. This core acts as a conducting
channel, and it is through it that much of the energy flows.

.. _sec:macro_induced_lightning:

Macro-induced Lightning
=======================

In most artificially triggered lightning experiments, such as those at
the International Center for Lightning Research and Testing (ICLRT)
:raw-latex:`\cite{Hill2012, Hill2013}`, a rocket trailing a grounded
triggering wire is launched when the quasi-static electric field at
ground exceeds :math:`E_{threshold} = 5\,`\ kV m\ :math:`^{-1}` and the
flash rate becomes relatively low. In about half of all such launches,
an initial stage is successfully triggered, consisting of a sustained
upward positive leader typically several kilometers in length followed
by an initial continuous current. Often, the initial stage is followed
by one or more leader/return stroke sequences, similar to subsequent
strokes in natural lightning.

The formation of a lightning strike caused by the passage of a macro
through the atmosphere is dependent on the formation of a plasma trail
produced by the macro scattering elastically off the atoms and
molecules. This trail would serve as the channel through which the
charge is transferred in a lightning strike. The plasma trails produced
by the macro are similar to the trailing grounded wires as both are
sources of free electrons.

We describe in this section the conditions under which a macro produces
a sufficiently large and long-lived plasma channel. We then identify the
the ways in which macro-induced lightning differs from natural
lightning, in particular in being extremely straight, and so can be used
as a signature to search for macros. Finally we discuss the one
photographically documented straight lightning bolt.

.. _sub:macro_induced_plasma_channels:

Forming Plasma Channels
-----------------------

We review the key quantities about this plasma first; we refer the
reader to reference :raw-latex:`\cite{Sidhu2018auv}` for more details.

Following the work of :raw-latex:`\citeauthor{Cyncynates2016}`
:raw-latex:`\cite{Cyncynates2016}`, we propagate the initial energy
deposition by the macro outward radially away from that trajectory using
the heat equation. Ignoring radiative cooling, the temperature field
after some time :math:`t` is

.. math::

   \label{eq:temperature_field}
               T(r,t) = \frac{\sigma_{x} v_x^2}{4\pi \alpha c_p}\frac{e^{-\frac{r^2}{4t\alpha}}}{t},

where
:math:`\alpha \approx 10^{-4}\,`\ m\ :math:`^2\,`\ s\ :math:`^{-1}`\ exp\ :math:`(D/10`\ km\ :math:`)`
is the thermal diffusivity of the air, and :math:`c_p \approx 25` kJ
kg\ :math:`^{-1}` K\ :math:`^{-1}` is the specific heat of the air
:raw-latex:`\cite{Capitelli2000}` (The specific heat varies around a
mean of :math:`\sim25\,`\ kJ kg\ :math:`^{-1}\,`\ K\ :math:`^{-1}` for
temperatures between :math:`10^4\,`\ K and :math:`10^5\,`\ K).

We invert `[eq:temperature_field] <#eq:temperature_field>`__ to obtain
:math:`\pi r_I(t)^2`, the area at time :math:`t` that has reached a
particular state of ionization :math:`I` characterized by the
appropriate ionization temperature :math:`T_I`. We do this by setting
:math:`T(r,t) = T_I \approx 5\times10^4`\ K
:raw-latex:`\cite{EisazadehFar2011}`, sufficient to ionize the 2p
electrons of N and O. This area is given by

.. math::

   \label{eq:ionization_crosssection}
               \pi r_I(t)^2 = 4\pi\alpha t\log\left(\frac{\sigma_{x} v_x^2}{4\pi \alpha t c_p T_I}\right) .

According to
`[eq:ionization_crosssection] <#eq:ionization_crosssection>`__, after
the macro passes, the size of the ionized region grows to a maximum of
:math:`r_I^{\rm max}=4\pi\alpha t_{I}^{\rm max}` at time

.. math::

   \label{eq:cooling_time}
               t_{I}^{\rm max}=\frac{\sigma_x v_x^2}{4\pi e \alpha c_p T_I} \approx 6\,s\left(\frac{\sigma_x}{cm^2}\right)\left(\frac{v_x}{250kms^{-1}}\right)^2e^{-\frac{D}{10 km}}\,.

It then shrinks back to :math:`0` at :math:`t_I^0=e~t_{I}^{\rm max}`.

.. _sub:inducing_lightning:

Inducing Lightning
------------------

In order to initiate lightning, we need to create charged filaments with
linear charged densities sufficient to seed a leader. In natural
lightning, the leaders have :raw-latex:`\citep[][p. 152]{DwyerUman2014}`
a linear electron density
:math:`\lambda_e^{\rm natural}\simeq 6\times 10^{13} cm^{-1}`. By
comparison, within the plasma channel at time :math:`t_I^{\rm max}` the
linear free-electron density will be

.. math:: \lambda_e^{\rm macro} \simeq \pi (r_I^{\rm max})^2 n_a f_e

where :math:`n_a` is the number density of atoms in air, and
:math:`f_e` is their ionization level. Taking :math:`f_e\simeq0.5`
appropriately accounts for the fact that the 2p electrons of N and O are
ionized at :math:`T_I` but the 1s and 2s electrons are not.

Knowing that each luminous step leader propagates
:raw-latex:`\cite{DwyerUman2014}` in at most :math:`1\mu{s}`, followed
by a pause of between :math:`50\mu{s}` (at high altitude) and
:math:`10\mu{s}` (near the ground) between leaders, We therefore require
that

.. math::

   \label{eq:tI0min}
               t_{I}^0 \geq 1\mu{s} \quad \implies \quad \sigma_x > 6\times 10^{-8}cm^2\,,

and that the linear charge density in the macro-induced plasma trail

.. math::

   \label{eq:lambdaemin}
               \lambda_e^{\rm macro}\geq \lambda_e^{\rm natural}
               \quad \implies \quad \sigma_x >  10^{-8}cm^2 \,.

Equation `[eq:tI0min] <#eq:tI0min>`__ is more stringent; however,
:math:`1\mu{s}` is an upper bound for the time-scale over which each
step leader forms, and represents propagation along the step leader at
approximately :math:`0.05c`. Positive return strokes travel
:raw-latex:`\cite{Idone1987}` at :math:`c/3`, which may be a more
realistic estimate of the propagation speed. This would drop the minimum
applicable :math:`\sigma_x` to :math:`10^{-8}cm^2`. Nevertheless we
quote our accessible macro parameter space using the more restrictive
:math:`\sigma_x \geq 6\times 10^{-8}cm^2`.

.. _sec:signatures_of_macro_induced_lightning:

Signatures of Macro-induced Lightning
-------------------------------------

Our macro-induced lightning initiation model differs from
:raw-latex:`\citet{DwyerUman2014}` in a few important regards. First, as
the macro trail acts as a “pre-leader", the channel process is not
stochastic but deterministic. Second, since the macro constantly creates
the plasma channel the leader propagates continuously along this
channel. The mode of the macro velocity distribution, 250 km/s, is near
exactly the propagation velocity of the leaders (:math:`200\,` km
s\ :math:`^{-1}`), when including the step time delay. However, the
propagation of the leader within each step is known to take at most
:math:`1\mu`\ s, and therefore to be at a velocity of at least
:math:`10^4\,` km s\ :math:`^{-1}`, and may perhaps be as much as the
:math:`c/3` measured for positive return strokes. So as the macro
continuously creates a plasma trail the leader will propagate at this
same velocity. Thus in macro-induced lightning leaders are continuous,
not discrete.

.. raw:: latex

   \centering

.. figure:: _static/macro_schematic.pdf
   :scale: 100 %
   :alt: *(Not to scale)*

   *(Not to scale)* Graphic representation of macro plasma channel
   seeding continuous leader. Macro plasma trail expands to maximum
   radius :math:`R_{I}^{\rm{max}}` before cooling. As
   :math:`v_{\rm{step}} < v_{\rm{macro}} < v_{\rm{leader}}`, the
   lightning-leader takes no “steps", instead propagating continuously
   with the macro trail.

[fig:macro_graphic]

This offers a few testable predictions: the leader process produces no
light pulses during steps, the RF and X-ray signatures of the leader
steps are similarly different. The most conspicuous prediction is that
macros source abnormally straight lightning compared to the typical
lightning strikes observed.

We note some caveats. First, the stepped leader model does not apply for
the last tens of meters as the ground emits an upward propagating
stepped leader which will connect to the downward propagating plasma
channel. Moreover, for macros moving slower than :math:`250\,`\ km/s,
the lightning is expected to be jagged like regular lightning as the
stepped leader would eventually overtake the macro trail. For macros
moving significantly faster than :math:`250\,`\ km/s the lightning is
expected to be straight the entire pathway from cloud to ground as the
ground will not have time to emit or significantly propagate its own
stepped leader.

Since macros are expected to move according to a Maxwellian velocity
distribution in a frame co-moving with the Galaxy,

.. math::

   \label{eq:maxwellian}
               f_{MB}(v_x) = 
                   \frac{4\pi v_x^2}
                   {\left({\pi v_{vir}^2}\right)^{3/2}}~
                   e^{-\left(\frac{v_x}{v_{vir}}\right)^2},

where :math:`v_{vir} \approx 250~ \text{km s}^{-1}`  [1]_. and taking
the relative motion between the macro and Earth into account, we find
that :math:`71\%` of all macros in the distribution will be moving at at
least 250 km/s.

Additionally, we expect that the mechanism outlined here may not hold
true if the macro comes in at a trajectory that is mostly parallel to
the ground. There is a critical angle at which a macro trail is
sufficiently misaligned from the storm electric field such that the
electric field induces offshoot lightning channels, obviating the
straight-lightning prediction. This is poorly constrained because plasma
channels in air are analogous to wires surrounded by an insulator. The
breakdown voltage is highly dependant on atmospheric properties such as
moisture and particulate content, etc. Despite this, order of magnitude
calculations suggest the critical angle is approximately unity. As
example, considering a cloud-to-ground macro-induced plasma channel for
a critical angle of 30\ :math:`\degree` from a perfectly perpendicular
trajectory, :math:`25\%` of all macro trajectories would fall in this
cone. We consider this when calculating the maximum mass that could be
probed by a careful monitoring of thunderstorms on Earth.

.. _sub:staying_straight:

Staying Straight
----------------

Although a macro creates a straight plasma channel, at least two
mechanisms will spoil that: the :math:`m=1` MHD instability on small
scales and wind shear on large scales. Of these only the wind-induced
non-linearity is expected to be observable by commercial-grade
equipment. We discuss both.

There have been a number of studies investigating how to artificially
induce lightning strikes through laser-generated plasma channels
:raw-latex:`\citep[see][]{Kasparian2008}`. Though no strikes have yet
been directly triggered due to technical limitations in producing a
continuous ground-to-cloud channel. Instead, an informative analogue to
macro-induced lightning is lightning induced by charged particles from
the IVY-MIKE 1952 nuclear explosion test on Enewetak Atoll
:raw-latex:`\citep{IVY-MIKE1987}`.

In laboratory tests to simulate the IVY-MIKE lightning, laser-guided
electric discharges were used to create a :math:`{\sim 1}` m straight
plasma filament, radius :math:`R_f\lesssim 1` cm, within a reduced
density channel, radius :math:`R_d \lesssim 2` cm
:raw-latex:`\citep[][fig. 6]{IVY-MIKE1987}`. On timescales exceeding
:math:`40 \, \mu s`, the :math:`m=1` magnetohydrodynamic (MHD) mode
kinks the central filament, with perturbations of amplitude :math:`R_e`
(:math:`R_f < R_e < R_d`) and growing wavelength :math:`\lambda`.
:math:`R_f`,  :math:`R_e` and :math:`R_d` grow sub-linearly
:raw-latex:`\citep[][fig. 9]{IVY-MIKE1987}`. Extrapolating to 20 ms
(ground-to-cloud time), the radius of the reduced density channel is
:math:`R_d<3m`. After 1 ms, the central filament kink radius :math:`R_e`
has nearly plateaued at 10 cm, while the filament :math:`R_f` itself is
stable at 1-2 cm. The :math:`m=1` mode wavelength is
:math:`\lambda\simeq4 m`. These lab-measurements of :math:`R_d` are
consistent with observed lightning. While the amplitude and wavelength
of the kink mode explain why it has yet to be observed. The :math:`m=1`
instability should not alter the apparently straight lightning path,
which is observed as the reduced density channel.

Wind shear is not expected to introduce significant long wavelength
deviations from straightness. The typical timescale of cloud-to-ground
ion channel formation is :math:`{\approx 20}` ms. The return stroke, aka
the first lightning strike :raw-latex:`\citep{DwyerUman2014}` occurs
directly following the ion channel creation and propagates at
:math:`c/3` :raw-latex:`\citep{Idone1987}`. At a wind speed of
:math:`{\approx 20}` m/s :raw-latex:`\citep{Choi2004}`, high for the
typical thunderstorm, local regions of the plasma channel can be
transported by :math:`{\sim 0.5}` m. Even if wind shear transports
neighboring plasma channel components in opposite directions, the
observed deviation from a straight strike is just :math:`1`\ m. Repeated
strikes are generally separated by :math:`{\sim 50}` ms, contributing a
further :math:`{\sim 2}` m deviation of the channel. In actuality,
repeated strokes can be distinguished by any camera with :math:`>30`
fps. These effects should not contribute significantly on the first
strike and a macro-induced lightning track is predicted to be nearly
perfectly straight.

.. _sec:macro_search_and_constraints:

Macro Search and Constraints
============================

Using the distribution `[eq:maxwellian] <#eq:maxwellian>`__, transformed
to the solar frame :raw-latex:`\citep{Freese2013}`, the macro flux on a
planet would be given by,

.. math::

   \label{eq:planet_macro_flux}
           F_{x} = \frac{\rho_{x,0}}{M_{x}} \int v_{x} f_{MB,SS} dv_x,

where :math:`\rho_{x,0} = 5 \times 10^{-25}` g cm\ :math:`^{-3}` is the
local DM density :raw-latex:`\cite{Bovy2012}`, :math:`M_{x}` is the mass
of the macro and the integral accounts for the velocity distribution of
all macros, and :math:`f_{MB,SS}` is the Maxwell Boltzmann distribution
in the Solar System frame. With this, we calculate the estimated rate of
macro-induced lightning strikes

.. math::

   \label{eq:macro_lightning_rate}
           n_{ml} = \frac{\rho_{x,0} \pi R_{O}^2 f_{TS} f_{LE}}{M_{x}}\int v_{x} f_{MB,SS} dv_x\,,

where :math:`R_{O}` is the planet’s radius, :math:`f_{TS}` is the
fraction of planet’s surface currently experiencing a thunderstorm, and
:math:`f_{LE}` is the fraction of macro strikes in thunderstorms that
actually lead to an observable event. For the range of cross-sections of
interest, :math:`f_{LE}\simeq1`.

.. _sub:straightest_observed_lightning:

Straightest Observed Lightning
------------------------------

We conducted a search in the physics literature and publicly available
new sources for reports of anomalously straight lightning. The most
promising candidate was reported in Mutare, Zimbabwe on 15 February 2015
:raw-latex:`\cite{Zimbabwe}` and recorded at 30 frames per second with a
Panasonic Lumix DMC-TZ10 compact camera in scene mode. The observed
lightning strike is a cloud-ground strike with no secondary strikes. The
maximum projected deviations from perfect linearity are of order a few
diameters. As the thickness of a beam of lightning is between 1m and 10m
(and does not depend significantly on the considered macro parameter
space), even this straight lightning strike is mostly likely not
straight enough to have been induced by a macro.

The expected signature from a macro-induced lightning strike would be
very unique. This presents, in theory, a straightforward way to search
for macros by looking for macro-induced lightning strikes, and to place
constraints on macros if no such strikes are observed.

.. figure:: _static/lightning-straight-2-15-2015-Mutare-Zimbabwe-Peter-Lowenstein.gif
   :scale: 50 %
   :alt: straight lightning observed in Zimbabwe

   Lightning observed in Mutare, Zimbabwe on 15 February 2015 and recorded at 30 frames per second with a Panasonic Lumix DMC-TZ10 compact camera in scene mode. The observed lightning strike is a cloud-ground strike with no secondary strikes.


.. _sub:macro_constraints_on_earth:

Macro Constraints
-----------------

To place constraints on macros from the non-observation of any straight
lightning strikes, we note that the passage of a macro through the area
covered by a thunderstorm is a Poisson process. Thus the probability of
:math:`n` passages over a given exposure time, :math:`\Delta t`,
:math:`P(n)` follows the distribution

.. math::

   \label{eq:poisson}
               P(n) = \frac{\left({n_{ml} \Delta t}\right)^n}{n!} e^{-n_{ml} \Delta t}\,.

The continued failure to observe a macro-induced lightning strike would
allow us to conclude that :math:`n_{ml}\Delta t<3` at 95\ :math:`\%`
confidence level.

To calculate the expected macro-induced lightning rate on Earth, we take
:math:`R_{O} = \bar{R_{\bigoplus}} = 6 \times 10^8` cm. At any given
time Earth experiences approximately 2,000 thunderstorms
:raw-latex:`\citep{NatGeo}`, with an average :math:`20` km in diameter,
giving :math:`f_{TS}\simeq 0.3\%`.

With these assumptions, and should we observe 0 very straight lightning
strikes in a year, we could place an upper bound on the mass of a macro
up to :math:`M_x \sim 10^6\,`\ g for
:math:`\sigma_x\gtrapprox6\times10^{-8}{\rm cm}^2`. The exact
projections are shown in Figure 2. It is of particular significance that
this method is sensitive to probing the nuclear density line.

We calculate these constraints with the simplification of a
gravitational infall velocity determined only by the mass of the sun and
Earth, not accounting for the Earth’s orbital velocity. This only
noticeably affects the small lower right plateau in the constraint curve
of `[fig:constraints] <#fig:constraints>`__, which is determined by this
velocity.

To achieve these constraints requires more detailed observations /
reporting of lightning as a significant fraction of lightning is not
observed, and only a fraction of those events are recorded. Fortunately,
lightning strikes are heavily concentrated over land
:raw-latex:`\citep{Christian2003}`, increasing the possibility of
establishing a dedicated monitoring program. It also increases the
probability of reporting by casual observers, since nearly straight
lightning strikes are rare enough to generate press (see
:raw-latex:`\cite{Zimbabwe}`).

For e.g. :math:`M_x = 100\,`\ g over the range of cross-sections of
interest, the macros can make up no more than :math:`2\times 10^{-3}` of
the dark matter :raw-latex:`\cite{Sidhu2019death}`. Thus, we would
expect a macro-induced lightning rate of :math:`\sim 10^{-6}`
s\ :math:`^{-1}`, combining this maximum fraction with the rate
`[eq:macro_lightning_rate] <#eq:macro_lightning_rate>`__. This is
already much lower than the actual observed rate of lightning strikes on
Earth, which is on order of 50 to :math:`100` s\ :math:`^{-1}`
:raw-latex:`\citep{Mackerras1998}`. This implies that we cannot
significantly constrain macros as dark matter through lightning rates
alone, as the macro-induced lightning signal would always be
significantly outnumbered by the rate of regular lightning strikes.
However, as discussed in Section
`3.3 <#sec:signatures_of_macro_induced_lightning>`__, the lightning
strikes induced by macros are expected to be significantly straighter
than regular lightning strikes. Thus, we expect to see straight
lightning caused by macros regardless of whether the macros populate a
part of parameter space where they can or cannot contribute all the dark
matter.

.. _sec:jovian_bolides:

Jupiter
=======

Given its size relative to Earth, a search for macros using Jupiter (or
another gas giant planet) as the target holds great potential for
exploring larger macro masses than can be explored using Earth as the
target. (Although on Earth we have the advantage of being able to search
for the effects of macros on targets like rocks that have "integrated"
for extremely long exposure times :raw-latex:`\cite{Sidhu2019granite}`).

A potential signal is the production of straight lightning in the Jovian
atmosphere as discussed above for Earth’s atmosphere. Lightning has been
observed near the Jovian poles by every passing satellite. Earlier
mysteries as to its origins have recently been clarified based on
observations from the Juno mission :raw-latex:`\cite{Brown2018}`, and it
is now understood to be be described by essentially the same physics as
terrestrial lightning.

The surface area of Jupiter is 125 times that of Earth, suggesting that
it is a potentially valuable target to search for macro-induced
fluorescence or macro-induced lightning. However, it is currently
unclear why lightning does not form over the entire surface of Jupiter
but only the poles. This could reduce the region of parameter space that
could be probed through this method. However, we shade, in Figure 2, the
region of parameter space that could be probed assuming that lightning
occurs only over :math:`10\%` of the surface of Jupiter, which is a
likely underestimate, and assuming lightning is identical on Jupiter
compared to the Earth. We defer detailed discussion of both points for a
future paper once more is known about lightning on Jupiter.

.. figure:: _static/lightningconstraints.pdf
   :scale: 100 %
   :alt: *(Not to scale)*

   Figure 1 of \cite{Sidhu2020reconsider} with the updated constraints discussed in the text. Earth lightning projections are in black hatching and Jupiter lightning projections are in cyan hatching. The lower right right constraint curves up because the number density of macros decreases with increased mass which requires a larger fraction of the velocity distribution. The step in the lower right is the average observed minimum macro velocity due to gravitational infall.
   Objects within the bottom-right corner are excluded as they are denser than black holes of the same mass. The grey region is ruled out from structure formation \cite{Wilkinson2014angular}; the yellow from mica observation \cite{DeRujula1984axn, Price1988ge};  the light purple from superbursts in neutron stars; the light blue from WDs becoming supernovae (\cite{Graham2018} as revised in \cite{Sidhu2020reconsider});  the red from a lack of human injuries or deaths \cite{Sidhu2019death}; the green from a lack of fast-moving bolides \cite{Sidhu2019bolide}; the maroon from a lack of microlensing events \cite{Niikura2019, Alcock2001, Tisserand2007, Carr2010, Griest2013}. Solid colors denotes verified constraints, hatching for potential constraints.

.. raw:: latex

   \medskip

.. _sec:conclusion:

Conclusion
==========

In this manuscript, we have proposed that macros could result in the
formation of distinctive, abnormally straight lightning that, to our
knowledge, has not been documented on Earth. This could serve as the
basis for a high-sensitivity search for macros of higher mass and lower
cross section than other methods that have been proposed. We also
proposed using lightning on Jupiter to probe a much larger region of
parameter space, although a detailed consideration of this idea must
still be performed.

.. _sec:acknowledgements:

Acknowledgements
================

This work was partially supported by Department of Energy grant
de-sc0009946 to the particle astrophysics theory group at CWRU.

We acknowledge the support of the Natural Sciences and Engineering
Research Council of Canada (NSERC) Canadian Graduate Scholarships -
Master’s Program, [funding reference number 542364 / 2019 (Nathaniel
Starkman), 542579 / 2019 (Harrison Winch)]

.. raw:: latex

   \bibliographystyle{apsrev4-1}

.. [1]
   This is the distribution of macro velocities in a non-orbiting frame
   moving with the Galaxy. When considering the velocity of macros
   impacting the atmosphere, `[eq:maxwellian] <#eq:maxwellian>`__ is
   modified by the motion of the Sun and Earth in that frame, and by the
   Sun’s and Earth’s gravitational potential. We have taken into account
   these effects (as explained in :raw-latex:`\cite{Freese2013}`),
   except the negligible effect of Earth’s gravitational potential.

   Recent hydrodynamical simulations of Milky Way-like galaxies
   including baryons, which have a non-negligible effect on the dark
   matter distribution in the Solar neighbourhood
   :raw-latex:`\cite{Tanabashi2018}` have been performed to determine
   the correctness of assuming a Maxwellian distribution. These
   simulations find that the velocity distributions are indeed close to
   Maxwellian.As discussed previously, macros are expected to move
   according to `[eq:maxwellian] <#eq:maxwellian>`__. Taking this
   minimum speed requirement into account, we find that :math:`71\%` of
   all macros in the distribution will be moving at at least
   :math:`250\,`\ km/s.

