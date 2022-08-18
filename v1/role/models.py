#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/8/18 15:59
# @Author : Joker
# @Site : 
# @File : models.py
# @Software: PyCharm
from tortoise import fields
from tortoise.models import Model


class Role(Model):
    id = fields.IntField(pk=True)
    r_name = fields.CharField(max_length=50)
    r_des = fields.TextField()
    role_permission = fields.ManyToManyField(
        model_name='permission.Permission',
        related_name='role',
        on_delete=fields.SET_NULL,
        null=True
    )
