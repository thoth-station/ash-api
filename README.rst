Thoth's Ash API
---------------

Topics in the Python ecosystem

Running locally
===============

.. code-block:: console

  pipenv install --dev
  pipenv run gunicorn thoth.ash.openapi_server:app
  # OpenAPI UI will be available at http://127.0.0.1:8000/api/v0/ui/

