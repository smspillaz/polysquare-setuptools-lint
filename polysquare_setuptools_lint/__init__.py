# /polysquare_setuptools_lint/__init__.py
#
# Provides a setuptools command for running pyroma, prospector and
# flake8 with maximum settings on all distributed files and tests.
#
# See /LICENCE.md for Copyright information
"""Provide a setuptools command for linters."""

import setuptools


class PolysquareLintCommand(setuptools.Command):  # suppress(unused-function)

    """Provide a lint command."""

    def __init__(self, *args, **kwargs):
        """Initialize this class' instance variables."""
        setuptools.Command.__init__(self, *args, **kwargs)
        self._file_lines_cache = None
        self.stamp_directory = None
        self.suppress_codes = None
        self.exclusions = None
        self.initialize_options()

    def run(self):  # suppress(unused-function)
        """Run linters."""
        pass

    def initialize_options(self):  # suppress(unused-function)
        """Set all options to their initial values."""
        pass

    def finalize_options(self):  # suppress(unused-function)
        """Finalize all options."""
        pass
