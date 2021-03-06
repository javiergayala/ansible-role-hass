# Ansible Role: HASS

[![Build Status](https://travis-ci.org/javiergayala/ansible-role-hass.svg?branch=master)](https://travis-ci.org/javiergayala/ansible-role-hass)

Installs [Home-Assistant](https://home-assistant.io/) and optionally [AppDaemon](https://www.home-assistant.io/docs/ecosystem/appdaemon/).

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

```yaml
hass_python_path: /usr/bin/python3
hass_pip_pkgs:
  - homeassistant
  - wheel
hass_virtualenv_path: /srv/home-assistant
hass_appdaemon_virtualenv_path: /srv/appdaemon
```

The `virtualenv` path where Home-Assistant or AppDaemon should be installed, the path to the Python binary, and the packages that should be installed via `pip`.

```yaml
hass_pip_pkgs_appdaemon: [ appdaemon ]
```

The PIP packages that should be installed for use by AppDaemon.

```yaml
hass_user: homeassistant
```

The name of the user that Home-Assistant will run as.  This will also be the name of the group.

```yaml
hass_config_path: /home/homeassistant/.homeassistant
```

The path to the Home-Assistant configuration file.

```yaml
hass_install_appdaemon: false
```

Set to `true` to have the role install AppDaemon in addition to Home-Assistant.

```yaml
hass_use_mysql: false
```

Set to `true` to have the role install the Python `mysqlclient` PIP Package.  This is useful if you are setting your `recorder` component of HASS to use a MariaDB or MySQL server as it's backend.  

```yaml
hass_install_mariadb: false
```

Set to `true` to have the role install the MariaDB dependencies required to build and install the `mysqlclient` PIP package.  

```yaml
hass_install_mysql: false
```

Set to `true` to have the role install the MySQL dependencies required to build and install the `mysqlclient` PIP package.

```yaml
hass_common_db_pkgs: []
```

A list containing the common OS packages that need to be installed in order to successfully compile the `mysqlclient` PIP Package.  

```yaml
hass_mariadb_pkgs: []
```

A list containing the MariaDB packages that need to be installed in order to successfully compile the `mysqlclient` PIP Package.  The default includes the `hass_common_db_pkgs` list.

```yaml
hass_mysql_pkgs: []
```

A list containing the MySQL packages that need to be installed in order to successfully compile the `mysqlclient` PIP Package.  The default includes the `hass_common_db_pkgs` list.

```yaml
hass_pip3:
```

The path to pip3 on the server.

```yaml
hass_os_pkgs:
```

The OS packages that need to be installed on the server.  This includes the Python 3 packages.

```yaml
hass_update_pkgs: false
```

Set to `true` to have the role upgrade the Home-Assistant and AppDaemon PIP packages.

## Dependencies

A list of other roles hosted on Galaxy should go here, plus any details in
regards to parameters that may need to be set for other roles, or variables that
are used from other roles.

## Example Playbook

To install the role with AppDaemon:

```yaml
    - hosts: servers
      roles:
        - role: ansible-role-hass
          hass_install_appdaemon: true
```

To install the role with AppDaemon and additional PIP Packages for AppDaemon:

```yaml
    - hosts: servers
      roles:
        - role: ansible-role-hass
          hass_install_appdaemon: true
          hass_pip_pkgs_appdaemon:
            - appdaemon
            - SQLAlchemy
            - requests
```

## License

BSD

## Author Information

Javier Ayala  
http://javierayala.com/
