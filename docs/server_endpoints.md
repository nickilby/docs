# Server Management API Endpoints

This module provides API endpoints for managing servers within different environments. It supports operations such as cloning, deleting, and creating servers.

## Dependencies
- `flask_cors` for enabling Cross-Origin Resource Sharing (CORS)
- `flasgger.utils.swag_from` for API documentation
- `flask` for request handling
- `http.HTTPStatus` for standardized HTTP response codes
- `distutils.util` for type conversion
- `automation_rest.cloud_api.decorators.fetch_environment` for environment fetching
- `flask_api_v1_v2.authentication.is_global_administrator` for authentication
- `flask_api_v1_v2.handlers.server` for server operations

## Blueprint Configuration

A Flask blueprint is used to define the API routes. CORS is enabled for these endpoints, allowing cross-domain requests from browser-based applications.

```python
BLUEPRINT = _trailing_slash_blueprint.TrailingSlashBlueprint("servers", __name__)
flask_cors.CORS(
    BLUEPRINT,
    max_age=21600,
    allow_headers=["X-Security-Token", "Content-Type"],
)
```

## Endpoints

### Delete a Server
```http
DELETE /environments/<alias>/servers/<server>
```

#### Description
Deletes a specified server from an environment.

#### Authorization
- Requires global administrator privileges.

#### Parameters
- `alias` (str): Identifier of the environment.
- `server` (str): Name of the server to be deleted.

#### Response
- `200 OK`: Server deleted successfully.
- `404 Not Found`: Server not found.

#### Example Response
```json
{
  "msg": "Server deleted successfully",
  "tasks_executed": [...],
  "success": true
}
```

### Create a Server
```http
POST /environments/<alias>/servers/<server>/create
```

#### Description
Creates a new server in the specified environment.

#### Parameters
- `alias` (str): Identifier of the environment.
- `server` (str): Name of the new server.

#### Response
- JSON response from `server_handler.create_environment_server`.

### Clone a Server
```http
POST /environments/<alias>/servers/<server>/copy
```

#### Description
Creates a clone of an existing server.

#### Authorization
- Requires global administrator privileges.

#### Parameters
- `alias` (str): Identifier of the environment.
- `server` (str): Name of the server to be cloned.
- `skip_deployment` (bool, optional): If `true`, skips deployment during cloning.

#### Response
- `200 OK`: Server cloned successfully.
- `422 Unprocessable Entity`: Cloning failed.

#### Example Response
```json
{
  "msg": "Server cloned successfully",
  "tasks_executed": [...],
  "success": true,
  "server": {...}
}
```

## Notes
- The `skip_deployment` parameter is converted to a boolean. If invalid, it defaults to `false`.
- The `server_handler` module handles the core logic for server operations.
- API documentation is available via `flasgger` annotations.

This module ensures a robust and secure way to manage servers within environments using Flask-based APIs.

