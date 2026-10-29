Example Page
============

Some example content using the theme.

Code
----

.. code-block:: python

   import ccpbiosim_sphinx_theme

   print(ccpbiosim_sphinx_theme.__version__)

Admonitions
-----------

.. note::

   This is a note.

.. warning::

   This is a warning.

Tables
------

.. list-table::
   :header-rows: 1

   * - Option
     - Default
   * - ``--input``
     - none
   * - ``--output``
     - ``results.txt``

Cards
-----

.. grid:: 1 2 2 2
   :gutter: 3

   .. grid-item-card:: Installation
      :link: index
      :link-type: doc

      Install with Conda or pip.

   .. grid-item-card:: User Guide
      :link: index
      :link-type: doc

      How to run the software.

Tabs
----

.. tab-set::

   .. tab-item:: Conda

      .. code-block:: bash

         conda install -c conda-forge my-project

   .. tab-item:: pip

      .. code-block:: bash

         pip install my-project
