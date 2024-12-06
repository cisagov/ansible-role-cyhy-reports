"""Module containing the texmf configuration tests for the main_memory scenario."""

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
# https://github.com/pytest-dev/pytest-testinfra/blob/e1eb9c11beb8042ae7c7a0f0ef3a0160eaa7c3cd/testinfra/modules/file.py#L130-L135
#
# Therefore, the regex string values for "contents" must be able to be passed to
# grep without any quotes around it.  This is the reason I do not
# use an r-string and use two backslashes before the plus.
@pytest.mark.parametrize(
    "file_key,contents",
    [
        ("main_memory_cnf", "main_memory=[[:digit:]]\\+"),
    ],
)
def test_texmf_configuration_exists(
    file_key, contents, host, request, texmf_config_file
):
    """Test that the texmf configuration has the configured options as expected."""
    target_file = request.config.stash.get(file_key, None)
    assert target_file is not None
    custom_texmf_cnf = host.file(target_file)
    assert custom_texmf_cnf.exists
    assert custom_texmf_cnf.is_file
    assert custom_texmf_cnf.contains(contents)

    assert texmf_config_file.contains(contents)


# Note that File.contains() does not use Python's re library but
# instead runs grep behind the scenes:
# https://github.com/pytest-dev/pytest-testinfra/blob/e1eb9c11beb8042ae7c7a0f0ef3a0160eaa7c3cd/testinfra/modules/file.py#L130-L135
#
# Therefore, the regex string values for "contents" must be able to be passed to
# grep without any quotes around it.  This is the reason I do not
# use an r-string and use two backslashes before the plus.
@pytest.mark.parametrize(
    "file_key,contents",
    [
        ("buffer_size_cnf", "buf_size=[[:digit:]]\\+"),
    ],
)
def test_texmf_configuration_absent(
    file_key, contents, host, request, texmf_config_file
):
    """Test that the texmf configuration is missing unconfigured options as expected."""
    target_file = request.config.stash.get(file_key, None)
    assert target_file is not None
    custom_texmf_cnf = host.file(target_file)
    assert custom_texmf_cnf.exists is False

    assert texmf_config_file.contains(contents) is False
