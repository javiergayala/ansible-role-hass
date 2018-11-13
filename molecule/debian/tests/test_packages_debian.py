"""Package related tests for Debian."""
import os

import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("name,version", [
    ("python3", "3"),
    ("python3-pip", "9"),
    ("python3-dev", "3"),
    ("python3-setuptools", "3"),
    ("python-setuptools", "3"),
])
<<<<<<< HEAD
def test_os_packages(host, name, version):
=======
def test_rpm_packages(host, name, version):
>>>>>>> 320a0fd03f50db5a3e72d2e98b33125c3fa01450
    """Test that rpm based packages are present.

    Arguments:
        host {fixture} -- Pytest fixture that provides access to modules.
        name {str} -- Name of package.
        version {str} -- Version of package that should be installed.
    """
    p = host.package(name)

    assert p.is_installed
    assert p.version.startswith(version)
