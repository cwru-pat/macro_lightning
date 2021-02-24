# -*- coding: utf-8 -*-

"""Astropy Quantity-Numpy Compatibility Utilities."""

__author__ = "Nathaniel Starkman"


__all__ = [
    "as_quantity",
    "qsquare",
    "qnorm",
    "qarange",
]


##############################################################################
# IMPORTS

# THIRD PARTY
import numpy as np
from astropy.units import Quantity
from numpy.linalg import norm

##############################################################################
# CODE
##############################################################################


def as_quantity(arg):
    """Convert argument to a Quantity (or raise `NotImplementedError`).

    from :mod:`~astropy.utils`.

    Returns
    -------
    `~astropy.units.Quantity`
        not copied, quantity subclasses passed through.

    Raises
    ------
    `NotImplementedError`
        if ``Quantity(arg)`` fails

    """
    try:
        return Quantity(arg, copy=False, subok=True)
    except Exception:
        raise NotImplementedError


# /def

# -------------------------------------------------------------------


def qsquare(*args, **kw):
    """Quantity, Squared.

    Parameters
    ----------
    *args : `~astropy.units.Quantity`
        Passed, as tuple, to :func:`~as_quantity`
    **kw
        Arguments into :func:`~numpy.square`

    Returns
    -------
    `~astropy.units.Quantity`
        Not copied, subclasses passed through.

    Raises
    ------
    `NotImplementedError`
        If :func:`~as_quantity` fails

    """
    return np.square(as_quantity(args), **kw)


# /def

# -------------------------------------------------------------------


def qnorm(*args, **kw):
    """Quantity, Normed.

    Parameters
    ----------
    *args : `~astropy.units.Quantity`
        Passed, as tuple, to :func:`~as_quantity`
    **kw
        Arguments into :func:`~numpy.linalg.norm`

    Returns
    -------
    `~astropy.units.Quantity`
        not copied, quantity subclasses passed through.

    Raises
    ------
    `NotImplementedError`
        If :func:`~as_quantity` fails

    """
    return norm(as_quantity(args), **kw)


# /def


# -------------------------------------------------------------------


def qarange(start, stop, step, unit=None):
    """:func:`~numpy.arange` for Quantities.

    Raises
    ------
    `AttributeError`
        If `start`, `stop`, or `step` are not `~astropy.units.Quantity`

    """
    if unit is None:
        unit = step.unit

    arng = np.arange(
        start.to_value(unit),
        stop.to_value(unit),
        step.to_value(unit),
    )

    return arng * unit


# /def


# -------------------------------------------------------------------


##############################################################################
# END
