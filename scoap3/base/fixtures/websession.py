# -*- coding: utf-8 -*-
#
## This file is part of SCOAP3.
## Copyright (C) 2012, 2013 CERN.
##
## SCOAP3 is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## SCOAP3 is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with SCOAP3; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.


from fixture import DataSet
from invenio.config import CFG_SITE_ADMIN_EMAIL


class UserData(DataSet):
    class admin:
        id = 1
        email = CFG_SITE_ADMIN_EMAIL
        password = ''
        note = '1'
        nickname = 'admin'

__all__ = ('UserData',)
