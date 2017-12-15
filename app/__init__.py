#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author:Xiuzhu
@file:__init__.py.py
@time:2017/12/14 17:51
"""


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#flask read configuration files
app.config.from_object('config')
# 初始化数据库
db = SQLAlchemy(app)
from app import views,models

import os
from flask_login import LoginManager
from flask_openid import OpenID
from config import basedir

lm = LoginManager()
lm.init_app(app)
oid = OpenID(app, os.path.join(basedir, 'tmp'))
lm.login_view = 'login'