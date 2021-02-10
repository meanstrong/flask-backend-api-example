# -*- coding:utf-8 -*-

from web import app

app.secret_key = "XXXXXXXX"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=app.config["PORT"], debug=app.config["DEBUG"])
