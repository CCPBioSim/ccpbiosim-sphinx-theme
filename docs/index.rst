:html_theme.sidebar_secondary.remove:

ccpbiosim-sphinx-theme
======================

.. ccpbiosim-hero::
   :logo: _static/CCPBioSim-logo-white-bottom-text.svg
   :logo-alt: CCPBioSim logo
   :tagline: Sphinx theme for CCPBioSim documentation
   :button: example | Example page
   :github: CCPBioSim/ccpbiosim-sphinx-theme

The shared Sphinx theme for CCPBioSim projects, based on
`pydata-sphinx-theme <https://pydata-sphinx-theme.readthedocs.io/>`_ and
styled to match `ccpbiosim.org <https://www.ccpbiosim.org/>`_.

Installation
------------

Add the theme to your docs requirements:

.. code-block:: text

   ccpbiosim-sphinx-theme>=1.0,<2.0

Usage
-----

Set the theme in ``conf.py``:

.. code-block:: python

   html_theme = "ccpbiosim_sphinx_theme"
   html_context = {"github_repo": "my-project"}

The banner at the top of this page is added with:

.. code-block:: rst

   .. ccpbiosim-hero::
      :logo: _static/logo.svg
      :tagline: A short description of the project
      :button: installation | Get started
      :github: CCPBioSim/my-project

.. toctree::
   :hidden:

   example
