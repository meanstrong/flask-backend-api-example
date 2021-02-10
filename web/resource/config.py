# -*- coding:utf-8 -*-
from web.service.config import ConfigService


class Config:
    def get(self, key):
        return ConfigService().get_value(key)
