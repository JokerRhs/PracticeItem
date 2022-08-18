#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/8/18 12:11
# @Author : Joker
# @Site : 
# @File : main.py
# @Software: PyCharm
from sanic import Sanic
from sanic_ext import Extend
from tortoise.contrib.sanic import register_tortoise

from Setting import *
from v1 import api_v1


def create_app():
    sanic_app = Sanic(__name__)
    sanic_app.update_config(BaseConfig)
    register_tortoise(sanic_app, config=sanic_app.config['DB_CONFIG'], generate_schemas=False)
    sanic_app.blueprint(api_v1)

    return sanic_app


if __name__ == '__main__':
    app = create_app()
    Extend(app)
    app.run(host="localhost", port=8624, debug=True)
