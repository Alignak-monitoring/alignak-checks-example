#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import re
del os.link
from importlib import import_module

try:
    from setuptools import setup, find_packages
except:
    sys.exit("Error: missing python-setuptools library")

try:
    python_version = sys.version_info
except:
    python_version = (1, 5)
if python_version < (2, 7):
    sys.exit("This application requires a minimum Python 2.7.x, sorry!")
elif python_version >= (3,):
    sys.exit("This application is not yet compatible with Python 3.x, sorry!")

# Define installation paths
# Get Alignak root installation directory
if os.path.exists("/usr/local/etc/alignak"):
    alignak_etc_path = "/usr/local/etc/alignak"
elif os.path.exists("/etc/alignak"):
    alignak_etc_path = "/etc/alignak"
else:
    print "Alignak etc not found: does not seem to be installed on this host!"
    exit(1)

# Define plugins paths
# Get Alignak libexec directory
if os.path.exists("/usr/local/etc/alignak"):
    alignak_libexec_path = "/usr/local/libexec/alignak"
elif os.path.exists("/etc/alignak"):
    alignak_libexec_path = "/usr/local/var/lib/alignak"
elif os.path.exists("/etc/alignak"):
    alignak_libexec_path = "/var/lib/alignak"
else:
    print "Alignak libexec not found: does not seem to be installed on this host!"
    exit(2)

# Import pack information
from alignak_checks_glances import __version__, __author__, __author_email__, __copyright__
from alignak_checks_glances import __license__, __url__, __checks_type__
from alignak_checks_glances import __name__ as __pkg_name__
package = import_module(__pkg_name__)

# Define installation paths
# Get Alignak root installation directory
alignak_etc_path = os.path.join(alignak_etc_path, 'arbiter_cfg', 'objects', 'packs', __checks_type__)
# Get Alignak libexec directory
# alignak_libexec_path = os.path.join(alignak_libexec_path, __pkg_name__)

# Build list of all installable package files
pack_files = []
plugins_files = []
for subdir, dirs, files in os.walk(__pkg_name__):
    if subdir and 'plugins' in subdir:
        for subdir, dirs, files in os.walk(os.path.join(__pkg_name__, 'plugins')):
            for file in files:
                print 'plugin: ' + file
                if not file.startswith('__'):
                    plugins_files.append(os.path.join(subdir, file))
    for file in files:
        if not file.startswith('__'):
            pack_files.append(os.path.join(subdir, file))


setup(
    name=__pkg_name__,
    version=__version__,

    # Metadata for PyPI
    author=__author__,
    author_email=__author_email__,
    keywords="alignak monitoring pack checks " + __checks_type__,
    url=__url__,
    license=__license__,
    description=package.__doc__.strip(),
    long_description=open('README.rst').read(),

    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Topic :: System :: Monitoring',
        'Topic :: System :: Systems Administration'
    ],

    # Unzip Egg
    zip_safe=False,

    # Package data
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': 'README.rst',
        '': 'AUTHORS',
        '': 'LICENSE',
        '': [os.path.join(__pkg_name__, '*')],
    },

    # Where to install which file ...
    # All pack files are installed at the same place.
    data_files = [
        (alignak_libexec_path, plugins_files),
        (alignak_etc_path, pack_files)
    ],

    # Dependencies (if some) ...
    install_requires=[''],

    # Entry points (if some) ...
    entry_points={
    }
)
