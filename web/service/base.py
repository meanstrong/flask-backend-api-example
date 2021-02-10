#!/usr/local/bin/python
# -*- coding:utf-8 -*-
from web import db


class Base(object):
    __model__ = None

    def __init__(self):
        self.query = db.session.query(self.__model__)

    def save(self, model):
        db.session.add(model)
        db.session.commit()
        return model

    def filter_by(self, **kargs):
        self.query = self.query.filter_by(**kargs)
        return self

    def get(self, id):
        return self.query.get(id)

    def all(self):
        return self.query.all()

    def first(self):
        return self.query.first()

    def count(self):
        return self.query.count()

    def create(self, **kargs):
        return self.save(self.__model__(**kargs))

    def update(self, **kargs):
        return self.query.update(kargs)

    def delete(self):
        return self.query.delete(synchronize_session=False)

    def multi_create(self, item_list):
        # 单条SQL语句每次插入page_size=1000条数据
        start = end = 0
        page_size = 1000
        total = len(item_list)
        while start < total:
            if start + page_size > total:
                end = total
            else:
                end = start + page_size
            self.session.execute(self.__model__.__table__.insert(item_list[start:end]))
            start = end
        db.session.commit()
