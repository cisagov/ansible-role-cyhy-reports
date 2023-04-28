"""pytest plugin configuration.

https://docs.pytest.org/en/latest/writing_plugins.html#conftest-py-plugins
"""
# Third-Party Libraries
import pytest


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
