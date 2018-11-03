Ansible Role: HASS
=========

Installs [Home-Assistant](https://home-assistant.io/).

Role Variables
--------------

Available variables are listed below, along with default values (see `defaults/main.yml`):

```yaml
hass_python_path: /usr/bin/python3
hass_pip_pkgs:
  - homeassistant
  - wheel
hass_virtualenv_path: /srv/home-assistant
```

The `virtualenv` path where Home-Assistant should be installed, the path to the Python binary, and the packages that should be installed via `pip`.

```yaml
hass_user: homeassistant
```

The name of the user that Home-Assistant will run as.  This will also be the name of the group.

```yaml
hass_config_path: /home/homeassistant/.homeassistant
```

The path to the Home-Assistant configuration file.

```yaml
hass_pip3:
```

The path to pip3 on the server.

```yaml
hass_os_pkgs:
```

The OS packages that need to be installed on the server.  This includes the Python 3 packages.


Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in
regards to parameters that may need to be set for other roles, or variables that
are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: ansible-role-hass, x: 42 }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a
website (HTML is not allowed).
