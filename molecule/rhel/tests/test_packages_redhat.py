"""Package related tests for RedHat."""
import os

import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('centos7')


@pytest.mark.parametrize("name,version", [
    ("python36u", "3.6"),
    ("python36u-pip", "9"),
    ("python36u-devel", "3.6"),
    ("python36u-setuptools", "39"),
    ("python-setuptools", "0.9"),
])
def test_rpm_packages(host, name, version):
    """Test that rpm based packages are present.

    Arguments:
        host {fixture} -- Pytest fixture that provides access to modules.
        name {str} -- Name of package.
        version {str} -- Version of package that should be installed.
    """
    p = host.package(name)

    assert p.is_installed
    assert p.version.startswith(version)
