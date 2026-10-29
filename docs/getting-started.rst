Getting started
===============

Install the theme
-----------------

Add the theme to ``docs/requirements.txt``, or to the ``docs`` group in
``pyproject.toml``:

.. code-block:: text

   ccpbiosim-sphinx-theme>=1.0,<2.0

Allowing any ``1.x`` release means your documentation picks up theme updates
on its next build, with no change to your repository.

Turn it on
----------

In ``conf.py``, set the theme and the name of your GitHub repository:

.. code-block:: python

   html_theme = "ccpbiosim_sphinx_theme"
   html_context = {"github_repo": "my-project"}

That is all most projects need. You can remove any Furo settings, such as
``html_theme_options`` with ``light_logo`` and ``dark_logo``.

What you get
------------

* the CCPBioSim logo in the header, with ``project`` from ``conf.py`` beside it
* GitHub, CCPBioSim docs and ccpbiosim.org icons in the header
* an "Edit on GitHub" button on every page
* a search box, light and dark mode, and an "On this page" panel
* previous and next page buttons, and a CCPBioSim footer
* `sphinx-design <https://sphinx-design.readthedocs.io/>`_ cards, buttons and
  tabs, and copy buttons on code blocks

You do not need to add ``sphinx_design`` or ``sphinx_copybutton`` to
``extensions``; the theme turns them on.

Next steps
----------

* Give your project a home page with a banner and section cards:
  :doc:`home-page`.
* Change any defaults, or add icons to the header: :doc:`configuration`.

Moving from Furo
----------------

Most CCPBioSim projects started from the Python template, which uses Furo.
To switch:

#. Replace ``furo`` with ``ccpbiosim-sphinx-theme>=1.0,<2.0`` in your docs
   requirements.
#. In ``conf.py``, set ``html_theme`` and ``html_context`` as above, and
   remove the Furo ``html_theme_options``.
#. If ``conf.py`` lives in ``docs/`` rather than ``docs/source/``, also set
   ``"doc_path": "docs"`` in ``html_context`` so the edit buttons link to the
   right files.
#. Optionally, rebuild your ``index.rst`` as described in :doc:`home-page`.
#. Build with ``make html SPHINXOPTS="-W --keep-going"`` to check for
   warnings.
