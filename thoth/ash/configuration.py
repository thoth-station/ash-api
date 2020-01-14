import os


class Configuration:
    """Configuration of Ash API service."""

    APP_SECRET_KEY = os.environ.get("ASH_API_APP_SECRET_KEY", None)
    SWAGGER_YAML_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../openapi")

    OPENAPI_PORT = 8080
