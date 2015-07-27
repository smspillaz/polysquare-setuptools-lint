# /test/test_polysquare_lint.py
#
# Tests for polysquare-setuptools-lint.
#
#
# See /LICENCE.md for Copyright information
"""Tests for polysquare-setuptools-lint."""

import errno

import os

import shutil

from mock import Mock

from tempfile import mkdtemp

import polysquare_setuptools_lint
from polysquare_setuptools_lint import PolysquareLintCommand

from setuptools import Distribution
from setuptools import find_packages as fp

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

    def _open_module_file(self):
        """Open test file and return it as a file object."""
        return _open_file_force_create(os.path.join(os.getcwd(),
                                                    self._package_name,
                                                    "module.py"),
                                       "w")

    # no-self-use is suppressed here to keep consistency
    # with _open_module_file.
    #
    # suppress(no-self-use)
    def _open_test_file(self):
        """Open test file and return it as a file object."""
        return _open_file_force_create(os.path.join(os.getcwd(),
                                                    "test",
                                                    "test.py"),
                                       "w")

    # no-self-use is suppressed here to keep consistency
    # with _open_module_file.
    #
    # suppress(no-self-use)
    def _open_setup_file(self):
        """Open setup file and return it as a file object."""
        return _open_file_force_create(os.path.join(os.getcwd(),
                                                    "setup.py"),
                                       "w")

    def setUp(self):  # suppress(N802)
        """Create a temporary directory and put some files in it."""
        super(TestPolysquareLintCommand, self).setUp()
        os.environ["_POLYSQUARE_SETUPTOOLS_LINT_TESTING"] = "1"
        self._previous_directory = os.getcwd()

        project_directory = mkdtemp(prefix=os.path.join(os.getcwd(),
                                                        "test_project_dir"))
        os.chdir(project_directory)

        def cleanup_func():
            """Change into the previous dir and remove the project dir."""
            os.chdir(self._previous_directory)
            shutil.rmtree(project_directory)

        self.addCleanup(cleanup_func)
        self.patch(polysquare_setuptools_lint, "sys_exit", Mock())

        with self._open_test_file():
            pass

        with self._open_module_file():
            pass

        with self._open_setup_file() as f:
            # Write a very basic /setup.py file so that pyroma doesn't trip
            # and throw an exception.
            f.write("from setuptools import setup\n"
                    "setup()\n")

        self._distribution = Distribution(dict(name="my-package",
                                               version="0.0.1",
                                               packages=fp(exclude=["test"])))

    def test_one(self):
        """Test one."""
        PolysquareLintCommand()
