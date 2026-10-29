Style guide
===========

This page shows how common content looks with the theme. Use it to check
changes to the theme in light and dark mode.

Headings
--------

Page titles and third-level headings are teal. Second-level headings, like
"Headings" above, have a rule underneath.

A third-level heading
~~~~~~~~~~~~~~~~~~~~~

Body text uses the same fonts as ccpbiosim.org. Here is a
`link <https://www.ccpbiosim.org/>`_, some **bold** and *italic* text, and
``inline code``.

Code
----

.. code-block:: python

   import ccpbiosim_sphinx_theme

   print(ccpbiosim_sphinx_theme.__version__)

.. code-block:: bash

   my-project --help

Notes and warnings
------------------

.. note::

   A note, for helpful extra information.

.. tip::

   A tip, for a better way to do something.

.. warning::

   A warning, for something that could go wrong.

.. danger::

   A danger notice, for something that could lose data.

Tables
------

.. list-table::
   :header-rows: 1

   * - Option
     - Default
     - Description
   * - ``--input``
     - none
     - File to read
   * - ``--output``
     - ``results.txt``
     - File to write
   * - ``--verbose``
     - off
     - Print progress messages

Tabs
----

.. tab-set::

   .. tab-item:: Conda

      .. code-block:: bash

         conda install -c conda-forge example

   .. tab-item:: pip

      .. code-block:: bash

         pip install example

Buttons
-------

.. button-ref:: getting-started
   :ref-type: doc
   :color: primary

   A primary button

.. button-link:: https://www.ccpbiosim.org/
   :color: primary
   :outline:

   An outline button

Dropdowns
---------

.. dropdown:: Click to show more

   Hidden content, useful for long output or optional detail.
