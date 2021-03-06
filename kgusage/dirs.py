# Copyright 2007-2014 VPAC
#
# This file is part of Karaage.
#
# Karaage is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Karaage is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Karaage  If not, see <http://www.gnu.org/licenses/>.

from django.conf import settings
import os.path
try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse

GRAPH_TMP = os.path.join(
    settings.TMP_DIR, getattr(settings, 'GRAPH_TMP', 'kgusage')
)
GRAPH_DIR = getattr(settings, 'GRAPH_DIR', 'kgusage')
GRAPH_ROOT = os.path.join(settings.FILES_DIR, GRAPH_DIR)
GRAPH_URL = urlparse.urljoin(settings.FILES_URL, GRAPH_DIR)
