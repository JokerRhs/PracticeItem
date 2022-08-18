#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/8/18 17:12
# @Author : Joker
# @Site : 
# @File : views.py
# @Software: PyCharm
from sanic import json
from sanic.blueprints import Blueprint

permission_bp = Blueprint('permission', url_prefix='/permission')


@permission_bp.route('/get_permission')
def get_permission_list(request):
    return json({'permission': []})

