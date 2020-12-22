# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by `poetry run pymedphys dev propagate`

from setuptools import setup

package_dir = {"": "lib"}

packages = [
    "pymedphys",
    "pymedphys._base",
    "pymedphys._data",
    "pymedphys._dev",
    "pymedphys._dicom",
    "pymedphys._dicom.anonymise",
    "pymedphys._dicom.connect",
    "pymedphys._dicom.constants",
    "pymedphys._dicom.ct",
    "pymedphys._dicom.delivery",
    "pymedphys._dicom.rtplan",
    "pymedphys._dicom.structure",
    "pymedphys._dicom.utilities",
    "pymedphys._electronfactors",
    "pymedphys._experimental",
    "pymedphys._experimental.autosegmentation",
    "pymedphys._experimental.fileformats",
    "pymedphys._experimental.fileformats.mapcheck",
    "pymedphys._experimental.fileformats.mephysto",
    "pymedphys._experimental.fileformats.profiler",
    "pymedphys._experimental.film",
    "pymedphys._experimental.paulking",
    "pymedphys._experimental.pedromartinez",
    "pymedphys._experimental.pedromartinez.oncentra",
    "pymedphys._experimental.pedromartinez.utils",
    "pymedphys._experimental.pinnacle",
    "pymedphys._experimental.plancomplexity",
    "pymedphys._experimental.pseudonymisation",
    "pymedphys._experimental.quickcheck",
    "pymedphys._experimental.serviceplans",
    "pymedphys._experimental.streamlit",
    "pymedphys._experimental.streamlit.apps",
    "pymedphys._experimental.streamlit.apps.wlutz",
    "pymedphys._experimental.streamlit.utilities",
    "pymedphys._gamma",
    "pymedphys._gamma.api",
    "pymedphys._gamma.implementation",
    "pymedphys._gamma.utilities",
    "pymedphys._icom",
    "pymedphys._imports",
    "pymedphys._imports.slow",
    "pymedphys._losslessjpeg",
    "pymedphys._metersetmap",
    "pymedphys._metersetmap.delivery",
    "pymedphys._metersetmap.plt",
    "pymedphys._mocks",
    "pymedphys._monaco",
    "pymedphys._mosaiq",
    "pymedphys._streamlit",
    "pymedphys._streamlit.apps",
    "pymedphys._streamlit.apps.metersetmap",
    "pymedphys._streamlit.utilities",
    "pymedphys._trf",
    "pymedphys._trf.decode",
    "pymedphys._trf.manage",
    "pymedphys._utilities",
    "pymedphys._utilities.algorithms",
    "pymedphys._utilities.constants",
    "pymedphys._utilities.filehash",
    "pymedphys._utilities.transforms",
    "pymedphys._vendor",
    "pymedphys._vendor.apipkg",
    "pymedphys._vendor.pylinac",
    "pymedphys._vendor.pylinac.core",
    "pymedphys._wlutz",
    "pymedphys.beta",
    "pymedphys.cli",
    "pymedphys.cli.experimental",
    "pymedphys.docs",
    "pymedphys.docs.theme",
    "pymedphys.experimental",
    "pymedphys.tests",
    "pymedphys.tests.coordinates",
    "pymedphys.tests.delivery",
    "pymedphys.tests.dicom",
    "pymedphys.tests.dicom.rtplan",
    "pymedphys.tests.dicom.structure",
    "pymedphys.tests.e2e",
    "pymedphys.tests.experimental",
    "pymedphys.tests.experimental.film",
    "pymedphys.tests.experimental.mapcheck",
    "pymedphys.tests.experimental.mephysto",
    "pymedphys.tests.experimental.paulking",
    "pymedphys.tests.experimental.paulking.film",
    "pymedphys.tests.experimental.paulking.test_coll",
    "pymedphys.tests.experimental.pinnacle",
    "pymedphys.tests.experimental.profiler",
    "pymedphys.tests.experimental.pseudonymisation",
    "pymedphys.tests.gamma",
    "pymedphys.tests.logfiles",
    "pymedphys.tests.logging",
    "pymedphys.tests.losslessjpeg",
    "pymedphys.tests.metersetmap",
    "pymedphys.tests.mocks",
    "pymedphys.tests.monaco",
    "pymedphys.tests.trf",
    "pymedphys.tests.utilities",
    "pymedphys.tests.winstonlutz",
]

package_data = {
    "": ["*"],
    "pymedphys._experimental": ["serviceplans/templates/*", "streamlit/apps/data/*"],
    "pymedphys.docs": [
        "_static/*",
        "background/*",
        "contributing/*",
        "howto/*",
        "howto/advanced/*",
        "howto/gamma/*",
        "img/*",
        "ref/*",
        "ref/cli/*",
        "ref/gui/*",
        "ref/lib/*",
        "ref/lib/experimental/*",
        "tutes/*",
    ],
    "pymedphys.tests": [
        "dicom/data/rtplan/*",
        "dicom/scratch/*",
        "e2e/cypress/*",
        "e2e/cypress/fixtures/.gitignore",
        "e2e/cypress/integration/streamlit/*",
        "e2e/cypress/plugins/*",
        "e2e/cypress/support/*",
        "experimental/mephysto/data/baselines/*",
        "experimental/mephysto/data/measurements/*",
        "experimental/paulking/film/data/*",
    ],
}

extras_require = {
    ':python_version >= "3.6" and python_version < "3.7"': ["dataclasses"],
    "comparables": ["flashgamma"],
    "dev": [
        "tqdm",
        "attrs",
        "watchdog",
        "keyring",
        "packaging",
        "PyYAML",
        "requests",
        "numpy>=1.12",
        "matplotlib",
        "scipy",
        "pandas>=1.0.0",
        "Pillow",
        "imageio",
        "shapely>=1.7.0",
        "pydicom>=2.0.0",
        "pynetdicom",
        "pylibjpeg-libjpeg",
        "pymssql",
        "pylinac==2.3.2",
        "python_dateutil",
        "scikit-image",
        "dbfread",
        "xmltodict",
        "streamlit==0.73.1",
        "timeago",
        "sphinx<3.4.0",
        "jupyter-book>=0.8.3",
        "sphinx-argparse",
        "sphinxcontrib-napoleon",
        "sphinx-book-theme",
        "sphinxcontrib-bibtex<2.0.0",
        "pytest",
        "pytest-sugar",
        "hypothesis",
        "psutil",
        "pylint",
        "pytest-pylint",
        "pytest-rerunfailures",
        "pre-commit",
        "black>=19.3b0,<20.0",
        "mypy",
        "rope",
        "doc8",
        "tomlkit",
        "readme-renderer",
    ],
    "dicom": ["pydicom>=2.0.0", "pynetdicom", "pylibjpeg-libjpeg"],
    "docs": [
        "sphinx<3.4.0",
        "jupyter-book>=0.8.3",
        "sphinx-argparse",
        "sphinxcontrib-napoleon",
        "sphinx-book-theme",
        "sphinxcontrib-bibtex<2.0.0",
    ],
    "doctests": [
        "tensorflow>=2.2.0",
        "sphinx-book-theme",
        "sphinxcontrib-bibtex<2.0.0",
        "black>=19.3b0,<20.0",
        "tomlkit",
    ],
    "ml": ["tensorflow>=2.2.0", "torch>=1.7.1"],
    "tests": [
        "pytest",
        "pytest-sugar",
        "hypothesis",
        "psutil",
        "pylint",
        "pytest-pylint",
        "pytest-rerunfailures",
    ],
    "user": [
        "tqdm",
        "attrs",
        "watchdog",
        "keyring",
        "packaging",
        "PyYAML",
        "requests",
        "numpy>=1.12",
        "matplotlib",
        "scipy",
        "pandas>=1.0.0",
        "Pillow",
        "imageio",
        "shapely>=1.7.0",
        "pydicom>=2.0.0",
        "pynetdicom",
        "pylibjpeg-libjpeg",
        "pymssql",
        "pylinac==2.3.2",
        "python_dateutil",
        "scikit-image",
        "dbfread",
        "xmltodict",
        "streamlit==0.73.1",
        "timeago",
    ],
}

entry_points = {
    "console_scripts": ["pymedphys = pymedphys.__main__:main"],
    "sphinx.html_themes": ["sphinx_pymedphys_theme = pymedphys.docs.theme"],
}

setup_kwargs = {
    "name": "pymedphys",
    "version": "0.36.0.dev0",
    "description": "Medical Physics library",
    "long_description": "|logo|\n\n.. |logo| image:: https://github.com/pymedphys/pymedphys/raw/ca501275227f190a77e641a75af925d9070952b6/lib/pymedphys/docs/_static/pymedphys_title.svg\n    :target: https://docs.pymedphys.com/\n\n\n.. START_OF_DOCS_IMPORT\n\n\n**A community effort to develop an open standard library for Medical Physics\nin Python. Building quality transparent software together via peer review\nand open source distribution. Open code is better science.**\n\n|streamlit| |build| |docs| |pypi| |python| |license|\n\n.. |streamlit| image:: https://static.streamlit.io/badges/streamlit_badge_black_white.svg\n    :target: https://share.streamlit.io/pymedphys/pymedphys/main/app.py\n\n.. |build| image:: https://img.shields.io/github/workflow/status/pymedphys/pymedphys/PullRequest\n    :target: https://github.com/pymedphys/pymedphys/actions\n\n.. |docs| image:: https://img.shields.io/netlify/c702e3b2-f436-46a3-b461-00a8a55bcdba\n    :target: https://app.netlify.com/sites/pymedphys/deploys\n\n.. |pypi| image:: https://img.shields.io/pypi/v/pymedphys\n    :target: https://pypi.org/project/pymedphys/\n\n.. |python| image:: https://img.shields.io/pypi/pyversions/pymedphys\n    :target: https://pypi.org/project/pymedphys/\n\n.. |license| image:: https://img.shields.io/pypi/l/pymedphys\n    :target: https://choosealicense.com/licenses/apache-2.0/\n\n\nWhat is PyMedPhys?\n------------------\n\nAn open-source Medical Physics python library with a focus on being\na place to share, review, improve, and transparently learn off of each\nother's code. It is inspired by the collaborative work of our physics peers\nin astronomy and their `Astropy Project`_. PyMedPhys is available on `PyPI`_\nand `GitHub`_.\n\n.. _`Astropy Project`: http://www.astropy.org/\n.. _`PyPI`: https://pypi.org/project/pymedphys/\n.. _`GitHub`: https://github.com/pymedphys/pymedphys\n\n\nMailing list\n------------\n\nIf you would like to dive into the community a great place to get started is\nto sign up to `the mailing list`_ and say hi by introducing yourself with\nwhere you're from, and what you hope to achieve with PyMedPhys.\n\n.. _`the mailing list`: https://groups.google.com/g/pymedphys\n\n\nBeta level of development\n-------------------------\n\nPyMedPhys is currently within the ``beta`` stage of its life-cycle. It will\nstay in this stage until the version number leaves ``0.x.x`` and enters\n``1.x.x``. While PyMedPhys is in ``beta`` stage, **no API is guaranteed to be\nstable from one release to the next.** In fact, it is very likely that the\nentire API will change multiple times before a ``1.0.0`` release. In practice,\nthis means that upgrading ``pymedphys`` to a new version will possibly break\nany code that was using the old version of pymedphys. We try to be abreast of\nthis by providing details of any breaking changes from one release to the next\nwithin the `Release Notes`_.\n\n\n\nDocumentation\n-------------\n\nFor App Users\n.............\n\nDocumentation of the PyMedPhys application's graphical user interface doesn't\nyet exist. Watch this space.\n\nFor Python Users\n................\n\n- Absolute Beginners Tutorial **[Doesn't yet exist]**\n\n  - Start here if you are new to Python and would like an in-depth instruction on\n    how to get started.\n\n- `Quickstart How-To Guide`_\n\n  - Start here if you are fluent in Python and just want a quick instruction on how\n    to get started.\n\n- `Tutorials`_\n\n  - A range of lessons that take you through various complete projects with the\n    intent to be able to show you what can be achieved with writing PyMedPhys based\n    Python software yourself.\n  - These are aimed at you if you don't yet know what you can achieve with\n    PyMedPhys but you would like to learn.\n\n- `How-To Guides`_\n\n  - Guides and recipes for common problems and tasks. These are aimed for you if\n    you already know how to use Python and PyMedPhys and are looking for direction\n    on a specific task you are trying to solve.\n\n- `Reference`_\n\n  - Technical reference for the `library`_ (modules, functions and classes),\n    as well as the available `command line tools`_. This is where you will find\n    listed information for the exposed functionality of PyMedPhys.\n  - This is aimed at you if you know exactly the feature you would like to use, you\n    just want to see what inputs it requires and what outputs it gives.\n\n- `Background`_\n\n  - Explanation and discussion of key topics and concepts. This is aimed at you if\n    you are looking to be able to think about PyMedPhys and its implementations at\n    a higher level and understand more about them.\n\n- Glossary **[Doesn't yet exist]**\n\n  - List of the most important terms\n\n\nFor Contributors\n................\n\n- `Getting Started Contributing`_ **[Under construction]**\n\n  - Start here for learning how to contribute to PyMedPhys.\n\n- Developer Guide **[Doesn't yet exist]**\n- `Documentation Guide`_\n\n  - How to contribute to this documentation.\n\n- Maintainers Guide **[Doesn't yet exist]**\n\n\nOur Team\n--------\n\nPyMedPhys is what it is today due to its maintainers and contributors both past\nand present. Here is our team.\n\nMaintainers\n...........\n\n* `Simon Biggs`_\n    * `Riverina Cancer Care Centre`_, Australia\n\n.. _`Simon Biggs`: https://github.com/SimonBiggs\n\n* `Stuart Swerdloff`_\n    * `ELEKTA Pty Ltd`_: New Zealand\n\n.. _`Stuart Swerdloff`: https://github.com/sjswerdloff\n\n|rccc| |sjs|\n\nActive contributors\n...................\n\n* `Phillip Chlap`_\n    * `University of New South Wales`_, Australia\n    * `Ingham Institute`_, Australia\n\n.. _`Phillip Chlap`: https://github.com/pchlap\n\n* `Matthew Cooper`_\n\n.. _`Matthew Cooper`: https://github.com/matthewdeancooper\n\n* `Jake Rembish`_\n    * `UT Health San Antonio`_, USA\n\n.. _`Jake Rembish`: https://github.com/rembishj\n\n* `Pedro Martinez`_\n    * `University of Calgary`_, Canada\n    * `Tom Baker Cancer Centre`_, Canada\n\n.. _`Pedro Martinez`: https://github.com/peterg1t\n\n* `Rafael Ayala`_\n    * `Hospital General Universitario Gregorio Marañón`_, Spain\n\n.. _`Rafael Ayala`: https://github.com/ayalalazaro\n\n\n|uth| |uoc| |hgugm|\n\n\nMaintainer emeritus\n...................\n\n* `Matthew Jennings`_\n    * `Royal Adelaide Hospital`_, Australia\n\n.. _`Matthew Jennings`: https://github.com/Matthew-Jennings\n\n|rah|\n\nPast contributors\n.................\n\n* `Matthew Sobolewski <https://github.com/msobolewski>`_\n* `Paul King <https://github.com/kingrpaul>`_\n* `Jacob McAloney <https://github.com/JacobMcAloney>`_\n\n\n.. |rccc| image:: https://github.com/pymedphys/pymedphys/raw/3f8d82fc3b53eb636a75336477734e39fa406110/docs/logos/rccc_200x200.png\n    :target: `Riverina Cancer Care Centre`_\n\n.. |rah| image:: https://github.com/pymedphys/pymedphys/raw/3f8d82fc3b53eb636a75336477734e39fa406110/docs/logos/gosa_200x200.png\n    :target: `Royal Adelaide Hospital`_\n\n.. |uoc| image:: https://github.com/pymedphys/pymedphys/raw/363b544281aab282a56b297dc8fdd521233c6a63/logos/uoc_200x200.png\n    :target: `University of Calgary`_\n\n.. |uth| image:: https://github.com/pymedphys/pymedphys/raw/3f8d82fc3b53eb636a75336477734e39fa406110/docs/logos/UTHSA_logo.png\n    :target: `UT Health San Antonio`_\n\n.. |hgugm| image:: https://github.com/pymedphys/pymedphys/raw/3f8d82fc3b53eb636a75336477734e39fa406110/docs/logos/HGUGM_200x200.png\n    :target: `Hospital General Universitario Gregorio Marañón`_\n\n.. |sjs| image:: https://github.com/pymedphys/pymedphys/raw/7e9204656e0468b0843533472553a03a99387386/logos/swerdloff.png\n    :target: `Swerdloff Family`_\n\n.. _`Riverina Cancer Care Centre`: https://www.riverinacancercare.com.au/\n\n.. _`ELEKTA Pty Ltd`: https://www.elekta.com/\n\n.. _`Royal Adelaide Hospital`: https://www.rah.sa.gov.au/\n\n.. _`University of New South Wales`: https://www.unsw.edu.au/\n\n.. _`South Western Sydney Local Health District`: https://www.swslhd.health.nsw.gov.au/\n\n.. _`Anderson Regional Cancer Center`: https://www.andersonregional.org/services/cancer-care/\n\n.. _`Northern Beaches Cancer Care`: https://www.northernbeachescancercare.com.au/\n\n.. _`University of Calgary`: https://www.ucalgary.ca/\n\n.. _`Tom Baker Cancer Centre`: https://www.ahs.ca/tbcc\n\n.. _`UT Health San Antonio`: https://www.uthscsa.edu/academics/biomedical-sciences/programs/radiological-sciences-phd\n\n.. _`Hospital General Universitario Gregorio Marañón`: https://www.comunidad.madrid/hospital/gregoriomaranon/\n\n.. _`Swerdloff Family`: https://github.com/sjswerdloff\n\n.. _`Ingham Institute`: https://inghaminstitute.org.au/\n\n.. END_OF_DOCS_IMPORT\n\n.. _`Tutorials`: https://docs.pymedphys.com/tutes\n\n.. _`How-To Guides`: https://docs.pymedphys.com/howto\n.. _`Quickstart How-To Guide`: https://docs.pymedphys.com/howto/get-started\n\n.. _`Reference`: https://docs.pymedphys.com/ref\n.. _`Background`: https://docs.pymedphys.com/background\n\n.. _`library`: https://docs.pymedphys.com/ref/lib\n.. _`command line tools`: https://docs.pymedphys.com/ref/cli\n\n.. _`Release Notes`: ./CHANGELOG.md\n.. _`Getting Started Contributing`: ./CONTRIBUTING.md\n.. _`Documentation Guide`: https://docs.pymedphys.com/howto/advanced/documentation.rst\n",
    "author": "PyMedPhys Contributors",
    "author_email": "developers@pymedphys.com",
    "maintainer": None,
    "maintainer_email": None,
    "url": "https://pymedphys.com",
    "package_dir": package_dir,
    "packages": packages,
    "package_data": package_data,
    "extras_require": extras_require,
    "entry_points": entry_points,
    "python_requires": ">=3.6.2,<4.0.0",
}


setup(**setup_kwargs)
