Constraints from Macro-Induced Lightning
========================================

Welcome to ``macro_lightning``, the code-base for a paper on constraining macroscopic dark matter models with observations of lightning on Earth and Jupiter. If you are looking for the paper, the peer-reviewed journal article can be found `here <www.google.com>`_ (TODO add link) and the arxiv pre-print `here <https://arxiv.org>`_ (TODO add link). Alternatively, the source code for the paper is included as a sub-module in the folder "papers_and_presentations/paper".

Macroscopic dark matter (macros) is a broad class of alternative candidates to particle dark matter. These candidates would transfer energy to matter primarily through elastic scattering. A sufficiently large macro passing through the atmosphere would produce a straight channel of ionized plasma. If the cross-section of the macro is :math:`\sigma_x \gtrapprox 6 \times 10^{-9} \rm{cm}^2`, then under atmospheric conditions conducive to lightning (eg. a thunderstorm) the plasma channel would be sufficient to seed a lightning strike with a single leader.

This is entirely unlike ordinary bolt lightning in which a long sequence of hundreds or thousands of few-meter-long leaders are strung together. This macro-induced lightning would be extremely straight, and thus highly distinctive. Neither wind shear nor magnetohydrodynamic instabilities would markedly spoil its straightness. The only photographically documented case of a straight lightning bolt is probably not straight enough to have been macro-induced.

For any discussion or derivations, see thee paper. For code documentation, see `ReadTheDocs <https://github.com/cwru-pat/macro_lightning>`_. This is the raw code.

.. container::

   |DOI| |PyPI| |Build Status| |Coveralls| |astropy|


Notebooks
---------

Folder contains Mathematica notebooks to compute event rates for macro-induced lightning, as well as the constraints in mass and cross-section, both for lightning events on Earth and on Jupiter. There is also a notebook to compute the fraction of the Maxwell distribution of DM particles with velocities high enough to produce straight lightning bolts (ie. traveling faster than a lightning leader would ordinarily propagate).

Further notebooks can be found in "docs/examples"


Papers and Presentations
------------------------

Look in folder for paper


CODE
----
The code is included in the ``macro_lightning`` folder.


References
----------
Many of the sources cited in the paper are downloaded and included here.



*****************
How to contribute
*****************

|Milestones| |Open Issues| |Last Commit|

We welcome contributions from anyone via pull requests on `GitHub
<https://github.com/cwru-pat/macro_lightning>`_. If you don't feel comfortable modifying or
adding functionality, we also welcome feature requests and bug reports as
`GitHub issues <https://github.com/cwru-pat/macro_lightning/issues>`_.

The development process follows that of the `astropy-package-template <https://docs.astropy.org/en/latest/development/astropy-package-template.html>`_ from Astropy's `release procedure <https://docs.astropy.org/en/latest/development/releasing.html#release-procedure>`_.


***********
Attribution
***********

|DOI| |License|

Copyright 2020 - Nathaniel Starkman, Jagjit Sidhu, Harrison Winch, Glenn Starkan, and contributors.

``macro_lightning`` is free software made available under the BSD-3 License. For details see the `LICENSE <https://github.com/cwru-pat/macro_lightning/blob/master/LICENSE>`_ file.

If you make use of this code, please consider citing the Zenodo DOI as a software citation::

   @software{macro_lightning:zenodo,
     author       = {Nathaniel Starkman and Jagjit Sidhu and Harrison Winch and Glenn Starkman},
     title        = {Constraints from Macro-Induced Lightning},
     publisher    = {Zenodo},
     doi          = {10.5281/zenodo.3911476},
     url          = {https://zenodo.org/badge/latestdoi/275470390}
   }



.. |astropy| image:: http://img.shields.io/badge/powered%20by-AstroPy-orange.svg?style=flat
   :target: http://www.astropy.org/

.. |Build Status| image:: https://travis-ci.com/cwru-pat/macro_lightning.svg?branch=master
    :target: https://travis-ci.com/cwru-pat/macro_lightning

.. |Documentation Status| image:: https://readthedocs.org/projects/macro_lightning/badge/?version=latest
   :target: https://macro_lightning.readthedocs.io/en/latest/?badge=latest

.. |DOI| image:: https://zenodo.org/badge/275470390.svg
   :target: https://zenodo.org/badge/latestdoi/275470390

.. |License| image:: https://img.shields.io/badge/License-BSD%203--Clause-blue.svg
   :target: https://opensource.org/licenses/BSD-3-Clause

.. |PyPI| image:: https://badge.fury.io/py/macro_lightning.svg
   :target: https://badge.fury.io/py/macro_lightning

.. |Milestones| image:: https://img.shields.io/github/milestones/open/cwru-pat/macro_lightning?style=flat
   :alt: GitHub milestones

.. |Open Issues| image:: https://img.shields.io/github/issues-raw/cwru-pat/macro_lightning?style=flat
   :alt: GitHub issues

.. |Last Commit| image:: https://img.shields.io/github/last-commit/cwru-pat/macro_lightning/master?style=flat
   :alt: GitHub last commit (branch)

.. |Coveralls| image:: https://coveralls.io/repos/github/cwru-pat/macro_lightning/badge.svg?branch=master
   :target: https://coveralls.io/github/cwru-pat/macro_lightning?branch=master
