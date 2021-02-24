# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------------
#
# AUTHOR  : Nathaniel Starkman, Harrison Winch, Jagjit Sidhu, Glenn Starkman
# PROJECT : macro_lightning
#
# ----------------------------------------------------------------------------

"""Macro-induced Lightning."""

__author__ = [
    "Jagjit Sidhu",
    "Nathaniel Starkman",
    "Harrison Winch",
    "Glenn Starkman",
]
__copyright__ = "Copyright 2020, "
__license__ = "BSD-3"
__maintainer__ = "Nathaniel Starkman"


__all__ = [
    # modules
    "data",
    "utils",
    "parameters",
    "physics",
    "plot",
    # functions
    "constraints_plot",
    "solar_system_vesc_params",
]


##############################################################################
# IMPORTS

# ---------------------------------------------------------

# keep this content at the top. (sets the __version__)
from ._astropy_init import *  # noqa: F401, F403  # isort:skip
from ._astropy_init import __version__  # noqa: F401  # isort:skip

# ---------------------------------------------------------

# PROJECT-SPECIFIC
from . import data, parameters, physics, plot, utils
from .parameters import solar_system_vesc_params
from .plot import constraints_plot

##############################################################################
# END
