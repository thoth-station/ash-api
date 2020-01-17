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

from typing import Dict
from typing import Any

import connexion
from thoth.ash import __version__


def info_response() -> Dict[str, Any]:
    """This method will do the real work."""
    return {
        "version": __version__,
        "connexionVersion": connexion.__version__,
    }


def search():
    return info_response(), 200, {"x-thoth-ash-api-version": __version__}
