# -*- coding: utf-8 -*-
"""Configure Test Suite.

This file is used to configure the behavior of pytest when using the Astropy
test infrastructure. It needs to live inside the package in order for it to
get picked up when running the tests inside an interpreter using
packagename.test

"""

# BUILT-IN
import os

# THIRD PARTY
import pytest

try:
    # THIRD PARTY
    from pytest_astropy_header.display import (
        PYTEST_HEADER_MODULES,
        TESTED_VERSIONS,
    )

    ASTROPY_HEADER = True
except ImportError:
    ASTROPY_HEADER = False


def pytest_configure(config):
    """Configure Pytest with Astropy.

    Parameters
    ----------
    config : pytest configuration

    """
    if ASTROPY_HEADER:

        config.option.astropy_header = True

        # Customize the following lines to add/remove entries from the list of
        # packages for which version numbers are displayed when running the
        # tests.
        PYTEST_HEADER_MODULES.pop("Pandas", None)
        PYTEST_HEADER_MODULES["scikit-image"] = "skimage"

        # PROJECT-SPECIFIC
        from . import __version__

        packagename = os.path.basename(os.path.dirname(__file__))
        TESTED_VERSIONS[packagename] = __version__


# ------------------------------------------------------
# Added by @nstarman


@pytest.fixture(autouse=True)
def add_units(doctest_namespace):
    """Add Imports to Pytest.

    Parameters
    ----------
    doctest_namespace : namespace

    """
    # import
    # THIRD PARTY
    import astropy.units

    # add to namespace
    doctest_namespace["u"] = astropy.units

    return


# def
