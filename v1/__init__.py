#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/8/18 14:59
# @Author : Joker
# @Site : 
# @File : __init__.py
# @Software: PyCharm
from sanic.blueprints import Blueprint

from v1.user import user_bp
from v1.permission import permission_bp
from v1.role import role_bp
from v1.index import index_bp

api_v1 = Blueprint.group(
    user_bp,
    permission_bp,
    role_bp,
    index_bp,
    url_prefix='/api',
    version='1'
)
