"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize(
    "f",
    [
        # The systemd service unit for generating CyHy reports
        "/etc/systemd/system/run-cyhy-reports.service",
        # The systemd timer unit for generating CyHy reports
        "/etc/systemd/system/run-cyhy-reports.timer",
        # The shell script for generating CyHy reports
        "/usr/local/sbin/run-cyhy-reports.sh",
    ],
)
def test_files(host, f):
    """Test that the expected files and directories are present."""
    assert host.file(f).exists


@pytest.mark.parametrize(
    "svc",
    [
        # The systemd timer unit for generating CyHy reports
        "run-cyhy-reports.timer",
    ],
)
def test_services(host, svc):
    """Test that the expected units were enabled as intended."""
    svc = host.service(svc)
    assert svc.is_enabled
