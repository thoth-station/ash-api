import connexion
from thoth.ash import __version__


def info_response() -> dict:
    """This method will do the real work."""
    return {
        "version": __version__,
        "connexionVersion": connexion.__version__,
    }


def search():
    return info_response(), 200, {"x-thoth-ash-api-version": __version__}
