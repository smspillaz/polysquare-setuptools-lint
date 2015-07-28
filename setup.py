# /setup.py
#
# Installation and setup script for polysquare-setuptools-lint
#
# See /LICENCE.md for Copyright information
"""Installation and setup script for polysquare-setuptools-lint."""

try:
    from polysquare_setuptools_lint import PolysquareLintCommand
    _CMDCLASS = {
        "polysquarelint": PolysquareLintCommand
    }

except ImportError:
    _CMDCLASS = dict()

import platform

import sys

from setuptools import (find_packages, setup)

if (not (platform.python_implementation() == "PyPy" and
         sys.version_info.major == 3) and
        platform.system() != "Windows"):
    _ADDITIONAL_LINTERS = ["frosted"]
else:
    _ADDITIONAL_LINTERS = list()


setup(name="polysquare-setuptools-lint",
      version="0.0.18",
      description="""Provides a 'polysquarelint' command for setuptools""",
      long_description_markdown_filename="README.md",
      author="Sam Spilsbury",
      author_email="smspillaz@gmail.com",
      url="http://github.com/polysquare/polysquare-setuptools-lint",
      classifiers=["Development Status :: 3 - Alpha",
                   "Programming Language :: Python :: 2",
                   "Programming Language :: Python :: 2.7",
                   "Programming Language :: Python :: 3",
                   "Programming Language :: Python :: 3.1",
                   "Programming Language :: Python :: 3.2",
                   "Programming Language :: Python :: 3.3",
                   "Programming Language :: Python :: 3.4",
                   "Intended Audience :: Developers",
                   "Topic :: Software Development :: Build Tools",
                   "License :: OSI Approved :: MIT License"],
      license="MIT",
      keywords="development linters",
      packages=find_packages(exclude=["test"]),
      cmdclass=_CMDCLASS,
      install_requires=[
          "setuptools",
          "jobstamps>=0.0.8",
          "parmap",
          "pep8",
          "dodgy",
          "mccabe",
          "pep257",
          "pyflakes",
          "pylint-common",
          "pyroma",
          "vulture",
          "logilab-common==0.63.0",
          "prospector>=0.10.1",
          "flake8==2.3.0",
          "flake8-blind-except",
          "flake8-docstrings",
          "flake8-double-quotes",
          "flake8-import-order",
          "flake8-todo",
          "six"
      ] + _ADDITIONAL_LINTERS,
      extras_require={
          "green": [
              "mock",
              "nose",
              "nose-parameterized",
              "setuptools-green",
              "testtools"
          ],
          "upload": ["setuptools-markdown"]
      },
      entry_points={
          "distutils.commands": [
              ("polysquarelint=polysquare_setuptools_lint:"
               "PolysquareLintCommand"),
          ]
      },
      zip_safe=True,
      include_package_data=True)
