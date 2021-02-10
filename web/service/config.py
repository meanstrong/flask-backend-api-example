from web.model.config import ConfigModel

from .base import Base


class ConfigService(Base):
    __model__ = ConfigModel

    def get_value(self, key, default=None):
        obj = self.filter_by(key=key).first()
        if obj is not None:
            return obj.value
        return default
