#!/usr/local/bin/python
# -*- coding:utf-8 -*-
from web import db


class ConfigModel(db.Model):
    __tablename__ = "ds_config"

    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(64))
    value = db.Column(db.Text)
    description = db.Column(db.String(128))
