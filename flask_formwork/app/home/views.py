#!/usr/bin/python
# -*- coding:utf-8 -*-
# author:b1ng0

# 导入蓝图
from . import home

# 导入其他配置文件
from flask import session, url_for, redirect, render_template

# 根据需求导入数据库模型 
# from home.models import url_index

# 登陆状态装饰器
from functools import wraps
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'login' in session:
            '''
            根据设置的session判断login
            '''
            if session['login'] == True:
                return func(*args, **kwargs)
            else:
                return redirect(url_for('home.error'))
        else:
            return redirect(url_for('home.error'))
    return wrapper

# 主要逻辑视图
@home.route('/')
def index():
    return 'hello home'

@home.route('/error')
def error():
    return '404 not found', 404