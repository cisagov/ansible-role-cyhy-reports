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
    "pkg",
    [
        "python-mpltoolkits.basemap",
        "python-numpy",
        "python-dateutil",
        "python-netaddr",
        "python-pandas",
        "python-progressbar",
        "python-docopt",
        "python-unicodecsv",
        "python-pypdf2",
        "rsync",
        "texlive",
        "texlive-fonts-extra",
        "texlive-latex-extra",
        "texlive-science",
        "texlive-xetex",
    ],
)
def test_apt_packages(host, pkg):
    """Test that the apt packages were installed."""
    assert host.package(pkg).is_installed


@pytest.mark.parametrize("pkg", ["cyhy-reports"])
def test_pip_packages(host, pkg):
    """Test that the pip packages were installed."""
    assert pkg in host.pip.get_packages(pip_path="/usr/bin/pip2")


@pytest.mark.parametrize(
    "f",
    [
        "/usr/local/share/fonts",
        "/var/local/cyhy/reports",
        "/var/cyhy/reports",
        "/var/cyhy/reports/output",
        "/var/cyhy/reports/create_snapshots_reports_scorecard.py",
        "/var/cyhy/reports/create_send_notifications.py",
    ],
)
def test_files(host, f):
    """Test that the expected files and directories are present."""
    assert host.file(f).exists


def test_texmf_configuration(host):
    """Test that the texmf configuration was modified as expected."""
    cmd = host.run("kpsewhich texmf.cnf")
    assert cmd.rc == 0
    texmf_config_filename = cmd.stdout.strip()
    texmf_config_file = host.file(texmf_config_filename)
    assert texmf_config_file.exists
    assert texmf_config_file.is_file
    # Note that File.contains() does not use Python's re library but
    # instead runs grep behind the scenes:
    # https://github.com/pytest-dev/pytest-testinfra/blob/main/testinfra/modules/file.py#L118-L119
    #
    # Therefore the regex string here must be able to be passed to
    # grep without any quotes around it.  This is the reason I do not
    # use an r-string and use two backslashes before the plus.
    assert texmf_config_file.contains("buf_size=[[:digit:]]\\+")
