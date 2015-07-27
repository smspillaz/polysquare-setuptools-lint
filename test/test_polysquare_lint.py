# /test/test_polysquare_lint.py
#
# Tests for polysquare-setuptools-lint.
#
#
# See /LICENCE.md for Copyright information
"""Tests for polysquare-setuptools-lint."""

import errno

import os

from testtools import TestCase


def _open_file_force_create(path, mode="w"):
    """Force creation of file at path and open it."""
    try:
        os.makedirs(os.path.dirname(path))
    except OSError as error:
        if error.errno != errno.EEXIST:
            raise error

    with open(os.path.join(os.path.dirname(path), "__init__.py"), "w"):
        pass

    return open(path, mode)


class TestPolysquareLintCommand(TestCase):

    """Tests for the PolysquareLintCommand class."""

    def __init__(self, *args, **kwargs):
        """Initialize this test case."""
        super(TestPolysquareLintCommand, self).__init__(*args, **kwargs)
        self._previous_directory = None
        self._package_name = "package"
        self._distribution = None
