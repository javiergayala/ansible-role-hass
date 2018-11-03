"""Package related tests for RedHat."""
import os

import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("name", [
    "homeassistant",
    "wheel"
])
def test_pip_packages(host, name):
    """Test that PIP based packages are present.

    Arguments:
        host {fixture} -- Pytest fixture that provides access to modules.
        name {str} -- Name of package.
    """
    pkgs = host.pip_package.get_packages(
        pip_path='/srv/home-assistant/bin/pip3')

    assert name in pkgs
