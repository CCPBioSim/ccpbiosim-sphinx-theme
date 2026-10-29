Configuration
=============

The theme is a child of
`pydata-sphinx-theme <https://pydata-sphinx-theme.readthedocs.io/>`_, so every
pydata option works. Anything you set in ``conf.py`` wins over the theme's
defaults.

html_context
------------

.. list-table::
   :header-rows: 1
   :widths: 25 25 50

   * - Key
     - Default
     - Meaning
   * - ``github_repo``
     - none
     - Repository name. Turns on the GitHub icon and edit buttons.
   * - ``github_user``
     - ``CCPBioSim``
     - GitHub organisation or user.
   * - ``github_version``
     - ``main``
     - Branch the edit buttons point at.
   * - ``doc_path``
     - ``docs/source``
     - Folder holding ``conf.py``, relative to the repository root.

html_theme_options
------------------

The theme sets these defaults:

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Option
     - Default
   * - ``logo``
     - CCPBioSim logo, with ``project`` as the text beside it
   * - ``icon_links``
     - GitHub (if ``github_repo`` is set), CCPBioSim docs, ccpbiosim.org
   * - ``use_edit_page_button``
     - on if ``github_repo`` is set
   * - ``navbar_align``
     - ``left``
   * - ``header_links_before_dropdown``
     - ``6``
   * - ``show_toc_level``
     - ``2``
   * - ``show_prev_next``
     - on
   * - ``footer_start``
     - ``["copyright"]``
   * - ``footer_end``
     - ``["ccpbiosim-footer"]``
   * - ``ccpbiosim_hub_url``
     - ``https://ccpbiosim.readthedocs.io/``

Common changes
--------------

Change the name beside the logo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   html_theme_options = {"logo": {"text": "My project"}}

Only the keys you give are changed; the CCPBioSim logo stays.

Add icons to the header
~~~~~~~~~~~~~~~~~~~~~~~

Your icons are added after the shared ones. Icons use
`Font Awesome <https://fontawesome.com/search?ic=free>`_ names.

.. code-block:: python

   html_theme_options = {
       "icon_links": [
           {
               "name": "Anaconda",
               "url": "https://anaconda.org/ccpbiosim/my-project",
               "icon": "fa-solid fa-box",
           },
       ],
   }

Hide the left sidebar
~~~~~~~~~~~~~~~~~~~~~

If none of your pages have sub-pages, the left sidebar is always empty.
Hide it with:

.. code-block:: python

   html_sidebars = {"**": []}

Edit buttons for docs in ``docs/``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   html_context = {"github_repo": "my-project", "doc_path": "docs"}

Colours
-------

The colours come from ccpbiosim.org and are set as CSS variables in the
theme. To keep every project consistent, change them in this repository
rather than in a single project.

.. list-table::
   :header-rows: 1
   :widths: 30 20 50

   * - Variable
     - Value
     - Used for
   * - ``--ccp-teal``
     - ``#1d7989``
     - Header bar, links, headings
   * - ``--ccp-teal-dark``
     - ``#0e3b43``
     - Link hover
   * - ``--ccp-sky``
     - ``#27aadf``
     - Buttons
   * - ``--ccp-navy``
     - ``#0f172a``
     - Banner, footer, dark mode background
   * - ``--ccp-navy-deep``
     - ``#001b4c``
     - Banner gradient
