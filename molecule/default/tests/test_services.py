"""Service related tests."""
import os

import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("name", [
    "appdaemon",
    "home-assistant"
])
def test_service_files(host, name):
    """Test that the systemd service files are present.

    Arguments:
        host {fixture} -- Pytest fixture that provides access to modules.
        name {str} -- Name of service.
    """
    f = host.file('/etc/systemd/system/%s@homeassistant.service' % name)

    assert f.exists


# @pytest.mark.parametrize("name", [
#     "appdaemon",
#     "home-assistant"
# ])
# def test_service(host, name):
#     """Test that the systemd services are enabled.

#     Arguments:
#         host {fixture} -- Pytest fixture that provides access to modules.
#         name {str} -- Name of service.
#     """
#     s = host.service('%s@homeassistant.service' % name)

#     assert s.is_enabled
