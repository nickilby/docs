# SAS Library Documentation

## Overview

The `sas_lib.py` file is a Python module designed for managing cloud-based environments, particularly for Contensis CMS automation. It provides functions to handle environment configurations, server management, authentication, subnet allocation, and deployment automation. The script integrates with Contensis cloud services and automation REST APIs.

## Dependencies

The module relies on several third-party libraries:

- `flask` - Handles API requests and responses.
- `jinja2` - Provides templating capabilities.
- `netaddr` - Used for IP address and subnet management.
- `yaml` and `json` - Reads and writes configuration data.
- `arrow` - Handles date-time manipulations.
- `bs4 (BeautifulSoup)` - Parses and manipulates HTML data.
- `ansi2html` - Converts ANSI-colored text to HTML.
- `automation_rest` - Interacts with cloud APIs for automation.

## Key Features

### 1. **Environment Management**

The script allows users to create, retrieve, and update environment configurations.

#### Functions:

- `get_environment_configuration(ans_base_path, alias)`: Fetches environment details.
- `get_environment(ans_base_path, alias, user_info)`: Returns environment configuration if the user has permissions.
- `update_environment_state(ans_base_path, alias, state)`: Updates the state of an environment.
- `create_environment(ans_base_path, environment)`: Creates a new environment.

### 2. **Server Management**

Provides utilities to allocate, configure, and modify cloud servers.

#### Functions:

- `ensure_server(ans_base_path, role_name, alias, simulate, count)`: Ensures a specific number of servers exist for a given role.
- `ensure_elastic_server(ans_base_path, alias, simulate, count, force=False, drive_size=800)`: Ensures elastic servers are properly allocated.
- `update_server_vm_fields(ans_base_path, alias, check_mode, server_name, fields)`: Updates multiple fields of a server.

### 3. **Authentication & Security**

Checks permissions and generates secure passwords for system use.

#### Functions:

- `can_view_environment(user_info, environment)`: Determines if a user has permission to view an environment.
- `can_admin_environment(user_info, environment)`: Checks if a user has admin access.
- `generate_password(length=16)`: Generates a secure random password.
- `get_password()`: Retrieves a generated password.

### 4. **Data Handling**

Manages reading, writing, and caching of environment data.

#### Functions:

- `load_data_json(filename)`: Reads data from a JSON file.
- `save_data_json(filename, data)`: Writes data to a JSON file.
- `load_data_yml(filename)`: Reads YAML configuration data.
- `save_data_yml(filename, data)`: Writes YAML configuration data.

### 5. **Subnet & Network Management**

Handles allocation and management of IP addresses and subnets.

#### Functions:

- `allocate_subnet(ans_base_path, name, alias, pod)`: Allocates a subnet to an environment.
- `get_free_ip_count(ans_base_path, full_subnet)`: Counts available IPs in a subnet.
- `get_shared_cloud_subnet_entity_exact(ans_base_path, pod, alias)`: Retrieves shared cloud subnet details.

### 6. **Deployment & Infrastructure**

Automates Kubernetes pod configurations and server deployments.

#### Functions:

- `save_pod_data(ans_base_path, pod_name, data)`: Saves configuration data for a Kubernetes pod.
- `get_pod_config(ans_base_path, pod_name)`: Retrieves configuration details for a specific pod.
- `regenerate_pod_inventory(ans_base_path, pod_name)`: Rebuilds inventory files for a Kubernetes pod.

## Usage Guide

### **Setting Up the Environment**

Before using the script, ensure that the necessary dependencies are installed:

```bash
pip install flask jinja2 netaddr yaml arrow bs4 ansi2html
```

### **Creating a New Environment**

To create a new environment, use:

```python
from sas_lib import create_environment

environment_config = {
    "alias": "new-environment",
    "pod": "hq",
    "size": "standard",
    "type": "contensis",
    "owner": "admin_user",
}

new_env = create_environment("/path/to/ansible", environment_config)
print(new_env)
```

### **Fetching an Existing Environment**

To get details about a specific environment:

```python
from sas_lib import get_environment_configuration

env_data = get_environment_configuration("/path/to/ansible", "existing-alias")
print(env_data)
```

### **Updating Server Configurations**

To modify server details within an environment:

```python
from sas_lib import update_server_vm_fields

fields = {"guest_memory": 8192, "guest_cpu_count": 4}
result = update_server_vm_fields("/path/to/ansible", "env-alias", False, "server-name", fields)
print(result)
```

### **Allocating a Subnet**

To assign a subnet to an environment:

```python
from sas_lib import allocate_subnet

allocated = allocate_subnet("/path/to/ansible", "subnet-name", "env-alias", "pod")
print(allocated)
```

## Best Practices

1. **Use Secure Passwords**: Always generate passwords using `generate_password()` rather than hardcoding them.
2. **Validate Permissions**: Before making changes, use functions like `can_view_environment()` to ensure proper authorization.
3. **Cache Data**: To improve performance, utilize `load_data_json()` and `cachedJson()` instead of reading files multiple times.
4. **Maintain Consistent Naming**: Use meaningful and descriptive names for environments, servers, and network components.
5. **Regularly Backup Configuration Files**: Before making changes, store backups of `hosts/vars/*.json` and `config/*.yml`.

## Conclusion

The `sas_lib.py` module is a powerful tool for managing cloud infrastructure and automating deployments for Contensis CMS. By leveraging its robust functions, administrators can efficiently create, manage, and modify cloud environments with minimal manual effort. Understanding the key functions and usage patterns will help ensure smooth operations and scalability in managing cloud-based services.

