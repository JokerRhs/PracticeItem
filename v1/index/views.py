#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/8/18 17:02
# @Author : Joker
# @Site : 
# @File : views.py
# @Software: PyCharm
from sanic.response import json
from sanic.blueprints import Blueprint

index_bp = Blueprint('index', url_prefix='/')


@index_bp.route("/index")
async def hello_world(request):
    return json({"hello": "world"})
