# ansible-role-cyhy-reports #

[![GitHub Build Status](https://github.com/cisagov/ansible-role-cyhy-reports/workflows/build/badge.svg)](https://github.com/cisagov/ansible-role-cyhy-reports/actions)
[![License](https://img.shields.io/github/license/cisagov/ansible-role-cyhy-reports)](https://spdx.org/licenses/)
[![CodeQL](https://github.com/cisagov/ansible-role-cyhy-reports/workflows/CodeQL/badge.svg)](https://github.com/cisagov/ansible-role-cyhy-reports/actions/workflows/codeql-analysis.yml)

An Ansible role for installing
[cisagov/cyhy-reports](https://github.com/cisagov/cyhy-reports).

## Pre-requisites (Ignore Until the COOL Migration) ##

In order to execute the Molecule tests for this Ansible role in GitHub Actions,
a test user must exist in AWS. The accompanying Terraform code will create the
user with the appropriate name and permissions. This only needs to be run once
per project, per AWS account. This user can also be used to run the Molecule
tests on your local machine.

Before the test user can be created, you will need a profile in your AWS
credentials file that allows you to read and write your remote Terraform state.
(You almost certainly do not want to use local Terraform state for this
long-lived test user.)  If the test user is to be created in the CISA COOL
environment, for example, then you will need the `cool-terraform-backend`
profile.

The easiest way to set up the Terraform remote state profile is to make use of
our [`aws-profile-sync`](https://github.com/cisagov/aws-profile-sync) utility.
Follow the usage instructions in that repository before continuing with the next
steps, and note that you will need to know where your team stores their remote
profile data in order to use
[`aws-profile-sync`](https://github.com/cisagov/aws-profile-sync).

### Creating a test user ###

You will need to create a test user for each environment that you use.  The
following steps show how to create a test user for an environment named "dev".
You will need to repeat this process for any additional environments.

1. Change into the `terraform` directory:

   ```console
   cd terraform
   ```

1. Create a backend configuration file named `dev.tfconfig` containing the
name of the bucket where "dev" environment Terraform state is stored - this file
is required to initialize the Terraform backend in each environment:

    ```hcl
    bucket = "my-dev-terraform-state-bucket"
    ```

1. Initialize the Terraform backend for the "dev" environment using your backend
   configuration file:

    ```console
    terraform init -backend-config=dev.tfconfig
    ```

    > [!NOTE]
    > When performing this step for additional environments (i.e. not your first
    > environment), use the `-reconfigure` flag:
    >
    > ```console
    > terraform init -backend-config=other-env.tfconfig -reconfigure
    > ```

1. Create a Terraform variables file named `dev.tfvars` containing all
required variables (currently only `terraform_state_bucket`):

    ```hcl
    terraform_state_bucket = "my-dev-terraform-state-bucket"
    ```

1. Create a Terraform workspace for the "dev" environment:

    ```console
   terraform workspace new dev
   ```

1. Initialize and upgrade the Terraform workspace, then apply the configuration
   to create the test user in the "dev" environment:

    ```console
    terraform init -upgrade=true
    terraform apply -var-file=dev.tfvars
    ```

Once the test user is created you will need to update the
[repository's secrets](https://help.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets)
with the new encrypted environment variables. This should be done using the
[`terraform-to-secrets`](https://github.com/cisagov/development-guide/tree/develop/project_setup#terraform-iam-credentials-to-github-secrets-)
tool available in the
[development guide](https://github.com/cisagov/development-guide). Instructions
for how to use this tool can be found in the
["Terraform IAM Credentials to GitHub Secrets" section](https://github.com/cisagov/development-guide/tree/develop/project_setup#terraform-iam-credentials-to-github-secrets-).
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
| cyhy\_reports\_cyhy\_core\_version | The version of cisagov/cyhy-core to use; must be a valid git reference. | `v1.1.14` | No |
| cyhy\_reports\_file\_owner\_group | The name of the group that should own any non-system files or directories created by this role. | [Omitted](https://docs.ansible.com/ansible/latest/user_guide/playbooks_filters.html#making-variables-optional) | No |
| cyhy\_reports\_file\_owner\_username | The name of the user that should own any non-system files or directories created by this role. | [Omitted](https://docs.ansible.com/ansible/latest/user_guide/playbooks_filters.html#making-variables-optional) | No |
| cyhy\_reports\_install\_geoipupdate | Whether to install the MaxMind geoipupdate tool. | `false` | No |
| cyhy\_reports\_maxmind\_account\_id | The MaxMind account ID for access to a GeoIP2 database subscription. | n/a | Yes |
| cyhy\_reports\_maxmind\_license\_key | The MaxMind license key that provides access to a GeoIP2 database subscription. | n/a | Yes |
| cyhy\_reports\_texmf\_buffer\_size | The value to use for the texmf buffer size. | n/a | No |
| cyhy\_reports\_texmf\_main\_memory | The value to use for the texmf main memory size. | n/a | No |
| cyhy\_reports\_version | The version of cisagov/cyhy-reports to install; must be a valid git reference. | `v1.1.1` | No |

## Dependencies ##

- [cisagov/ansible-role-cyhy-core](https://github.com/cisagov/ansible-role-cyhy-core)
- [cisagov/ansible-role-ncats-webd](https://github.com/cisagov/ansible-role-ncats-webd)
- [cisagov/ansible-role-pip](https://github.com/cisagov/ansible-role-pip)
- [cisagov/ansible-role-python](https://github.com/cisagov/ansible-role-python)

## Installation ##

This role can be installed via the command:

```console
ansible-galaxy install --role-file path/to/requirements.yml
```

where `requirements.yml` looks like:

```yaml
---
- name: cyhy_reports
  src: https://github.com/cisagov/ansible-role-cyhy-reports
```

and may contain other roles as well.

For more information about installing Ansible roles via a YAML file,
please see [the `ansible-galaxy`
documentation](https://docs.ansible.com/ansible/latest/galaxy/user_guide.html#installing-multiple-roles-from-a-file).

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
