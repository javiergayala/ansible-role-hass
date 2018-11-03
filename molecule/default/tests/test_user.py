"""User related tests."""
import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_user(host):
    """Test that user exists and is configured properly.

    Arguments:
        host {fixture} -- Pytest fixture that provides access to modules.
    """
    u = host.user('homeassistant')

    assert u.exists
    assert u.name == 'homeassistant'
    assert u.group == 'homeassistant'


def test_group(host):
    """Test that group exists and is configured properly.

    Arguments:
        host {fixture} -- Pytest fixture that provides access to modules.
    """
    g = host.group('homeassistant')

    assert g.exists
