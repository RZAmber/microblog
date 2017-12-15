#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author:Xiuzhu
@file:forms.py
@time:2017/12/15 9:50
"""

# create login webform
# use   OpenID

from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    # DataRequired是wtf的验证器的一种
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default= False)