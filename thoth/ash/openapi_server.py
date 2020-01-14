import connexion
from connexion.resolver import RestyResolver

from thoth.ash.configuration import Configuration

app = connexion.FlaskApp(__name__, specification_dir=Configuration.SWAGGER_YAML_PATH, debug=True)

app.add_api(
    "ash-api.yaml",
    options={"swagger_ui": True},
    arguments={"title": "Ash API"},
    resolver=RestyResolver("stub.api"),
    strict_validation=True,
    validate_responses=True,
)


if __name__ == "__main__":
    app.run()
