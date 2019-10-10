#!/usr/bin/python
# -*- coding:utf-8 -*-
# author:b1ng0

import os
from flask import Flask
import config

# 注册蓝图
def start_Blueprint(app):
    from home import home
    app.register_blueprint(home)
    # from admin import admin
    # app.register_blueprint(admin, prefix_url='/admin')

# 注册数据库
def start_Db(app):
    from home.models import db
    db.init_app(app)
    with app.app_context():
        db.create_all()

def create_app():
    app = Flask(__name__, template_folder=('templates'), static_folder=('static'))
    app.config.from_object(config)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    start_Blueprint(app)
    start_Db(app)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(
        host='0.0.0.0', 
        port=5000
    )