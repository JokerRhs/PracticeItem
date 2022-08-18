#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/8/18 15:10
# @Author : Joker
# @Site : 
# @File : models.py
# @Software: PyCharm
from tortoise.models import Model
from tortoise import fields


class Permission(Model):
    id = fields.UUIDField(pk=True)
    p_des = fields.TextField(null=True)
    p_details = fields.JSONField()
    p_url = fields.CharField(512, unique=True)
    module_permissions = fields.BooleanField()
    create_time = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.p_url

