#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/8/18 17:16
# @Author : Joker
# @Site : 
# @File : views.py
# @Software: PyCharm
from sanic import json
from sanic.blueprints import Blueprint

user_bp = Blueprint('user', url_prefix='/user')


@user_bp.route('/get_user')
def get_user_list(request):
    return json({'user': []})
