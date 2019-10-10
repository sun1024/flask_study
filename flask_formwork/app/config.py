#!/usr/bin/python
# -*- coding:utf-8 -*-
# author:b1ng0
import os

# 数据库信息
HOST = '127.0.0.1'
DATABASE = 'test'
USER = 'root'
PASSWORD = 'xxxx'
PORT = 3306
DRIVER = 'mysqlconnector'

# flask 选项 调试模式和开启多线程,以及安全码
THREADED = True
DEBUG = False
SECRET_KEY = os.urandom(16)

# SQLALchemy 的配置驱动与修改默认连接池与超时
SQLALCHEMY_DATABASE_URI = 'mysql+' + DRIVER + '://' \
    + USER + ':' \
    + PASSWORD + '@' + HOST + ':' \
    + str(PORT) + '/' + DATABASE + '?charset=utf8'

SQLALCHEMY_TRACK_MODIFIACTIONS = False
SQLALCHEMY_POOL_SIZE = 50
SQLALCHEMY_POOL_TIMEOUT = 30
SQLALCHEMY_POOL_RECYCLE = -1