from app.schemas.user import User
from fastapi import APIRouter
from app.models.user import Users
from app.config.database import engine

user = APIRouter()
user_schema = Users()


def show_data(query):
    res = []
    for info in query:
        res_dict = {
            "id": info.tuple()[0],
            "name": info.tuple()[1],
            "email": info.tuple()[2],
            "password": info.tuple()[3],

        }
        res.append(res_dict)
    return {"user": res}


@user.get('/')
def fetch_user():
    conn = engine.connect()
    query = conn.execute(user_schema.get_instance().select()).fetchall()
    return show_data(query)


@user.get('/{id}')
def fetch_single_user(id: int):
    conn = engine.connect()
    query = conn.execute(user_schema.get_instance().select().where(user_schema.get_instance().c.id == id)).first()
    return show_data(query)


@user.post('/')
def create_user(usr: User):
    conn = engine.connect()
    conn.execute(user_schema.get_instance().insert().values(
        name=usr.name,
        email=usr.email,
        password=usr.password
    ))
    query = conn.execute(user_schema.get_instance().select()).fetchall()
    return show_data(query)


@user.put('/{id}')
def update_user(id: int, user: User):
    conn = engine.connect()
    conn.execute(user_schema.get_instance().update().values(
        name=user.name,
        email=user.email,
        password=user.password
    ).where(user_schema.get_instance().c.id == id))
    query = conn.execute(user_schema.get_instance().select()).fetchall()
    return show_data(query)


@user.delete('/{id}')
def delete_user(id: int):
    conn = engine.connect()
    conn.execute(user_schema.get_instance().delete().where(user_schema.get_instance().c.id == id))
    query = conn.execute(user_schema.get_instance().select()).fetchall()
    return show_data(query)
