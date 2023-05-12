"""pytest plugin configuration.

https://docs.pytest.org/en/latest/writing_plugins.html#conftest-py-plugins
"""
# Third-Party Libraries
import pytest


def pytest_configure(config):
    """Set up the values to be shared in the pytest cache."""
    config.stash["buffer_size_cnf"] = "/etc/texmf/texmf.d/99buffer_size.cnf"
    config.stash["main_memory_cnf"] = "/etc/texmf/texmf.d/99main_memory.cnf"


@pytest.fixture(scope="module")
def texmf_config_file(host):
    """Retrieve the texmf configuration file."""
    cmd = host.run("kpsewhich texmf.cnf")
    assert cmd.rc == 0
    texmf_config_filename = cmd.stdout.strip()
    texmf_config_file = host.file(texmf_config_filename)
    assert texmf_config_file.exists
    assert texmf_config_file.is_file
    return texmf_config_file
