#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/8/18 12:04
# @Author : Joker
# @Site : 
# @File : Setting.py
# @Software: PyCharm
__all__ = ['BaseConfig']

APP_MODULES = [
    'v1.user',
    'v1.permission',
    'v1.role',
]

db_config = {
    'connections': {
        # Dict format for connection
        'default': {
            'engine': 'tortoise.backends.mysql',
            'credentials': {
                'host': 'localhost',
                'port': '3306',
                'user': 'sanic_joker',
                'password': 'f7TtXF2Dpr2WFfBG',
                'database': 'sanic_blog',
            }
        },
        # Using a DB_URL string
        # 'default': 'postgres://postgres:qwerty123@localhost:5432/test'
    },
    'apps': {
        'user': {
            'models': ['v1.user.models'],
            # If no default_connection specified, defaults to 'default'
            'default_connection': 'default',
        },
        'permission': {
            'models': ['v1.permission.models'],
            'default_connection': 'default',
        },
        'role': {
            'models': ['v1.role.models'],
            'default_connection': 'default',
        }
    },
    # 'routers': ['v1.user.models'],
    'use_tz': False,
    'timezone': 'UTC8'
}


class BaseConfig:
    DB_CONFIG = db_config
