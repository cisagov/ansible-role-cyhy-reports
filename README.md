# ansible-role-cyhy-reports #

[![GitHub Build Status](https://github.com/cisagov/ansible-role-cyhy-reports/workflows/build/badge.svg)](https://github.com/cisagov/ansible-role-cyhy-reports/actions)
[![CodeQL](https://github.com/cisagov/ansible-role-cyhy-reports/workflows/CodeQL/badge.svg)](https://github.com/cisagov/ansible-role-cyhy-reports/actions/workflows/codeql-analysis.yml)

An Ansible role for installing
[cisagov/cyhy-reports](https://github.com/cisagov/cyhy-reports).

## Pre-requisites (Ignore Until the COOL Migration) ##

In order to execute the Molecule tests for this Ansible role in GitHub
Actions, a build user must exist in AWS. The accompanying Terraform
code will create the user with the appropriate name and
permissions. This only needs to be run once per project, per AWS
account. This user can also be used to run the Molecule tests on your
local machine.

Before the build user can be created, you will need a profile in your
AWS credentials file that allows you to read and write your remote
Terraform state.  (You almost certainly do not want to use local
Terraform state for this long-lived build user.)  If the build user is
to be created in the CISA COOL environment, for example, then you will
need the `cool-terraform-backend` profile.

The easiest way to set up the Terraform remote state profile is to
make use of our
[`aws-profile-sync`](https://github.com/cisagov/aws-profile-sync)
utility. Follow the usage instructions in that repository before
continuing with the next steps, and note that you will need to know
where your team stores their remote profile data in order to use
[`aws-profile-sync`](https://github.com/cisagov/aws-profile-sync).

To create the build user, follow these instructions:

```console
cd terraform
terraform init --upgrade=true
terraform apply
```

Once the user is created you will need to update the [repository's
secrets](https://help.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets)
with the new encrypted environment variables. This should be done
using the
[`terraform-to-secrets`](https://github.com/cisagov/development-guide/tree/develop/project_setup#terraform-iam-credentials-to-github-secrets-)
tool available in the [development
guide](https://github.com/cisagov/development-guide). Instructions for
how to use this tool can be found in the ["Terraform IAM Credentials
to GitHub Secrets"
section](https://github.com/cisagov/development-guide/tree/develop/project_setup#terraform-iam-credentials-to-github-secrets-).
of the Project Setup README.

If you have appropriate permissions for the repository you can view
existing secrets on the [appropriate
page](https://github.com/cisagov/ansible-role-cyhy-reports/settings/secrets) in
the repository's settings.

## Requirements ##

None.

## Role Variables ##

> **Note**
> Any variables that are not required, but have no default value, are used to
> control the creation of optional resources. They [use a filter to default to
> `false`](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_filters.html#providing-default-values)
> for use in conditionals so that unneeded resources are not created.

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| cyhy_reports_file_owner_group | The name of the group that should own any non-system files or directories created by this role. | [Omitted](https://docs.ansible.com/ansible/latest/user_guide/playbooks_filters.html#making-variables-optional) | No |
| cyhy_reports_file_owner_username | The name of the user that should own any non-system files or directories created by this role. | [Omitted](https://docs.ansible.com/ansible/latest/user_guide/playbooks_filters.html#making-variables-optional) | No |
| cyhy_reports_maxmind_license_key | The MaxMind license key that provides access to a GeoIP2 database subscription. | n/a | Yes |
| cyhy_reports_texmf_buffer_size | The value to use for the texmf buffer size. | n/a | No |
| cyhy_reports_texmf_main_memory | The value to use for the texmf main memory size. | n/a | No |

## Dependencies ##

- [cisagov/ansible-role-cyhy-core](https://github.com/cisagov/ansible-role-cyhy-core)
- [cisagov/ansible-role-ncats-webd](https://github.com/cisagov/ansible-role-ncats-webd)
- [cisagov/ansible-role-pip](https://github.com/cisagov/ansible-role-pip)
- [cisagov/ansible-role-python](https://github.com/cisagov/ansible-role-python)

## Example Playbook ##

Here's how to use it in a playbook:

```yaml
- hosts: all
  become: true
  become_method: sudo
  tasks:
    - name: Install cisagov/cyhy-reports
      ansible.builtin.include_role:
        name: cyhy_reports
```

## Contributing ##

We welcome contributions!  Please see [`CONTRIBUTING.md`](CONTRIBUTING.md) for
details.

## License ##

This project is in the worldwide [public domain](LICENSE).

This project is in the public domain within the United States, and
copyright and related rights in the work worldwide are waived through
the [CC0 1.0 Universal public domain
dedication](https://creativecommons.org/publicdomain/zero/1.0/).

All contributions to this project will be released under the CC0
dedication. By submitting a pull request, you are agreeing to comply
with this waiver of copyright interest.

## Author Information ##

Shane Frasier - <jeremy.frasier@gwe.cisa.dhs.gov>
