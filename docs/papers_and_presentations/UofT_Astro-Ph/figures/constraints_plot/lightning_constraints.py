# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------------
#
# TITLE   : Make Lightning Constraints Plot
# AUTHOR  : Nathaniel Starkman and Jagjit Sidhu
# PROJECT : macro_lightning
#
# ----------------------------------------------------------------------------

"""Script to Generate Plot."""

__author__ = [
    "Nathaniel Starkman",
    "Jagjit Sidhu",
    "Harrison Winch",
    "Glenn Starkman",
]
__copyright__ = "Copyright 2020, "
__license__ = "GPL3, with proper citations"
__version__ = "Jun 26, 2020"
__maintainer__ = "Nathaniel Starkman"
__email__ = "n.starkman@mail.utoronto.c"
__status__ = "Pre-Print"


##############################################################################
# IMPORTS

# THIRD PARTY
import matplotlib.pyplot as plt
import numpy as np
from astropy import units as u
from astropy.table import QTable

# PROJECT-SPECIFIC
from macro_lightning import parameters
from macro_lightning import physics as ph
from macro_lightning import plot
from macro_lightning.utils import qarange, qnorm

##############################################################################
# PARAMETERS

load_saved = True

PI = np.pi
KMS = u.km / u.s

vcirc = 220.0 * KMS
vvir = 250 * KMS  # virial velocity
vesc = 550 * KMS  # Galactic escape velocity

v_start = -500 * KMS
v_step = 25 * KMS  # bin size

vels = qarange(v_start, vesc + v_step, v_step, unit=KMS)[::-1]

# Mass
m_unit = u.g
m_arr = np.logspace(1, 25)

# Cross-Section
sigma_unit = u.cm ** 2
sigmin, sigmax = 1e-15, 1e25
min_sigma = 6e-8 * u.cm ** 2
"""Minimum observable sigma_x from lightning"""


##############################################################################
# CODE
##############################################################################

#####################################################################
# EARTH

# from https://ssd.jpl.nasa.gov/?planet_phys_par
vesc_sun_at_earth = 42.1 * u.km / u.s
vesc_earth = parameters.solar_system_vesc_params.get()["Earth"]

vminE = qnorm(vesc_sun_at_earth, vesc_earth)
vminE

# A_{det}*\rho_{DM}*T; the quantity outside the integral
ArhoE = 3 * u.g * u.s / u.m

sigma_factor_earth = 1e8 * (u.cm ** 2 / u.s) ** 2
r"""Paper Eqn. 7, setting $\lambda_e^{macro} \geq \lambda_e^{natural}$."""

# -------------------------------------------------------------------

try:
    if load_saved:
        macro = QTable.read("macro_msig_earth.ecsv", format="ecsv")
    else:
        raise Exception("load_saved = False")

except Exception as e:
    print("Can't load, ", e)

    # this function determines the lower bounds of sigma_x
    # that can be probed for a wide range of masses M_x
    massE, sigmaE, *_ = ph.calculate_Mx_and_Sx(
        vels,
        vvir=vvir,
        vesc=vesc,
        vcirc=vcirc,
        vmin=vminE,
        Arho=ArhoE,
        # kwargs
        minsigma=min_sigma,
        m_unit=m_unit,
        sigma_factor=sigma_factor_earth,
        sig_unit=sigma_unit,
    )

    macro = QTable([massE, sigmaE], names=["mass", "sigma"])
    macro.write("macro_msig_earth.ecsv", format="ecsv")

else:
    massE = macro["mass"]
    sigmaE = macro["sigma"]

# -------------------------------------------------------------------

upperlightning = massE * 1e-4 * u.cm ** 2 / u.g
"""The upper bound to any constraints.

sigma_x/M_x > 10^-4 loses most of the energy while traveling
through the atmosphere, reaching some slow terminal velocity
and so would not be detectable.

"""


#####################################################################
# JUPITER

sigma_factor = 5e8 * (u.cm ** 2 / u.s) ** 2
r"""Paper Eqn. 7, setting $\lambda_e^{macro} \geq \lambda_e^{natural}$."""

# -------------------------------------------------------------------

# https://ssd.jpl.nasa.gov/?planet_phys_par
vesc_sun_at_jupiter = 18.5 * u.km / u.s
vesc_jupiter = parameters.solar_system_vesc_params.get()["Jupiter"]

vminJ = qnorm(vesc_sun_at_earth, vesc_jupiter)
vminJ

# A_{det}*\rho_{DM}*T; the quantity outside the integral
ArhoJ = 2e5 / 3 * (u.g * u.s / u.m)

# -------------------------------------------------------------------

try:
    if load_saved:
        macro = QTable.read("macro_msig_jupiter.ecsv", format="ecsv")
    else:
        raise Exception("load_saved = False")

except Exception as e:
    print("Can't load, ", e)

    # this function determines the lower bounds of sigma_x
    # that can be probed for a wide range of masses M_x
    massJ, sigmaJ, *_ = ph.calculate_Mx_and_Sx(
        vels,
        vvir=vvir,
        vesc=vesc,
        vcirc=vcirc,
        vmin=vminJ,
        Arho=ArhoJ,
        # kwargs
        minsigma=min_sigma,
        sigma_factor=5 * sigma_factor_earth,
        m_unit=m_unit,
        sig_unit=sigma_unit,
    )

    macro = QTable([massJ, sigmaJ], names=["mass", "sigma"])
    macro.write("macro_msig_jupiter.ecsv", format="ecsv")

else:
    massJ = macro["mass"]
    sigmaJ = macro["sigma"]

# -------------------------------------------------------------------
# Note that the integral solvers in `calculate_Mx_and_Sx` are stiff and will
# find a minimum mass. This is an artifact of the bin size. In truth the mass
# range extends to the sigma lower / upper bounds convergence.
# We extend the derived exclusion region manually.

massJ = massJ.insert(0, 1e1 * u.g)
sigmaJ = sigmaJ.insert(0, sigmaJ[0])

# -------------------------------------------------------------------

uppersigmalightningjupiter = massJ[:] * 1e-4
"""The upper bound to any constraints.

sigma_x/M_x > 10^-4 loses most of the energy while traveling
through the atmosphere, reaching some slow terminal velocity
and so would not be detectable we use the same number as Earth,
as lightning on Jupiter is expected to occur under very
similar conditions.

"""

#####################################################################
# CONSTRAINTS

with plot.constraints_plot(
    m_arr=m_arr,
    sigmin=sigmin,
    sigmax=sigmax,
    all_constrs=True,  # previous constraints
    savefig="figures/lightningconstraints.png",
) as (fig, ax, m_arr, ymin, ymax):

    plt.fill_between(
        massE,
        sigmaE,
        upperlightning,
        where=None,
        facecolor="none",
        edgecolor="black",
        hatch="//",
        alpha=1.0,
        zorder=8,
        label="Earth Lightning",
    )
    plt.fill_between(
        massJ,
        sigmaJ,
        uppersigmalightningjupiter,
        where=None,
        facecolor="none",
        edgecolor="cyan",
        hatch="\\",
        alpha=1.0,
        zorder=5,
        label="Jupiter Lightning",
    )

# /with

plt.show()


##############################################################################
# END
