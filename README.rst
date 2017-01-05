Alignak checks package example
==============================

*This project is an example and a how-to to help building a checks pack for Alignak monitoring framework.*


.. image:: https://img.shields.io/badge/IRC-%23alignak-1e72ff.svg?style=flat
    :target: http://webchat.freenode.net/?channels=%23alignak
    :alt: Join the chat #alignak on freenode.net

.. image:: https://img.shields.io/badge/License-AGPL%20v3-blue.svg
    :target: http://www.gnu.org/licenses/agpl-3.0
    :alt: License AGPL v3


Packaging
---------

Repositories
~~~~~~~~~~~~

All Alignak packs are stored in their own repository in the `Alignak monitoring contrib`_ Github organization. For creating a new checks pack, it needs to create a new repository in this organization. Contact us on the IRC channel or send an email to discuss the matter ;)


Design and principles
~~~~~~~~~~~~~~~~~~~~~

Each pack aims to provide all the necessary elements in the Alignak configuration to monitor hosts and/or services.

Each pack includes the checks commands definitions, services templates, hosts templates, ...

It is even possible to include the monitoring plugins that will be run by Alignak to check an host/service.

Usually, the packs are only made of configuration files using the most common monitoring plugins available from the Nagios community.

The pack files are to be made available in the monitoring objects configuration directory and provide configuration utilities for the end-user:

   - hosts templates: the host "use" the pack features
   - services templates: the service "use" the pack features
   -  ...

The proposed structure to build a pack:

    * all the checks packs are named as ``alignak_checks_EXAMPLE``
    * the ``EXAMPLE`` repository is named as ``alignak-checks-EXAMPLE``
    * the ``EXAMPLE`` repository includes the following files:
        * README.rst
        * LICENCE (optional)
        * AUTHORS (optional)
        * setup.py
        * version.py

    * the ``EXAMPLE`` repository includes an ``alignak_checks_EXAMPLE`` directory containing the pack configuration files
    * the files/folders in ``alignak_checks_EXAMPLE/etc`` directory will be copied to the Alignak etc directory
    * the files/folders in ``alignak_checks_EXAMPLE/libexec`` directory will be copied to the Alignak libexec directory


Repository example
~~~~~~~~~~~~~~~~~~
Repository directories and files example:
::

    README.rst
    LICENCE
    AUTHORS
    requirements.txt
    setup.py
    version.py

    alignak_checks_EXAMPLE/
        arbiter/
            packs/
                resource.d/
                    EXAMPLE.cfg
            EXAMPLE/
                templates.cfg
                services.cfg
                groups.cfg
                commands.cfg
        etc/
            test.cfg
        plugins/
            sub/
                plugin.conf
            plugin.py

The content of the directory ``alignak_checks_EXAMPLE/etc`` (including files and sub
directories) will be copied to */usr/local/var/etc/alignak*.

The content of the directory ``alignak_checks_EXAMPLE/plugins`` (including sub directories)
will be copied to */usr/local/var/libexec/alignak*.


Building
~~~~~~~~

To build a new package EXAMPLE2:

    * create a new ``alignak-checks-EXAMPLE2`` repository which is a copy of this repository

        * rename the ``alignak_checks_EXAMPLE`` directory to ``alignak_checks_EXAMPLE2``

    * update the ``version.py`` file

        * edit the ``__pkg_name__`` and the ``checks_type`` variables (at minimum)

    * update the ``MANIFEST.in`` file

        * rename the ``alignak_checks_EXAMPLE`` directory to ``alignak_checks_EXAMPLE2``

    * update the ``README.rst`` file

        * remove this section **Packaging**
        * search and replace ``EXAMPLE`` with ``EXAMPLE2``
        * update and extend the **Documentation** chapter

    * update the ``alignak_checks_EXAMPLE2/version.py`` file with all the package information

        * ``__checks_type__`` will be used to complete the keywords in PyPI and as the sub-directory to store the pack's files
        * the file docstring will be used as the package description in PyPI

    * update the ``setup.py`` file (**not recommended**)

        * ``setup.py`` should not be modified for most of the packs ... if necessary, do it with much care!

And that's it!

Then, to build and make your package available to the community, you must use the standard Python setuptools:

    * run ``setup.py register -r pypi`` to register the new package near PyPI
    * run ``setup.py sdist -r pypi`` to build the package
    * run ``sudo pip install . -e`` to make the package installed locally (development mode)
    * run ``sudo pip uninstall -v . -e`` to remove the development mode
    * run ``sudo pip install . -v`` to make the package installed locally
    * run ``sudo pip uninstall -v alignak_checks_EXAMPLE`` to uninstall the package

When your package is ready and functional:

    * run ``python setup.py sdist upload -r pypi`` to upload the package to `PyPI repository`_.

**Note**: every time you upload a package to PyPI you will need to change the package version in the ``alignak_checks_EXAMPLE2/__init.py__`` file. You can make some tests with the `-r pypitest` ;)




Under this line, keep the content for the new built package. Remove the former *Packaging* section of this document.
-----





Installation
------------

The pack configuration files are to be copied to the monitoring objects configuration directory. The most suitable location is the *arbiter/packs/* directory in the main alignak configuration directory.

**Note**: The main Alignak configuration directory is usually */usr/local/etc/alignak* or */etc/alignak* but it may depend upon your system and/or your installation.

The pack plugins (if any ...) are to be copied to the executable libraries directories.

**Note**: The Alignak librairies directory is usually */usr/local/var/libexec/alignak* but it may depend upon your system and/or your installation.

From PyPI
~~~~~~~~~
To install the package from PyPI:
::

   sudo pip install alignak-checks-EXAMPLE


From source files
~~~~~~~~~~~~~~~~~
To install the package from the source files:
::

   git clone https://github.com/Alignak-monitoring-contrib/alignak-checks-EXAMPLE
   cd alignak-checks-EXAMPLE
   sudo pip install .

**Note:** *using `sudo python setup.py install` will not correctly manage the package configuration files! The recommended way is really to use `pip`;)*

Documentation
-------------

**To be updated/completed!**

Checks packs dependencies / installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If needed...

Configuration
~~~~~~~~~~~~~
Explain what is configurable in this checks pack.

Edit the */usr/local/etc/alignak/arbiter/packs/EXAMPLE/resources.cfg* file and configure ... bla,bla...
::

   #-- Configurable macro
   $PACK_MACRO$=qsdqsdqsd


Prepare host
~~~~~~~~~~~~
Some operations are necessary on the monitored hosts if SNMP remote access is not yet activated.
::

   # Install local SNMP agent

Alignak configuration
~~~~~~~~~~~~~~~~~~~~~

You simply have to tag the concerned hosts with the template `EXAMPLE`.
::

    define host{
        use                     EXAMPLE
        host_name               my_host
        address                 127.0.0.1
    }



Bugs, issues and contributing
-----------------------------

Contributions to this project are welcome and encouraged ... `issues in the project repository <https://github.com/alignak-monitoring-contrib/alignak-checks-EXAMPLE/issues>`_ are the common way to raise an information.

.. _Alignak monitoring contrib: https://github.com/Alignak-monitoring-contrib
.. _PyPI repository: <https://pypi.python.org/pypi>
