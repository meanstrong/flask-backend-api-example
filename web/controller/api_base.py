#!/usr/bin/env python
# -*- coding:utf-8 -*-


from flask import current_app, request

from web import app
from web.resource.config import Config
from web.response import JsonResponse


@app.route("/api/v1/get_config", methods=["POST"])
def get_config():
    args = request.get_json(force=True)
    current_app.logger.info("get_config request data: {}".format(args))
    data = Config().get(args.get("key", ""))
    return JsonResponse(data=data).build()
