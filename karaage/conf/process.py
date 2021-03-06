# -*- coding: utf-8 -*-
#
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

import importlib
import django
import pkg_resources
from karaage.plugins import BasePlugin


def registered_karaage_apps():
    apps = []
    for entry_point in pkg_resources.iter_entry_points('karaage.apps'):
        try:
            entry_point.load()
        except (ImportError, pkg_resources.DistributionNotFound):
            continue # dependencies for the entry point not satisfied
        apps.append(entry_point.name)
    return apps


def add_plugin(namespace, plugin_name, django_apps, depends):

    module_name, descriptor_name = plugin_name.rsplit(".", 1)
    module = importlib.import_module(module_name)
    descriptor = getattr(module, descriptor_name)
    assert issubclass(descriptor, BasePlugin)

    value = descriptor.depends
    depends.extend(value)

    if django.VERSION < (1, 7):
        value = descriptor.name
        assert value is not None
        django_apps.append(value)
    else:
        django_apps.append(plugin_name)

    value = descriptor.django_apps
    django_apps.extend(value)

    value = descriptor.xmlrpc_methods
    namespace.XMLRPC_METHODS += value

    value = descriptor.template_context_processors
    namespace.TEMPLATE_CONTEXT_PROCESSORS += value

    for key, value in descriptor.settings.items():
        try:
            getattr(namespace, key)
        except AttributeError:
            setattr(namespace, key, value)


def load_plugins(namespace, plugins):
    done = set()
    django_apps = []

    depends = plugins
    while len(depends) > 0:
        new_depends = []
        for plugin in depends:
            if plugin not in done:
                add_plugin(namespace, plugin, django_apps, new_depends)
                done.add(plugin)
        depends = new_depends

    installed_apps = []
    done = set()

    for apps in [
        registered_karaage_apps(),
        namespace.KARAAGE_APPS,
        django_apps,
        namespace.INSTALLED_APPS,
    ]:
        for app in apps:
            if app not in done:
                installed_apps.append(app)
                done.add(app)

    namespace.INSTALLED_APPS = installed_apps

    del namespace.KARAAGE_APPS


def post_process(namespace):
    http_host = namespace.HTTP_HOST
    for i, host in enumerate(namespace.ALLOWED_HOSTS):
        namespace.ALLOWED_HOSTS[i] = host % {'HOST': http_host}
    namespace.REGISTRATION_BASE_URL = \
        namespace.REGISTRATION_BASE_URL % {'HOST': http_host}
    namespace.ADMIN_BASE_URL = \
        namespace.ADMIN_BASE_URL % {'HOST': http_host}
    load_plugins(namespace, namespace.PLUGINS)
