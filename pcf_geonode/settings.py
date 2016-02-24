# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2012 OpenPlans
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

# Django settings for the GeoNode project.
import os
import json
from urlparse import urlparse
import geonode
from geonode.settings import *

#
# General Django development settings
#

SITENAME = 'pcf_geonode'

# Defines the directory that contains the settings file as the LOCAL_ROOT
# It is used for relative settings elsewhere.
GEONODE_ROOT = os.path.abspath(os.path.abspath(geonode.__file__))
LOCAL_ROOT = os.path.abspath(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

WSGI_APPLICATION = "pcf_geonode.wsgi.application"


# Load more settings from a file called local_settings.py if it exists
try:
    from local_settings import *
except ImportError:
    pass

# Additional directories which hold static files
STATICFILES_DIRS.append(
    os.path.join(LOCAL_ROOT, "static"),
)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# Note that Django automatically includes the "templates" dir in all the
# INSTALLED_APPS, se there is no need to add maps/templates or admin/templates
TEMPLATE_DIRS = (
    os.path.join(LOCAL_ROOT, "templates"),
) + TEMPLATE_DIRS

# Location of url mappings
ROOT_URLCONF = 'pcf_geonode.urls'


# Location of locale files
LOCALE_PATHS = (
    os.path.join(LOCAL_ROOT, 'locale'),
    ) + LOCALE_PATHS

# Get ElasticSearch config from environment variables that point to a service url.
"""
if 'VCAP_SERVICES' in os.environ:
    searchly_service = json.loads(os.environ['VCAP_SERVICES'])['searchly'][0]['credentials']['uri']

    # Get your connection url from Searchly dashboard
    es = urlparse(searchly_service)
    port = es.port or 80

    HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
            'URL': es.scheme + '://' + es.hostname + ':' + str(port),
            'INDEX_NAME': 'geonode',
        },
    }

    if es.username:
        HAYSTACK_CONNECTIONS['default']['KWARGS'] = {"http_auth": es.username + ':' + es.password}

    INSTALLED_APPS = INSTALLED_APPS + ('haystack',)

# Run "python manage.py rebuild_index"
HAYSTACK_SEARCH = True
# Avoid permissions prefiltering
SKIP_PERMS_FILTER = True
# Update facet counts from Haystack
HAYSTACK_FACET_COUNTS = True

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 20
"""

import dj_database_url
DATABASES = {'default': dj_database_url.config()}
