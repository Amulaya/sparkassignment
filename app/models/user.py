from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from app.config.database import meta, engine


class Users:
    def __init__(self):
        self._ins = None

    def get_instance(self):
        if self._ins is None:
            self._ins = Table('users', meta,
                              Column('id', Integer, primary_key=True),
                              Column('name', String(255)),
                              Column('email', String(255)),
                              Column('password', String(255)),
                              )
            meta.create_all(engine)

        return self._ins
