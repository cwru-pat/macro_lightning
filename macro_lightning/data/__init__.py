# -*- coding: utf-8 -*-
# see LICENSE.rst

"""Data Loading Functions."""


__all__ = [
    "load_mica_constraints",
    "load_superbursts_polygons",
    "load_humandeath_constraints",
    "load_whitedwarf_constraints",
    "load_dfn_constraints",
    "load_dfn_future_constraints",
    "load_whitedwarf_constraints",
]


##############################################################################
# IMPORTS

# BUILT IN

# BUILT-IN
import pathlib
import typing as T

# THIRD PARTY
import numpy as np
from astropy.table import Table

##############################################################################
# PARAMETERS

_data_dir = pathlib.Path(__file__).parent


##############################################################################
# CODE
##############################################################################


def load_mica_constraints() -> T.Sequence:
    r"""Mica Polygon Vertices.

    A longstanding constraint comes from examination of a slab of
    ancient mica for tracks that would have been left by the passage of
    a macro moving at the typical speed of dark matter in the Galaxy.
    This was used to rule out macros of :math:`M_x \leq 55\,` g for a wide
    range of cross sections [1]_, [2]_, [3]_

    Returns
    -------
    points : :class:`~numpy.ndarray`
        N x 2 array for a :class:`~matplotlib.patches.Polygon`

    References
    ----------
    .. [1] Price, P. (1988). Limits on Contribution of Cosmic Nuclearites
        to Galactic Dark MatterPhysical Review D, 38, 3813-3814.
    .. [2] De Rujula, A., & Glashow, S. (1984).
        Nuclearites: A Novel Form of Cosmic RadiationNature, 312, 734-737.
    .. [3] David M. Jacobs, Glenn D. Starkman, & Bryan W. Lynn (2014).
        Macro Dark MatterMNRAS.

    See Also
    --------
    :func:`~macro_lightning.plot.plot_mica_constraints`

    """
    points = np.loadtxt(
        _data_dir.joinpath("mica_polygon.txt"),
        delimiter=",",
        skiprows=1,
    )

    return points


# /def

# -------------------------------------------------------------------


def load_superbursts_polygons() -> T.Tuple[T.Sequence, T.Sequence]:
    """Superbursts Polygon Vertices.

    For sufficiently large cross-sections, the linear energy deposition could
    produce observable signals if a macro were to pass through compact objects
    such as neutron stars in the form of thermonuclear runaway, leading to a
    superburst. New constraints are inferred from the low mass X-ray
    binary 4U 1820-30, in which more than a decade passed between successive
    superbursts [1]_.

    .. |ndarray| replace:: :class:`~numpy.ndarray`
    .. |Polygon| replace:: :class:`~matplotlib.patches.Polygon`

    Returns
    -------
    superbursts1_points : |ndarray|
        N x 2 array for a |Polygon|
    superbursts2_points : |ndarray|
        N x 2 array for a |Polygon|

    References
    ----------
    .. [1] J. S. Sidhu and G. D. Starkman, Physical Review D 101 (2020),
        0.1103/physrevd.101.083503.

    See Also
    --------
    :func:`~macro_lightning.plot.plot_superbursts_constraints`

    """
    points1 = np.loadtxt(_data_dir.joinpath("superbursts1_polygon.txt"))

    points2 = np.loadtxt(_data_dir.joinpath("superbursts2_polygon.txt"))

    return points1, points2


# /def


# -------------------------------------------------------------------


def load_humandeath_constraints() -> T.Tuple[
    T.Sequence,
    T.Sequence,
    T.Sequence,
]:
    r"""Constraint data from dark matter caused human deaths.

    Macroscopic dark matter (macros) refers to a class of dark matter
    candidates that scatter elastically off of ordinary matter with a large
    geometric cross-section. A wide range of macro masses :math:`M_X` and
    cross-sections :math:`\sigma_X` remain unprobed. Over a wide region within
    the unexplored parameter space, collisions of a macro with a human body
    would result in serious injury or death. The absence of such unexplained
    impacts with a well-monitored subset of the human population to exclude a
    region bounded by :math:`\sigma_X > 10^{−8} − 10^{−7}` cm2 and :math:`M_X
    < 50` kg [1].

    .. |ndarray| replace:: :class:`~numpy.ndarray`

    Returns
    -------
    mass : |ndarray|, optional
        N x 1 array for :class:`~matplotlib.pyplot.fill_between`
    xsec : |ndarray|, optional
        N x 1 array for `~fill_between` 2nd argument
    upper : |ndarray|, optional
        N x 1 array for a `~fill_between` 3rd argument

    References
    ----------
    .. [1] J. S. Sidhu and G. D. Starkman, Physical Review D 101 (2020),
        0.1103/physrevd.101.083503.

    See Also
    --------
    :func:`~macro_lightning.plot.plot_humandeath_constraints`

    """
    data = Table.read(
        _data_dir.joinpath("humandeath_constraints.ecsv"),
        format="ascii.ecsv",
    )

    return data["mass"], data["cross-section"], data["upper-lim"]


# /def

# -------------------------------------------------------------------


def load_dfn_constraints() -> T.Tuple[T.Sequence, T.Sequence, T.Sequence]:
    r"""Constraint data from Desert Fireball Network (DFN).

    Constraints for low mass macros from the null observation of bright
    meteors formed by a passing macro, across two extensive networks of
    cameras built originally to observe meteorites. The parameter space that
    could be probed with planned upgrades to the existing array of cameras in
    one of these networks still currently in use, the Desert Fireball Network
    in Australia, is estimated [1]_.

    .. |ndarray| replace:: :class:`~numpy.ndarray`

    Returns
    -------
    mass : |ndarray|, optional
        N x 1 array for :class:`~matplotlib.pyplot.fill_between`
    xsec : |ndarray|, optional
        N x 1 array for `~fill_between` 2nd argument
    upper : |ndarray|, optional
        N x 1 array for a `~fill_between` 3rd argument

    References
    ----------
    .. [1] J. S. Sidhu and G. Starkman, Physical Review D 100 (2019),
        10.1103/physrevd.100.123008.

    See Also
    --------
    :func:`~macro_lightning.plot.plot_dfn_constraints`

    """
    data = Table.read(
        _data_dir.joinpath("dfn_constraints.ecsv"),
        format="ascii.ecsv",
    )

    return data["mass"], data["cross-section"], data["upper-lim"]


# /def

# -------------------------------------------------------------------


def load_dfn_future_constraints() -> T.Tuple[
    T.Sequence,
    T.Sequence,
    T.Sequence,
]:
    r"""Constraint data from Desert Fireball Network (DFN).

    Constraints for low mass macros from the null observation of bright
    meteors formed by a passing macro, across two extensive networks of
    cameras built originally to observe meteorites. The parameter space that
    could be probed with planned upgrades to the existing array of cameras in
    one of these networks still currently in use, the Desert Fireball Network
    in Australia, is estimated [1]_.

    .. |ndarray| replace:: :class:`~numpy.ndarray`

    Returns
    -------
    mass : |ndarray|, optional
        N x 1 array for :class:`~matplotlib.pyplot.fill_between`
    xsec : |ndarray|, optional
        N x 1 array for `~fill_between` 2nd argument
    upper : |ndarray|, optional
        N x 1 array for a `~fill_between` 3rd argument

    References
    ----------
    .. [1] J. S. Sidhu and G. Starkman, Physical Review D 100 (2019),
        10.1103/physrevd.100.123008.

    """
    data = Table.read(
        _data_dir.joinpath("dfn_future_constraints.ecsv"),
        format="ascii.ecsv",
    )

    return data["mass"], data["cross-section"], data["upper-lim"]


# /def

# -------------------------------------------------------------------


def load_whitedwarf_constraints() -> T.Sequence:
    r"""Constraint data from the existence of massive White Dwarfs.

    For sufficiently large cross-sections, the linear energy deposition could
    produce observable signals if a macro were to pass through compact objects
    such as white dwarfs in the form of thermonuclear runaway leading to a
    type IA supernova. These are weaker than previously inferred [2]_ in
    important respects because of more careful treatment of the passage of a
    macro through the white dwarf and greater conservatism regarding the size
    of the region that must be heated to initiate runaway. On the other hand,
    more stringent constraints are placed on macros at low cross-section,
    using new data from the Montreal White Dwarf Database [1]_.

    Returns
    -------
    points : :class:`~numpy.ndarray`
        N x 2 array for a :class:`~matplotlib.patches.Polygon`

    References
    ----------
    .. [1] J. S. Sidhu and G. D. Starkman, Physical Review D 101 (2020),
        0.1103/physrevd.101.083503.
    .. [2] P. Graham, R. Janish, V. Narayan, S. Rajendran, and P. Riggins,
       Physical Review D 98, 115027 (2018).

    See Also
    --------
    :func:`~macro_lightning.plot.plot_white_dwarf_constraints`

    """
    points = np.loadtxt(_data_dir.joinpath("whitedwarf_polygon.txt"))

    return points


# /def


##############################################################################
# END
