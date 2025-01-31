# Server Handlers Documentation

This module provides handlers for cloning, deleting, and managing servers within different environments. It includes logic for server creation, IP allocation, and Elasticsearch server management.

## Dependencies
- `copy` for deep copying objects
- `re` for regex operations
- `six` for Python 2 and 3 compatibility
- `automation_rest.config` for configuration settings
- `automation_rest.playbook_runner` for executing playbooks
- `automation_rest.sas_lib` for handling server automation scripts
- `automation_rest.cloud_api.models` for server models
- `automation_rest.cloud_api.util` for utility functions
- `automation_rest.cloud_api.networking` for IP allocation and subnet retrieval

## Constants and Matrices

### Base Image OS Mapping
Defines the mapping between OS versions and their base images.

### Elasticsearch Configuration Matrices
Defines role, resource, server name, and base image mappings for Elasticsearch versions.

## Functions

### `search_contensis_major_version_matrix(version, matrix, ascending=False)`
Searches for the correct Contensis version mapping from a given matrix.

### `create_elasticsearch(root_path, environment, preparation=False, version=None)`
Creates an Elasticsearch server based on the provided environment configuration.

#### Parameters
- `root_path` (str): The root path for server data.
- `environment` (dict): The environment details.
- `preparation` (bool, optional): Whether this is a preparation step.
- `version` (int, optional): Specific version of Contensis.

#### Returns
- `(bool, str)`: Success flag and role name.

### `internal_delete_server(alias, environment, server_name)`
Deletes a specified server from an environment.

#### Parameters
- `alias` (str): Environment alias.
- `environment` (dict): Environment details.
- `server_name` (str): Name of the server to delete.

#### Returns
- `(bool, list)`: Success flag and list of executed tasks.

### `generate_server_name_copy(environment, name)`
Generates a unique name for a copied server to avoid conflicts.

### `copy_environment_server(alias, environment, server, skip_deployment)`
Clones a server in the environment.

#### Parameters
- `alias` (str): Environment alias.
- `environment` (dict): Environment details.
- `server` (str): Name of the server to clone.
- `skip_deployment` (bool): Whether to skip the deployment process.

#### Returns
- `dict`: Cloning success status and new server details.

### `create_environment_server(alias: str, server: str) -> dict`
Creates a new server.

#### Parameters
- `alias` (str): Environment alias.
- `server` (str): Name of the new server.

#### Returns
- `dict`: Success status and message.

## Notes
- The module ensures the correct allocation of resources based on predefined matrices.
- Cloning functions generate unique names and allocate necessary resources automatically.
- API interactions depend on playbook execution and automation scripts for provisioning.

This documentation provides an overview of the server handler module and its critical functionalities.

