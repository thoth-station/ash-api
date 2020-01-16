#!/usr/bin/env python3
# Ash
# Copyright(C) 2020 Red Hat, Inc.
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import connexion
from connexion.resolver import RestyResolver

from thoth.ash.configuration import Configuration

app = connexion.FlaskApp(__name__, specification_dir=Configuration.SWAGGER_YAML_PATH, debug=True)

app.add_api(
    "ash-api.yaml",
    options={"swagger_ui": True},
    arguments={"title": "Ash API"},
    resolver=RestyResolver("thoth.ash.api"),
    strict_validation=True,
    validate_responses=True,
)


if __name__ == "__main__":
    app.run()
