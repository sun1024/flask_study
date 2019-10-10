#!/usr/bin/python
# -*- coding:utf-8 -*-
# author:b1ng0

# 注册蓝图
from flask import Blueprint
home = Blueprint('home', __name__)

# 导入视图函数
from . import views