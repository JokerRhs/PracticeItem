#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/8/18 11:54
# @Author : Joker
# @Site : 
# @File : models.py
# @Software: PyCharm
from tortoise.models import Model
from tortoise import fields


class User(Model):
    id = fields.IntField(pk=True)
    u_mail = fields.CharField(128, unique=True, index=True)
    u_pwd = fields.CharField(32, null=False)
    u_detail = fields.OneToOneField('user.UserDetail', on_delete=fields.CASCADE)
    u_role = fields.ManyToManyField('role.Role', 'userId')


class UserDetail(Model):
    id = fields.IntField(pk=True)
    u_name = fields.CharField(32, null=False,)
    u_sex = fields.SmallIntField()



