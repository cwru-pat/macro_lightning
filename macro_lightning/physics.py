# -*- coding: utf-8 -*-

"""Physics Functions."""


__all__ = [
    "CMB",
    "nuclear_density",
    "black_hole",
    "atomic_density",
    "KeplerTop",
    "LMCTop",
    "twobody_vesc",
    "multibody_vesc",
    "calculate_Mx",
    "calculate_Sx",
    "calculate_Mx_and_Sx",
]


##############################################################################
# IMPORTS

# BUILT-IN

# BUILT-IN
import functools
import itertools
import typing as T

# THIRD PARTY
import astropy.units as u
import numpy as np
from astropy.utils.decorators import format_doc
from astropy.utils.misc import indent
from tqdm import tqdm

# PROJECT-SPECIFIC
from .utils import as_quantity, qnorm

##############################################################################
# PARAMETERS

_KMS = u.km / u.s

_sqrt2 = np.sqrt(2)


##############################################################################
# CODE
##############################################################################


def CMB(M: T.Sequence) -> T.Sequence:
    r"""CMB bound from Celine Boehm paper.

    Paper considers dark matter elastic scattering effects on the CMB.
    :math:`sigma_x/M_x \geq 4.5e-7` is ruled out.

    """
    return M * 4.5e-7


# /def


# -------------------------------------------------------------------


def nuclear_density(M: T.Sequence) -> T.Sequence:
    """Quantity sigma_x(cross-section) for a nuclear density object."""
    volume = 4.0 / 3.0 * np.pi * 3.6e14
    out = np.pi * np.power(M / volume, 2.0 / 3)
    return out


# /def


# -------------------------------------------------------------------


def black_hole(M: T.Sequence) -> T.Sequence:
    """Cross section by mass satisfying the Schwarzchild radius."""
    return np.pi * (3e5) ** 2 * (M / (2e33)) ** 2.0


# /def


# -------------------------------------------------------------------


def atomic_density(M: T.Sequence) -> T.Sequence:
    """Quantity sigma_x(cross-section) for an atomic density object."""
    volume = 4.0 / 3.0 * np.pi * 1e0
    out = np.pi * np.power(M / volume, 2.0 / 3.0)
    return out


# /def


# -------------------------------------------------------------------


def KeplerTop(M: T.Sequence) -> T.Sequence:
    """Microlensing bounds from Kepler."""
    return 1e-6 * M


# /def


# -------------------------------------------------------------------


def LMCTop(M: T.Sequence) -> T.Sequence:
    """Microlensing bounds from observation of the LMC."""
    return 1e-4 * M


# /def

# -------------------------------------------------------------------


@u.quantity_input(vx="speed", vbin="speed", vvir="speed")
def f_BM_bin(vx, vbin, vvir):
    """Equation 3 of [1]_, binned.

    Parameters
    ----------
    vx : |Quantity|
        With physical type "speed"
    vvir : |Quantity|
        The virial velocity
        With physical type "speed"

    Returns
    -------
    |Quantity|
        The fraction of macros in the distribution that have some minimum
        velocity after performing the integral (4) in [1]_;
        We iterate over a wide range of velocities.

    References
    ----------
    .. [1] J.  S.  Sidhu  and  G.  Starkman,  Physical  Review  D
         100(2019), 10.1103/physrevd.100.123008.

    .. |Quantity| replace:: :class:`~astropy.units.Quantity`

    """
    norm = (vbin / vvir) ** 3 / np.power(np.pi, 3.0 / 2.0)
    exp = np.exp(-np.square(vx / vvir))

    return norm * exp


# /def


# -------------------------------------------------------------------


def sigma_limit_through_earth(mass: u.Quantity) -> u.Quantity:
    """Calculate the sigma limit for macros passing through the Earth.

    Assuming the PREM model (basically piecewise) model for the Earth.

    .. |Quantity| replace:: `~astropy.units.Quantity`

    Parameters
    ----------
    mass : |Quantity|
        The macro mass

    Returns
    -------
    sigma : |Quantity|
        The limiting cross section

    """
    sigma = (2e-10 * (u.cm ** 2 / u.g)) * mass

    return sigma << u.cm ** 2


# -------------------------------------------------------------------


def _norm_v1_v2(v1: T.Sequence, v2: T.Sequence) -> T.Sequence:
    return np.sqrt(v1 ** 2.0 + v2 ** 2.0)


# /def


_multibody_escape_wikipedia = indent(
    r"""
When escaping a compound system, such as a moon orbiting a planet or a
planet orbiting a sun, a rocket that leaves at escape velocity (ve1) for
the first (orbiting) body, (e.g. Earth) will not travel to an infinite
distance because it needs an even higher speed to escape gravity of the
second body (e.g. the Sun). Near the Earth, the rocket's trajectory will
appear parabolic, but it will still be gravitationally bound to the second
body and will enter an elliptical orbit around that body, with an orbital
speed similar to the first body.

To escape the gravity of the second body once it has escaped the first
body the rocket will need to be traveling at the escape velocity for the
second body (ve2) (at the orbital distance of the first body). However,
when the rocket escapes the first body it will still have the same orbital
speed around the second body that the first body has (vo). So its excess
velocity as it escapes the first body will need to be the difference
between the orbital velocity and the escape velocity. With a circular
orbit, escape velocity is sqrt(2) times the orbital speed. Thus the total
escape velocity vte when leaving one body orbiting a second and seeking to
escape them both is, under simplified assumptions:

.. math::

    v_{te}=\sqrt{(v_{e2} - v_o)^2 + v_{e1}^2}
    = \sqrt{\left(k v_{e2}\right)^2 + v_{e1}^2}

where :math:`k=1−1/\sqrt{2} \sim 0.2929` for circular orbits.
""",
)


@format_doc(None, wikipedia=_multibody_escape_wikipedia)
def twobody_vesc(
    ve1,
    ve2,
    vo: T.Union[None, T.Sequence] = None,
):
    r"""Two-body escape velocity.

    .. |Quantity| replace:: :class:`~astropy.units.Quantity`

    Parameters
    ----------
    ve1, ve2 : |Quantity|
        Escape velocities.
    vo : |Quantity| or `None`, optional
        The orbital velocity of object 1 around object 2.

    Returns
    -------
    vesc : |Quantity|
        The compound escape velocity.

    Examples
    --------
    For a rocket attempting to escape the solar system.

        >>> vesc_earth = 11.186 * u.km / u.s
        >>> vesc_sun_at_earth = 42.1 * u.km / u.s
        >>> twobody_vesc(vesc_earth, vesc_sun_at_earth)
        <Quantity 16.6485836 km / s>

    Notes
    -----
    From `Wikipedia <https://en.wikipedia.org/wiki/Escape_velocity>`_ [1]_:

    {wikipedia}

    References
    ----------
    .. [1] https://en.wikipedia.org/wiki/Escape_velocity

    See Also
    --------
    :func:`~macro_lightning.physics.multibody_vesc`

    """
    vo = vo or ve2 / _sqrt2  # None -> circular

    return np.sqrt(ve1 ** 2 + (ve2 - vo) ** 2)


# /def


@format_doc(None, wikipedia=_multibody_escape_wikipedia)
def multibody_vesc(
    *vescs,
    vo: T.Union[None, T.Sequence] = None,
    accumulate: bool = False,
):
    """Multi-body escape velocity.

    .. |Quantity| replace:: :class:`~astropy.units.Quantity`

    Parameters
    ----------
    *vescs: |Quantity|
        velocities, ordered from 1st to last body.

    vo : list of |Quantity| or None, optional
        The orbital velocity of object vescs[i+1] around object vescs[i].
        if list of quantities, must match vescs in length
        if None (default) then orbits are assumed circular.

    accumulate : bool
        whether to return the accumulative escape velocity for each larger
        system (True), or just the total escape velocity (False, default).

    Returns
    -------
    |Quantity|
        The compound escape velocity
        if `accumulate` False (default) then scalar, else accumulated vector.

    Examples
    --------
    For a rocket attempting to escape the Galaxy.

        >>> vesc_earth = 11.186 * u.km / u.s
        >>> vesc_sun_at_earth = 42.1 * u.km / u.s
        >>> vesc_gal_at_sun = 550 * u.km / u.s
        >>> multibody_vesc(vesc_earth, vesc_sun_at_earth, vesc_gal_at_sun)
        <Quantity 161.94929058 km / s>

    Notes
    -----
    From `Wikipedia <https://en.wikipedia.org/wiki/Escape_velocity>`_ [1]_:

    {wikipedia}

    References
    ----------
    .. [1] https://en.wikipedia.org/wiki/Escape_velocity

    See Also
    --------
    :func:`~macro_lightning.physics.twobody_vesc`

    """
    vs: u.Quantity = as_quantity(vescs)

    if vo is None:
        vs[1:] = vs[1:] * (1 - 1 / np.sqrt(2))
    else:
        vs[1:] = vs[1:] - vo

    if accumulate:
        return as_quantity(itertools.accumulate(vs, _norm_v1_v2))
    else:
        return functools.reduce(_norm_v1_v2, vs)


# /def


# -------------------------------------------------------------------


@u.quantity_input(
    vels="speed",
    vvir="speed",
    vesc="speed",
    vstep="speed",
    vmin="speed",
    vcirc="speed",
)
def calculate_Mx(vels, vvir, vesc, vcirc, vmin, Arho, m_unit=u.g):
    """Calculate Mx.

    Mx is the array of M_x values corresponding to the minimum sigma_x values;
    these two quantities (M_x and sigma_x) are linked through v_x. The
    integral 4 determines vbar, and correspondingly a value for M_x. This
    minimum value in this integral determines  the value corresponding of
    sigma_x and the pair (sigma_x, M_x) is what is plotted in the
    constraints/projections graph.

    Parameters
    ----------
    vels : Sequence
        an array of velocities, treated as along one Cartesian component.
        must be evenly spaced
    vvir : |Quantity|
        virial velocity
    vesc : |Quantity|
        Galactocentric escape velocity
    vcirc : |Quantity|
        Galactocentric circular velocity
    vmin : |Quantity|
        infall velocity of a macro to the Earth.

    Returns
    -------
    Mxs : Sequence
    vbar : |Quantity|
        The value of the integral 4 as we iterate over different values of vx,
        vy and vz.
    Vhold : |Quantity|
        hold accounts for the usage of the minimum speed (not vbar; that is
        relevant to M_x only) when determining the minimum sigma_x  for a
        detectable signal. Vhold Starts high and then is constantly lowered as
        we iterate over different values of vx, vy, vz.

    Other Parameters
    ----------------
    m_unit : :class:`~astropy.units.Unit`

    Notes
    -----
    this integration can be very slow.

    .. |Quantity| replace:: :class:`~astropy.units.Quantity`

    """
    vbar = 0.0 * u.km / u.s
    Vhold = 800.0 * u.km / u.s

    steps = np.diff(vels)
    if not np.allclose(steps[:-1], steps[1:]):  # check all close
        raise ValueError("vels steps unequal in size.")
    else:
        vstep = np.abs(steps[0])  # positive

    Mxs = np.zeros(len(vels) ** 3) * m_unit
    iterator = itertools.product(vels, vels, vels)

    for i, (vx, vy, vz) in tqdm(enumerate(iterator), total=len(Mxs)):
        if qnorm(vx, vy, vz) <= vesc:
            maxwellian = f_BM_bin(qnorm(vx, vy, vz), vbin=vstep, vvir=vvir)
            vrel = qnorm(vmin, vx, vy - vcirc, vz)

            vbar = vbar + vrel * maxwellian  # cumulative

            # the product of the A_{det} and rho_{DM} and T, the integration
            # time, outside the integral in equation of 4 of the bolides
            # paper.
            mx = Arho * vbar

            Mxs[i] = mx

    # update variable
    Vhold = vrel

    # /for

    Mxs = Mxs[Mxs > 0 * m_unit]

    return Mxs, vbar, Vhold


# /def

# -------------------------------------------------------------------


def calculate_Sx(
    vels,
    vesc,
    vhold,
    vcirc,
    vmin,
    minsigma,
    sigma_factor,
    sig_unit=u.cm ** 2,
):
    """Calculate Sx.

    Sx holds the minimum values of sigma_x for a detectable signal.

    Parameters
    ----------
    vels : Sequence
        Array of velocities, treated as along one Cartesian component.
        Must be evenly spaced
    vesc : |Quantity|
        Galactocentric escape velocity
    vhold : |Quantity|
        Vhold accounts for the usage of the minimum speed (not vbar; that is
        relevant to M_x only) when determining the minimum sigma_x  for a
        detectable signal. Vhold Starts high and then is constantly lowered as
        we iterate over different values of vx, vy, vz.
    vcirc : |Quantity|
        Galactocentric circular velocity
    vmin : |Quantity|
        infall velocity of a macro to the Earth.
    minsigma : |Quantity|

    Returns
    -------
    Sxs : Sequence
    vhold : |Quantity|

    Other Parameters
    ----------------
    sig_unit : :class:`~astropy.units.Unit`

    Notes
    -----
    This integration can be slow.

    .. |Quantity| replace:: :class:`~astropy.units.Quantity`

    """
    Sxs = np.zeros(len(vels) ** 3) * sig_unit
    iterator = itertools.product(vels, vels, vels)

    for i, (vx, vy, vz) in tqdm(enumerate(iterator), total=len(Sxs)):
        if qnorm(vx, vy, vz) <= vesc:
            vrel = qnorm(vmin, vx, vy - vcirc, vz)
            if vrel > vhold:
                vrel = vhold
            vhold = vrel  # update vhold   # problem? never reset vhold

            sx = sigma_factor / vrel ** 2
            if sx < minsigma:
                sx = minsigma

            Sxs[i] = sx
    # /for

    Sxs = Sxs[Sxs > 0]

    return Sxs, vhold


# /def


# -------------------------------------------------------------------


def calculate_Mx_and_Sx(
    vels,
    vvir=250 * _KMS,
    vesc=550 * _KMS,
    vcirc=220 * _KMS,
    vmin=42.1 * _KMS,
    Arho=3 * u.g * u.s / u.m,
    *,
    minsigma=6e-8 * u.cm ** 2,
    sigma_factor=None,
    m_unit=u.g,
    sig_unit=u.cm ** 2,
):
    r"""Calculate Mx and Sx.

    Parameters
    ----------
    vels : Sequence
        Array of velocities, treated as along one Cartesian component.
        Must be evenly spaced
    vvir : |Quantity|, optional
        virial velocity
    vesc : |Quantity|, optional
        Galactocentric escape velocity
    vcirc : |Quantity|, optional
        Galactocentric circular velocity
    vmin : |Quantity|, optional
        infall velocity of a macro to the Earth.
    Arho: |Quantity|, optional
        A_{det}*\rho_{DM},
    minsigma : |Quantity|, optional

    Returns
    -------
    Mxs, Sxs : Sequence
    vbar : |Quantity|
    vhold : |Quantity|

    Other Parameters
    ----------------
    minsigma : |Quantity|, optional
    m_unit : :class:`~astropy.units.Unit`, optional
    sig_unit : :class:`~astropy.units.Unit`, optional

    Notes
    -----
    This calculation can be slow.

    .. |Quantity| replace:: :class:`~astropy.units.Quantity`

    """
    Mxs, vbar, Vhold = calculate_Mx(
        vels,
        vvir=vvir,
        vesc=vesc,
        vcirc=vcirc,
        vmin=vmin,
        Arho=Arho,
        m_unit=m_unit,
    )

    Sxs, Vhold = calculate_Sx(
        vels,
        vesc=vesc,
        vhold=Vhold,
        vmin=vmin,
        vcirc=vcirc,
        minsigma=minsigma,
        sig_unit=sig_unit,
        sigma_factor=sigma_factor,
    )

    return Mxs, Sxs, vbar, Vhold


# /def


##############################################################################
# END
