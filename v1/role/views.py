#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/8/18 17:15
# @Author : Joker
# @Site : 
# @File : views.py
# @Software: PyCharm
from sanic import json
from sanic.blueprints import Blueprint

role_bp = Blueprint('role', url_prefix='/role')


@role_bp.route('/get_role')
def get_role_list(request):
    return json({'role': []})
