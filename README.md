ccpbiosim-sphinx-theme
==============================

| Category       | Badges |
|----------------|--------|
| **Build**      | [![PR Checks](https://github.com/CCPBioSim/ccpbiosim-sphinx-theme/actions/workflows/pr.yaml/badge.svg)](https://github.com/CCPBioSim/ccpbiosim-sphinx-theme/actions/workflows/pr.yaml) [![Weekly Tests](https://github.com/CCPBioSim/ccpbiosim-sphinx-theme/actions/workflows/weekly-tests.yaml/badge.svg)](https://github.com/CCPBioSim/ccpbiosim-sphinx-theme/actions/workflows/weekly-tests.yaml) |
| **Documentation** | [![Weekly Docs](https://github.com/CCPBioSim/ccpbiosim-sphinx-theme/actions/workflows/weekly-docs.yaml/badge.svg)](https://github.com/CCPBioSim/ccpbiosim-sphinx-theme/actions/workflows/weekly-docs.yaml) [![Docs - Status](https://app.readthedocs.org/projects/ccpbiosim-sphinx-theme/badge/?version=latest)](https://ccpbiosim-sphinx-theme.readthedocs.io/en/latest/?badge=latest) |
| **PyPI**       | [![PyPI - Version](https://img.shields.io/pypi/v/ccpbiosim-sphinx-theme.svg)](https://pypi.org/project/ccpbiosim-sphinx-theme/) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ccpbiosim-sphinx-theme.svg)](https://pypi.org/project/ccpbiosim-sphinx-theme/) |
| **Quality**    | [![Coverage Status](https://coveralls.io/repos/github/CCPBioSim/ccpbiosim-sphinx-theme/badge.svg?branch=main)](https://coveralls.io/github/CCPBioSim/ccpbiosim-sphinx-theme?branch=main) |

The Sphinx theme used across CCPBioSim projects. It is built on [pydata-sphinx-theme](https://pydata-sphinx-theme.readthedocs.io/) and uses the same colours and fonts as [ccpbiosim.org](https://www.ccpbiosim.org/).

An example site using the theme is available at [ccpbiosim-sphinx-theme.readthedocs.io](https://ccpbiosim-sphinx-theme.readthedocs.io/).

## Installation

Add the theme to your docs requirements:

```text
ccpbiosim-sphinx-theme>=1.0,<2.0
```

## Usage

Set the theme in `conf.py`:

```python
html_theme = "ccpbiosim_sphinx_theme"
html_context = {"github_repo": "my-project"}
```

This adds the CCPBioSim header, footer and colours, the GitHub link and the "Edit on GitHub" buttons. sphinx-design and sphinx-copybutton are enabled by the theme, so they do not need adding to `extensions`.

If `conf.py` is in `docs/` rather than `docs/source/`, also set `"doc_path": "docs"` in `html_context`. Anything set in `html_theme_options` or `html_context` takes priority over the theme defaults.

To add a banner to the home page, put this under the page title:

```rst
.. ccpbiosim-hero::
   :logo: _static/logo.svg
   :tagline: A short description of the project
   :button: installation | Get started
   :github: CCPBioSim/my-project
```

## Development

```bash
pip install -e ".[testing,pre-commit]"
pytest
```

## Releasing

Releases are made by running the **Release ccpbiosim-sphinx-theme** workflow from the Actions tab. This updates the version, tags the release and publishes it to PyPI.

Projects use any `1.x` release automatically, so use a minor or patch release for changes that should reach every project. Use a new major version for changes that need projects to update their `conf.py`.

## Contact Information

For questions or problems, please contact CCPBIOSIM@stfc.ac.uk.
