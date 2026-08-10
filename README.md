# ansible-role-cyhy-reports #

[![GitHub Build Status](https://github.com/cisagov/ansible-role-cyhy-reports/workflows/build/badge.svg)](https://github.com/cisagov/ansible-role-cyhy-reports/actions)
[![License](https://img.shields.io/github/license/cisagov/ansible-role-cyhy-reports)](https://spdx.org/licenses/)
[![CodeQL](https://github.com/cisagov/ansible-role-cyhy-reports/workflows/CodeQL/badge.svg)](https://github.com/cisagov/ansible-role-cyhy-reports/actions/workflows/codeql-analysis.yml)

An Ansible role for installing
[cisagov/cyhy-reports](https://github.com/cisagov/cyhy-reports).

## Requirements ##

None.

## Role Variables ##

> **Note**
> Any variables that are not required, but have no default value, are used to
> control the creation of optional resources. They [use a filter to default to
> `false`](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_filters.html#providing-default-values)
> for use in conditionals so that unneeded resources are not created.

| Variable | Description | Default | Required |
| -------- | ----------- | ------- | -------- |
| cyhy\_reports\_cyhy\_core\_version | The version of cisagov/cyhy-core to use; must be a valid git reference. | `v1.3.2` | No |
| cyhy\_reports\_file\_owner\_group | The name of the group that should own any non-system files or directories created by this role. | [Omitted](https://docs.ansible.com/ansible/latest/user_guide/playbooks_filters.html#making-variables-optional) | No |
| cyhy\_reports\_file\_owner\_username | The name of the user that should own any non-system files or directories created by this role. | [Omitted](https://docs.ansible.com/ansible/latest/user_guide/playbooks_filters.html#making-variables-optional) | No |
| cyhy\_reports\_install\_geoipupdate | Whether to install the MaxMind geoipupdate tool. | `false` | No |
| cyhy\_reports\_maxmind\_account\_id | The MaxMind account ID for access to a GeoIP2 database subscription. | n/a | Yes |
| cyhy\_reports\_maxmind\_license\_key | The MaxMind license key that provides access to a GeoIP2 database subscription. | n/a | Yes |
| cyhy\_reports\_texmf\_buffer\_size | The value to use for the texmf buffer size. | n/a | No |
| cyhy\_reports\_texmf\_main\_memory | The value to use for the texmf main memory size. | n/a | No |
| cyhy\_reports\_version | The version of cisagov/cyhy-reports to install; must be a valid git reference. | `v2.0.1` | No |

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
