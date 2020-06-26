# -*- coding: utf-8 -*-

"""test plot functions.

It's hard to test the exact plots, so we only test whether the plot function
successfully creates a plot.

"""


# __all__ = [
#     # functions
#     "",
#     # other
#     "",
# ]


##############################################################################
# IMPORTS

# BUILT-IN

# THIRD PARTY

# import astropy.units as u

import matplotlib.pyplot as plt

import numpy as np

import pytest


# PROJECT-SPECIFIC

from .. import plot


##############################################################################
# PARAMETERS

m_arr = np.logspace(1, 25)

mmin = m_arr.min()
mmax = m_arr.max()

sigmin: float = 1e-15
sigmax: float = 1e25

Mmicro = np.logspace(23.0, 28.0)


##############################################################################
# CODE
##############################################################################


@pytest.mark.mpl_image_compare
def test_plot_atomic_density_line():
    """Test :func:`~macro_lightning.utils.as_quantity`."""
    fig, ax = plt.subplots(figsize=(6, 4))

    plot.plot_atomic_density_line(m_arr)

    plt.xlim([mmin, mmax])
    plt.ylim([sigmin, sigmax])

    return fig


# /def


# -------------------------------------------------------------------


@pytest.mark.mpl_image_compare
def test_plot_nuclear_density_line():
    """Test :func:`~macro_lightning.utils.as_quantity`."""
    fig, ax = plt.subplots(figsize=(6, 4))

    plot.plot_nuclear_density_line(m_arr)

    plt.xlim([mmin, mmax])
    plt.ylim([sigmin, sigmax])

    return fig


# /def


# -------------------------------------------------------------------


@pytest.mark.mpl_image_compare
def test_plot_black_hole_line():
    """Test :func:`~macro_lightning.utils.as_quantity`."""
    fig, ax = plt.subplots(figsize=(6, 4))

    plot.plot_black_hole_line(m_arr)

    plt.xlim([mmin, mmax])
    plt.ylim([sigmin, sigmax])

    return fig


# /def


# -------------------------------------------------------------------


@pytest.mark.mpl_image_compare
def test_plot_reference_densities():
    """Test :func:`~macro_lightning.utils.as_quantity`."""
    fig, ax = plt.subplots(figsize=(6, 4))

    plot.plot_reference_densities(m_arr)

    plt.xlim([mmin, mmax])
    plt.ylim([sigmin, sigmax])

    return fig


# /def


# -------------------------------------------------------------------


@pytest.mark.mpl_image_compare
def test_plot_mica_constraints():
    """Test :func:`~macro_lightning.utils.as_quantity`."""
    fig, ax = plt.subplots(figsize=(6, 4))

    plot.plot_reference_densities(m_arr)
    plot.plot_mica_constraints()

    plt.xlim([mmin, mmax])
    plt.ylim([sigmin, sigmax])

    return fig


# /def


# -------------------------------------------------------------------


@pytest.mark.mpl_image_compare
def test_plot_white_dwarf_constraints():
    """Test :func:`~macro_lightning.utils.as_quantity`."""
    fig, ax = plt.subplots(figsize=(6, 4))

    plot.plot_reference_densities(m_arr)
    plot.plot_white_dwarf_constraints()

    plt.xlim([mmin, mmax])
    plt.ylim([sigmin, sigmax])

    return fig


# /def


# -------------------------------------------------------------------


@pytest.mark.mpl_image_compare
def test_plot_cmb_constraints():
    """Test :func:`~macro_lightning.utils.as_quantity`."""
    fig, ax = plt.subplots(figsize=(6, 4))

    plot.plot_reference_densities(m_arr)
    plot.plot_cmb_constraints(m_arr, sigmax=sigmax)

    plt.xlim([mmin, mmax])
    plt.ylim([sigmin, sigmax])

    return fig


# /def


# -------------------------------------------------------------------


@pytest.mark.mpl_image_compare
def test_plot_superbursts_constraints():
    """Test :func:`~macro_lightning.utils.as_quantity`."""
    fig, ax = plt.subplots(figsize=(6, 4))

    plot.plot_reference_densities(m_arr)
    plot.plot_superbursts_constraints()

    plt.xlim([mmin, mmax])
    plt.ylim([sigmin, sigmax])

    return fig


# /def


# -------------------------------------------------------------------


@pytest.mark.mpl_image_compare
def test_plot_humandeath_constraints():
    """Test :func:`~macro_lightning.utils.as_quantity`."""
    fig, ax = plt.subplots(figsize=(6, 4))

    plot.plot_reference_densities(m_arr)
    plot.plot_humandeath_constraints()

    plt.xlim([mmin, mmax])
    plt.ylim([sigmin, sigmax])

    return fig


# /def


# -------------------------------------------------------------------


@pytest.mark.mpl_image_compare
def test_plot_dfn_constraints():
    """Test :func:`~macro_lightning.utils.as_quantity`."""
    fig, ax = plt.subplots(figsize=(6, 4))

    plot.plot_reference_densities(m_arr)
    plot.plot_dfn_constraints()

    plt.xlim([mmin, mmax])
    plt.ylim([sigmin, sigmax])

    return fig


# /def


# -------------------------------------------------------------------


@pytest.mark.mpl_image_compare
def test_plot_lensing_constraints():
    """Test :func:`~macro_lightning.utils.as_quantity`."""
    fig, ax = plt.subplots(figsize=(6, 4))

    plot.plot_reference_densities(m_arr)
    plot.plot_lensing_constraints(Mmicro=Mmicro)

    plt.xlim([mmin, mmax])
    plt.ylim([sigmin, sigmax])

    return fig


# /def


# -------------------------------------------------------------------


@pytest.mark.mpl_image_compare
def test_plot_black_hole_constraints():
    """Test :func:`~macro_lightning.utils.as_quantity`."""
    fig, ax = plt.subplots(figsize=(6, 4))

    plot.plot_reference_densities(m_arr)
    plot.plot_black_hole_constraints(m_arr, sigmin=sigmin)

    plt.xlim([mmin, mmax])
    plt.ylim([sigmin, sigmax])

    return fig


# /def


# -------------------------------------------------------------------


@pytest.mark.mpl_image_compare
def test_empty_constraints_plot():
    """Test :func:`~macro_lightning.utils.as_quantity`."""
    with plot.constraints_plot(m_arr, sigmin=sigmin, sigmax=sigmax) as (
        fig,
        *_,
    ):
        pass

    # /with

    return fig


# /def


# -------------------------------------------------------------------


@pytest.mark.mpl_image_compare
def test_full_constraints_plot():
    """Test :func:`~macro_lightning.utils.as_quantity`."""
    with plot.constraints_plot(
        m_arr,
        sigmin=sigmin,
        sigmax=sigmax,
        constr_labels=False,
        # constraints
        mica_constr=True,
        WD_constr=True,
        CMB_constr=True,
        superbursts_constr=True,
        humandeath_constr=True,
        dfn_constr=True,
        lensing_constr=True,
        bh_constr=True,
    ) as (fig, *_):
        pass
    # /with

    return fig


# /def


# -------------------------------------------------------------------


##############################################################################
# END