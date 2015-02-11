# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2012, 2013, 2014 CERN.
##
## Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

"""about Blueprint implementation."""

import json
from functools import wraps
import warnings

from flask import current_app, Blueprint, \
    render_template, \
    request, \
    jsonify, \
    redirect, \
    url_for, \
    flash, \
    send_file, \
    abort, \
    make_response
from werkzeug.datastructures import MultiDict
from werkzeug.utils import secure_filename
from flask.ext.breadcrumbs import default_breadcrumb_root, register_breadcrumb
from flask.ext.menu import register_menu

from invenio.base.i18n import _
# from ..signals import template_context_created

blueprint = Blueprint(
    'about',
    __name__,
    url_prefix='/about',
    template_folder='../templates',
    static_folder='../static'
)

default_breadcrumb_root(blueprint, '.about')


@blueprint.route('/')
@register_menu(blueprint, 'main.about', _('About'), order=2)
@register_breadcrumb(blueprint, '.', _('About'))
def index():
    """Render the about page."""
    # draft_cache = aboutionDraftCacheManager.from_request()
    # draft_cache.save()

    # Send signal to allow modifications to the template context
    # template_context_created.send(
    #     '%s.%s' % (blueprint.name, index.__name__)  # ,
    #     #context=ctx
    # )

    return render_template('about/index.html')
