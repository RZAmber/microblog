#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author:Xiuzhu
@file:config.py
@time:2017/12/15 9:44
"""

#许多flask需要大量的配置，因此在根目录下创建一个配置文件

#flask-wtf用于处理web表单
CSRF_ENDBLED = True
SECRET_KEY = 'you-will-never-guess' #加密令牌

# 为了用户更加方便使用openid，将其链接转换为短名称
# 将openid提供者定位为列表然后作为render_template参数传入到模板
OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]

#采用sqlite数据库
import os
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' +os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# SQLALCHEMY_DATABASE_URI是数据库路径，SQLALCHEMY_MIGRATE_REPO是数据文件存储文件夹

