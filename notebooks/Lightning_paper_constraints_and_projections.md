---
jupyter:
  jupytext:
    formats: ipynb,md,Rmd
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.5.2
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# Macro-Induced Lightning Constraints

```python inputHidden=false jupyter={"outputs_hidden": false} outputHidden=false
"""
    TITLE   : Macro-Induced Lightning Constraints
    AUTHOR  : Jagjit Sidhu, Nathaniel Starkman
    PROJECT : https://github.com/cwru-pat/macro_lightning
""";

__author__ = ['Jagjit Sidhu', "Nathaniel Starkman"]
```

<span style='font-size:30px;font-weight:650'>
    About
</span>

This notebook contains the calculations for how well macro-induced lightnint on Earth and Jupiter can constrain macro models.



<br><br>

- - -



## Prepare

```python
from utilipy import ipython
ipython.add_raw_code_toggle()
```

<!-- #region inputHidden=false outputHidden=false -->
### Imports
<!-- #endregion -->

```python
# THIRD PARTY

from astropy import units as u
from astropy.table import QTable
import matplotlib.pyplot as plt
import numpy as np


# PROJECT SPECIFIC

from macro_lightning import plot, physics as ph
from macro_lightning import parameters
from macro_lightning.utils import qnorm, qarange

```

### Parameters

```python
load_saved = True
```

```python
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
sigma_unit = u.cm**2
sigmin, sigmax = 1e-15, 1e25
min_sigma = 6e-8 * u.cm ** 2
"""Minimum observable sigma_x from lightning""";

```

<br><br>

- - -



## Earth


We first perform the integral $$\Gamma(M_x, \sigma_x) T = A_{det}\frac{\rho_{DM} T}{M_x} \int_{v_{threshold}(\sigma_x;D)}^{v_{esc}}v_x f_{MBSS}(v_x) \rm{d}v_x $$

from https://arxiv.org/pdf/1908.00557.pdf

For an observation period of two years.

```python
# from https://ssd.jpl.nasa.gov/?planet_phys_par
vesc_sun_at_earth = 42.1 * u.km / u.s
vesc_earth = parameters.solar_system_vesc_params.get()["Earth"]

vminE = qnorm(vesc_sun_at_earth, vesc_earth)
vminE

# A_{det}*\rho_{DM}*T; the quantity outside the integral
# this includes the 30% alignment factor
ArhoE = 3 * u.g * u.s / u.m

sigma_factor_earth = 1e8 * (u.cm ** 2 / u.s) ** 2
r"""Paper Eqn. 7, setting $\lambda_e^{macro} \geq \lambda_e^{natural}$."""
```

```python
try:
    if load_saved:
        macro = QTable.read("data/macro_msig_earth.asdf", format="asdf")
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
        Arho = ArhoE,
        # kwargs
        minsigma=min_sigma,
        m_unit=m_unit,
        sigma_factor=sigma_factor_earth,
        sig_unit=sigma_unit
    )

    macro = QTable([massE, sigmaE], names=["mass", "sigma"])
    macro.write("data/macro_msig_earth.asdf", format="asdf")

else:
    massE = macro["mass"]
    sigmaE = macro["sigma"]

```

**Plot Constraints**

```python
upperlightning = massE * 1e-4 * u.cm**2 / u.g
"""The upper bound to any constraints.

sigma_x/M_x > 10^-4 loses most of the energy while traveling
through the atmosphere, reaching some slow terminal velocity
and so would not be detectable.

""";

```

```python
with plot.constraints_plot(m_arr, sigmin=sigmin):

    plt.fill_between(
        massE, sigmaE, upperlightning,
        where=None,
        facecolor='none',
        edgecolor='black',
        hatch="\\",
        alpha=1.0,
        zorder=8,
        label="Earth: Downward"
    )

    lim = ph.sigma_limit_through_earth(massE)
    sel = lim > sigmaE
    plt.fill_between(
        massE[sel], sigmaE[sel], lim[sel],
        where=None,
        facecolor='none',
        edgecolor='gray',
        hatch=r"//",
        alpha=0.8,
        zorder=8,
        label="Earth: Upward"
    )

plt.show();
```

## Jupiter

```python
sigma_factor = 5e8 * (u.cm**2 / u.s) ** 2
r"""Paper Eqn. 7, setting $\lambda_e^{macro} \geq \lambda_e^{natural}$.""";
```

```python
# https://ssd.jpl.nasa.gov/?planet_phys_par
vesc_sun_at_jupiter = 18.5 * u.km / u.s
vesc_jupiter = parameters.solar_system_vesc_params.get()["Jupiter"]

vminJ = qnorm(vesc_sun_at_earth, vesc_jupiter)
vminJ

# A_{det}*\rho_{DM}*T; the quantity outside the integral
# this includes the 30% alignment factor
ArhoJ = 2e5 / 3 * (u.g * u.s / u.m)

```

```python
try:
    if load_saved:
        macro = QTable.read("data/macro_msig_jupiter.asdf", format="asdf")
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
    macro.write("data/macro_msig_jupiter.asdf", format="asdf")

else:
    massJ = macro["mass"]
    sigmaJ = macro["sigma"]

```

**Plot Constraints**


Note that the integral solvers in `calculate_Mx_and_Sx` are stiff and will find a minimum mass. This is an artifact of the bin size. In truth the mass range extends to the sigma lower / upper bounds convergence.

We extend the derived exclusion region manually.

```python
massJ = massJ.insert(0, 1e1 * u.g)
sigmaJ = sigmaJ.insert(0, sigmaJ[0])
```

```python
uppersigmalightningjupiter = massJ[:] * 1e-4
"""The upper bound to any constraints.

sigma_x/M_x > 10^-4 loses most of the energy while traveling
through the atmosphere, reaching some slow terminal velocity
and so would not be detectable we use the same number as Earth,
as lightning on Jupiter is expected to occur under very
similar conditions.

""";
```

```python
with plot.constraints_plot(m_arr, sigmin=sigmin):

    plt.fill_between(
        massJ,
        sigmaJ,
        uppersigmalightningjupiter,
        where=None,
        facecolor="none",
        edgecolor="cyan",
        hatch="\\",
        alpha=1.0,
        zorder=4,
    )

plt.show();
```

### Plotting All Constraints


Plotting both Earth and Jupiter lightning constraints on macro mass and cross-section.

```python
with plot.constraints_plot(
    m_arr=m_arr,
    sigmin=sigmin,
    sigmax=sigmax,
    all_constrs=True,  # previous constraints
    savefig="figures/lightningconstraints.pdf",
) as (fig, ax, m_arr, ymin, ymax):

    plt.fill_between(
        massE, sigmaE, upperlightning,
        where=None,
        facecolor='none',
        edgecolor='black',
        hatch="\\",
        alpha=1.0,
        zorder=8,
        label="Earth: Downward"
    )

    lim = ph.sigma_limit_through_earth(massE)
    sel = lim > sigmaE
    plt.fill_between(
        massE[sel], sigmaE[sel], lim[sel],
        where=None,
        facecolor='none',
        edgecolor='gray',
        hatch=r"//",
        alpha=0.8,
        zorder=8,
        label="Earth: Upward"
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

plt.show();

```

<br><br>

- - -

<span style='font-size:40px;font-weight:650'>
    END
</span>
