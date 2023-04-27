"""Module containing the texmf configuration tests for the default scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


# Note that File.contains() does not use Python's re library but
# instead runs grep behind the scenes:
# https://github.com/pytest-dev/pytest-testinfra/blob/main/testinfra/modules/file.py#L118-L119
#
# Therefore the regex string values for "contents" must be able to be passed to
# grep without any quotes around it.  This is the reason I do not
# use an r-string and use two backslashes before the plus.
@pytest.mark.parametrize(
    "file,contents",
    [
        ("/etc/texmf/texmf.d/99buffer_size.cnf", "buf_size=[[:digit:]]\\+"),
        ("/etc/texmf/texmf.d/99main_memory.cnf", "main_memory=[[:digit:]]\\+"),
    ],
)
def test_texmf_configuration(file, contents, host, texmf_config_file):
    """Test that the texmf configuration was not modified."""
    custom_texmf_cnf = host.file(file)
    assert custom_texmf_cnf.exists is False

    assert texmf_config_file.contains(contents) is False
