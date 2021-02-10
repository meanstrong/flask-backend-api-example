# -*- coding:utf-8 -*-
import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object("web.config")
app.config["SQLALCHEMY_DATABASE_URI"] = ("mysql+pymysql://{0}:{1}@{2}:{3}/{4}?autocommit=true").format(
    app.config["DB_USER"], app.config["DB_PASS"], app.config["DB_HOST"], app.config["DB_PORT"], app.config["DB_NAME"]
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["JSON_AS_ASCII"] = False
app.config["PERMANENT_SESSION_LIFETIME"] = datetime.timedelta(hours=12)


db = SQLAlchemy(app)


from .controller import api_base