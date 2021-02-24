# -*- coding: utf-8 -*-

"""Test :mod:`~macro_lightning.parameters`."""


__all__ = [
    "test_solar_system_vesc_params",
    "test_vesc_sun_at_R",
]


##############################################################################
# IMPORTS

# THIRD PARTY

# THIRD PARTY
import astropy.units as u
import pytest

# PROJECT-SPECIFIC
from .. import parameters as params

##############################################################################
# PARAMETERS

_KMS = u.km / u.s


##############################################################################
# CODE
##############################################################################


def test_solar_system_vesc_params():
    """Test :class:`~macro_lightning.parameters.solar_system_vesc_params`."""
    # test set
    params.solar_system_vesc_params.set("latest")

    # test setting set references
    refs = params.solar_system_vesc_params._references
    expected = params.solar_system_vesc_params._registry["DEFAULT"][
        "references"
    ]
    assert refs == expected

    # test get
    ss = params.solar_system_vesc_params.get()
    expected = params.solar_system_vesc_params._registry["DEFAULT"]["params"]
    assert ss == expected

    # test register
    new_params = {k: v + 2 * _KMS for k, v in ss.items()}
    params.solar_system_vesc_params.register(
        "new",
        params=new_params,
        references={"_source": None},
    )

    # test can set
    params.solar_system_vesc_params.set("new")

    # test getting works
    new_ss = params.solar_system_vesc_params.get()
    assert new_ss == new_params

    pass


# /def


# -------------------------------------------------------------------


def test_vesc_sun_at_R():
    """Test :func:`~macro_lightning.parameters.vesc_sun_at_R`."""
    # Unity test
    assert params.vesc_sun_at_R(1 * u.AU) == params.vesc_sun_at_earth

    # quadruple distance = half the escape velocity
    assert params.vesc_sun_at_R(4 * u.AU) == 2.0 * params.vesc_sun_at_earth

    # Error test
    with pytest.raises(Exception):
        params.vesc_sun_at_R(1)

    with pytest.raises(Exception):
        params.vesc_sun_at_R(1 * u.deg)


# /def


##############################################################################
# END
