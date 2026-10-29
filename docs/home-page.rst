Home page
=========

A CCPBioSim home page has three parts: a banner, a short introduction, and a
grid of cards linking to each section. See this site's
:doc:`home page <index>` for the finished result.

Banner
------

The ``ccpbiosim-hero`` directive adds the dark navy banner. Put it directly
under the page title. The title is hidden on the page because the banner
replaces it, but it is still used for the browser tab and navigation.

.. code-block:: rst

   My project
   ==========

   .. ccpbiosim-hero::
      :logo: _static/logo-white-text.svg
      :tagline: A one-line description of the project
      :button: installation | Get started
      :github: CCPBioSim/my-project

      A short summary of what the project does.

The text under the options becomes the summary. Every option is optional:

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Option
     - Meaning
   * - ``:logo:``
     - Project logo. Use the version with white text, as the banner is dark.
   * - ``:logo-alt:``
     - Alt text for the logo. Defaults to "*project* logo".
   * - ``:tagline:``
     - Large headline under the logo.
   * - ``:button:``
     - Primary button, written as ``document | Button text``. The text
       defaults to "Get started".
   * - ``:github:``
     - Adds a "View on GitHub" button for ``organisation/repository``.

Example
~~~~~~~

A banner with only a tagline, summary and GitHub button:

.. code-block:: rst

   .. ccpbiosim-hero::
      :tagline: An example project
      :github: CCPBioSim/ccpbiosim-sphinx-theme

      A banner does not need a logo.

.. ccpbiosim-hero::
   :tagline: An example project
   :github: CCPBioSim/ccpbiosim-sphinx-theme

   A banner does not need a logo.

Section cards
-------------

Under the introduction, link to each section with sphinx-design's grid cards.
``1 2 2 3`` sets the number of columns on phones, tablets, laptops and wide
screens.

.. code-block:: rst

   .. grid:: 1 2 2 3
      :gutter: 3

      .. grid-item-card:: 📦 Installation
         :link: installation
         :link-type: doc

         Install with Conda, or build from source.

      .. grid-item-card:: 🧬 User guide
         :link: user-guide
         :link-type: doc

         How to use the project, its options and output.

      .. grid-item-card:: 📚 Citing
         :link: citation
         :link-type: doc

         How to cite the software and its methods.

.. grid:: 1 2 2 3
   :gutter: 3

   .. grid-item-card:: 📦 Installation
      :link: getting-started
      :link-type: doc

      Install with Conda, or build from source.

   .. grid-item-card:: 🧬 User guide
      :link: configuration
      :link-type: doc

      How to use the project, its options and output.

   .. grid-item-card:: 📚 Citing
      :link: style-guide
      :link-type: doc

      How to cite the software and its methods.

Recommended sections
--------------------

Using the same sections in every project means users can find their way
around any CCPBioSim tool:

#. **Installation**
#. **User guide**
#. **Examples**
#. **API reference**, for Python packages
#. **Development**
#. **Citing**

Hiding the side panel
---------------------

Home pages usually look better without the "On this page" panel. Put this at
the very top of ``index.rst``:

.. code-block:: rst

   :html_theme.sidebar_secondary.remove:
