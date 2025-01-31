# Environment API Documentation

This module provides API endpoints for managing environments. It includes functionalities such as checking availability, deploying, scaling, shrinking, and deleting environments. Additionally, it provides endpoints for retrieving status, configuration, and FTP information.

## Dependencies
- `flask`, `flask_cors` for request handling and CORS support
- `flasgger.utils` for API documentation
- `http.HTTPStatus` for standardized HTTP response codes
- `automation_rest` modules for automation and security
- `pkg_config`, `pkg_platform` modules for environment configurations

## Blueprint Configuration

A Flask blueprint is used to define API routes with CORS enabled to allow browser-based applications access.

```python
BLUEPRINT = _trailing_slash_blueprint.TrailingSlashBlueprint("environment", __name__)
flask_cors.CORS(
    BLUEPRINT,
    max_age=21600,
    allow_headers=["X-Security-Token", "Content-Type"],
)
```

## Endpoints

### Check Environment Availability
```http
GET /environments/<alias>/is_available
```
#### Description
Checks if the suggested alias is available.

#### Response
- `200 OK`: `{ "ok": true/false }`

### Deploy Environment
```http
POST /environments/<alias>/deploy
```
#### Description
Deploys an environment based on its type.

#### Authorization
- Requires administrator privileges.

#### Response
- `200 OK`: `{ "tasks_executed": [...], "success": true }`

### Scale Environment
```http
POST /environments/<alias>/scale
```
#### Description
Scales an environment by adding nodes.

#### Authorization
- Requires administrator privileges.

#### Response
- `200 OK`: `{ "tasks_executed": [...], "success": true }`
- `422 Unprocessable Entity`: Scaling not possible.

### Shrink Environment
```http
POST /environments/<alias>/shrink
```
#### Description
Shrinks an environment by removing nodes.

#### Authorization
- Requires administrator privileges.

#### Response
- `200 OK`: `{ "tasks_executed": [...], "success": true }`
- `422 Unprocessable Entity`: Shrinking not possible.

### Deploy Sites Configuration
```http
POST /environments/<alias>/sites/deploy
```
#### Description
Deploys pending site configurations.

#### Authorization
- Requires administrator privileges.

#### Response
- `200 OK`: `{ "tasks_executed": [...], "success": true }`

### Check Environment Configuration
```http
GET /environments/<alias>/check
```
#### Description
Checks the environment configuration for issues.

#### Authorization
- Requires administrator privileges.

#### Response
- `200 OK`: `{ "validation_errors": [...] }`
- `422 Unprocessable Entity`: Configuration issues found.

### Get Environment Status
```http
GET /environments/<alias>/status
```
#### Description
Retrieves the status of an environment.

#### Authorization
- Requires administrator privileges.

#### Response
- `200 OK`: `{ "status": {...} }`

### Get FTP Information
```http
GET /environments/<alias>/ftp_info
```
#### Description
Retrieves FTP configuration details for an environment.

#### Response
- `200 OK`: `{ "ip": "...", "enabled": true/false }`

### Create Environment
```http
POST /environments/create
```
#### Description
Creates a new environment.

#### Authorization
- Requires global administrator privileges.

#### Response
- `200 OK`: `{ "success": true, "msg": "..." }`

### Delete Environment
```http
DELETE /environments/<alias>
```
#### Description
Deletes an existing environment.

#### Authorization
- Requires administrator privileges.

#### Response
- `200 OK`: `{ "success": true, "tasks_executed": [...] }`

### Clone Environment
```http
POST /environments/clone
```
#### Description
Creates a development or test clone of an environment.

#### Authorization
- Requires administrator privileges.

#### Response
- `200 OK`: `{ "success": true, "tasks_executed": [...] }`

### Edit Environment Configuration
```http
PATCH /environments/<alias>
POST /environments/<alias>/edit
```
#### Description
Modifies environment settings.

#### Authorization
- Requires administrator privileges.

#### Response
- `200 OK`: `{ "success": true, "updated_keys": {...} }`

### Get List of Environments
```http
GET /environments
```
#### Description
Retrieves a list of all environments.

#### Authorization
- Requires authentication.

#### Response
- `200 OK`: `{ "environments": [...] }`

### Get User Environments
```http
GET /environments/my
```
#### Description
Retrieves environments associated with the authenticated user.

#### Authorization
- Requires authentication.

#### Response
- `200 OK`: `{ "environments": [...] }`

### Get Environment Configuration
```http
GET /environment/<alias>
```
#### Description
Retrieves the configuration of a specific environment.

#### Authorization
- Requires authentication.

#### Response
- `200 OK`: `{ "environment": {...} }`

## Notes
- The module ensures secure access to environment data and operations.
- API documentation is maintained via `flasgger` annotations.
- The API enables automation and orchestration of cloud environments efficiently.

This documentation provides an overview of environment API handlers and their functionalities.

