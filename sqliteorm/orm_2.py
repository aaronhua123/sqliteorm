# -*- coding: utf-8 -*-
# Created by go on 2019/5/8
# Copyright (c) 2019 go. All rights reserved.

from abc import ABC, abstractmethod
from .database import *


class Model(dict, ABC):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for k, v in kwargs.items():
            setattr(self, k, v)
        self.mappings = self.init()
        if not hasattr(self, "__table__"):
            self.__table__ = self.__class__.__name__

    def varchar(self, value):
        return f"varchar {value}"

    def TEXT(self):
        return 'TEXT'

    def PRIMARY(self):
        return 'INTEGER PRIMARY KEY AUTOINCREMENT'

    def delete(self, name, value):
        sql = 'delete from %s where %s=%s' % (self.__table__, name, value)
        return execute(sql, [])

    def creatdb(self):
        create = ""
        for k, v in self.mappings.items():
            create += f'{k} {v},'
        sql = '''CREATE TABLE {table} ({create})'''.format(table=self.__table__, create=create[:-1])
        execute(sql, [])
        print("creatdb")

    def save(self):
        value = []
        name = []
        typedb = []
        if self.get("id") is None:
            self["id"] = None
        for k, v in self.mappings.items():
            value.append(self[k])
            name.append(k)
            typedb.append(v)
        # print(value, name, typedb, self.__table__)
        sql = 'replace into %s (%s) values (%s)' % (self.__table__, ",".join(name), ",".join(["?"] * len(name)))
        return execute(sql, value)

    def findall(self):
        sql = 'select * from %s' % (self.__table__)
        print(sql)
        return select(sql, [], size=0)

    def select(self,sql):
        return select(sql, [], size=0)

    @abstractmethod
    def init(self):
        raise Exception("must defind init func")


class Shop(Model):
    # __table__ = "shop123"
    def init(self):
        return {
            "id": self.PRIMARY(),
            "qwe": self.TEXT(),
            "nameurl": self.TEXT()
        }
