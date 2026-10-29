:html_theme.sidebar_secondary.remove:

ccpbiosim-sphinx-theme
======================

.. ccpbiosim-hero::
   :logo: _static/CCPBioSim-logo-white-bottom-text.svg
   :logo-alt: CCPBioSim logo
   :tagline: One look for every CCPBioSim project's documentation
   :button: getting-started | Get started
   :github: CCPBioSim/ccpbiosim-sphinx-theme

   A Sphinx theme that matches ccpbiosim.org, so every CCPBioSim tool's
   documentation looks and works the same way.

This site is built with the theme, so everything you see here is what your
project gets: the teal header with the CCPBioSim logo, this banner, the
section cards below, light and dark mode, and the navy footer.

Quick start
-----------

.. tab-set::

   .. tab-item:: requirements.txt

      .. code-block:: text

         ccpbiosim-sphinx-theme>=1.0,<2.0

   .. tab-item:: conf.py

      .. code-block:: python

         html_theme = "ccpbiosim_sphinx_theme"
         html_context = {"github_repo": "my-project"}

Explore the documentation
-------------------------

.. grid:: 1 2 2 2
   :gutter: 3

   .. grid-item-card:: 🚀 Getting started
      :link: getting-started
      :link-type: doc

      Add the theme to a project and see what it sets up for you.

   .. grid-item-card:: 🏠 Home page
      :link: home-page
      :link-type: doc

      Build a project home page with the banner and section cards.

   .. grid-item-card:: ⚙️ Configuration
      :link: configuration
      :link-type: doc

      The theme's defaults, and how to override them.

   .. grid-item-card:: 🎨 Style guide
      :link: style-guide
      :link-type: doc

      How headings, code, notes, tables, tabs and buttons look.

.. toctree::
   :maxdepth: 2
   :hidden:

   getting-started
   home-page
   configuration
   style-guide
