# -*- coding: utf-8 -*-

"""Parameters."""


__all__ = [
    # functions
    "solar_system_vesc_params",
    "vesc_sun_at_R",
]


##############################################################################
# IMPORTS

# BUILT-IN
import typing as T

# THIRD PARTY
import numpy as np
from astropy import units as u
from astropy.utils.state import ScienceState

##############################################################################
# PARAMETERS

_KMS = u.km / u.s

_ref_B = (
    "Explanatory Supplement to the Astronomical Almanac. "
    "1992. K. P. Seidelmann, Ed., p.706 (Table 15.8) and p.316 "
    "(Table 5.8.1), University Science Books, Mill Valley, California."
)
_ref_C = (
    "Seidelmann, P.K. et al. 2007. 'Report of the IAU/IAG Working "
    "Group on cartographic coordinates and rotational elements: 2006' "
    "Celestial Mech. Dyn. Astr. 98:155-180."
)
_ref_D = (
    "Archinal, B.A. et al. 2018. 'Report of the IAU/IAG Working Group "
    "on cartographic coordinates and rotational elements: 2015' "
    "Celestial Mech. Dyn. Astr. 130:22."
)


##############################################################################
# CODE
##############################################################################


class solar_system_vesc_params(ScienceState):
    """Solar System Parameters."""

    _latest_value = "default"
    _references = None
    _value = None

    _registry = {
        "DEFAULT": {
            "params": {
                "Sun": 617.5 * _KMS,
                "Mercury": 4.25 * _KMS,
                "Venus": 10.36 * _KMS,
                "Earth": 11.19 * _KMS,
                "Mars": 5.03 * _KMS,
                "Jupiter": 60.20 * _KMS,
                "Saturn": 36.09 * _KMS,
                "Uranus": 21.38 * _KMS,
                "Neptune": 23.56 * _KMS,
                "Pluto": 1.21 * _KMS,
            },
            "references": {
                "_source": "https://ssd.jpl.nasa.gov/?planet_phys_par",
                "Sun": (_ref_B, _ref_C, _ref_D),
                "Mercury": (_ref_B, _ref_C, _ref_D),
                "Venus": (_ref_B, _ref_C, _ref_D),
                "Earth": (_ref_B, _ref_C, _ref_D),
                "Mars": (_ref_B, _ref_C, _ref_D),
                "Jupiter": (_ref_B, _ref_C, _ref_D),
                "Saturn": (_ref_B, _ref_C, _ref_D),
                "Uranus": (_ref_B, _ref_C, _ref_D),
                "Neptune": (_ref_B, _ref_C, _ref_D),
                "Pluto": (_ref_B, _ref_C, _ref_D),
            },
        },
    }

    @classmethod
    def get_solar_params_from_string(cls, arg):
        """Get parameters from registry."""
        # Resolve the meaning of 'latest'
        if arg == "latest":
            arg = cls._latest_value

        if arg.lower() == "default":

            info = cls._registry["DEFAULT"]

        elif arg in cls._registry:

            info = cls._registry[arg]

        else:
            raise ValueError(
                f"Invalid string input to retrieve solar "
                f'parameters for Galactocentric frame: "{arg}"',
            )

        return info["params"], info["references"]

    # /def

    @classmethod
    def validate(cls, value):
        """Validate `value`, from string or dict."""
        if value is None:
            value = cls._latest_value

        if isinstance(value, str):
            params, refs = cls.get_solar_params_from_string(value)
            cls._references = refs
            return params

        elif isinstance(value, dict):
            return value

        else:
            raise ValueError(
                "Invalid input to retrieve solar parameters."
                "Input must be a string, or dict",
            )

    # /def

    @classmethod
    def register(cls, name: str, params: dict, references: dict):
        """Register a set of parameters.

        Parameters
        ----------
        name : str
        params : dict
        references : dict

        """
        cls._registry[name] = {"params": params, "references": references}

    # /def

    @classmethod
    def set(
        cls,
        value: dict,
        register_as: T.Optional[str] = None,
        references: T.Optional[dict] = None,
    ):
        """Set (see ScienceState) with optional registering.

        Parameters
        ----------
        value : dict
        register_as : str, optional
            the name of the science state to set
        references : dict, optional
            references for `value`. Only used if `register_as` is str.

        """
        super().set(value)

        if isinstance(register_as, str):
            cls._registry[register_as] = {
                "params": value,
                "references": references or {},
            }

    # /def


# /class

# -------------------------------------------------------------------


vesc_sun_at_earth = 42.1 * _KMS
"""Solar escape velocity, from 1 AU to infinity [1]_.

References
----------
.. [1] https://en.wikipedia.org/wiki/Escape_velocity

"""


# -------------------------------------------------------------------


@u.quantity_input(R="length")
def vesc_sun_at_R(R):
    r"""Escape velocity from the sun, starting at position R.

    The Newtonian escape velocity from a spherical mass distribution,
    starting at a position r_0, is :math:`v_0=\sqrt{2gr_0}`. If this value
    is known at some position r0, than it is known at all R by virtue
    of ratios. We calculate this value for the sun relative to the
    known value at the earth -- 42.1 km / s.

    Parameters
    ----------
    R : :class:`~astropy.coordinates.Distance` or |Quantity|
        From the sun.

    Returns
    -------
    vesc : |Quantity|
        Same shape as `R`

    .. |Quantity| replace:: :class:`~astropy.units.Quantity`

    """
    ratio = R.to_value(u.AU)  # b/c r_earth = 1 AU
    return np.sqrt(ratio) * vesc_sun_at_earth


# /def


##############################################################################
# END
