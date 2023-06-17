from app.schemas.user import User
from fastapi import APIRouter
from app.models.user import users
from app.config.database import conn

user = APIRouter()


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
    query = conn.execute(users.select()).fetchall()
    show_data(query)


@user.get('/{id}')
def fetch_single_user(id: int):
    query = conn.execute(users.select().where(users.c.id == id)).first()
    show_data(query)


@user.post('/')
def create_user(usr: User):
    conn.execute(users.insert().values(
        name=usr.name,
        email=usr.email,
        password=usr.password
    ))
    query = conn.execute(users.select()).fetchall()
    show_data(query)


@user.put('/{id}')
def update_user(id: int, user: User):
    conn.execute(users.update().values(
        name=user.name,
        email=user.email,
        password=user.password
    ).where(users.c.id == id))
    query = conn.execute(users.select()).fetchall()
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


@user.delete('/{id}')
def delete_user(id: int):
    conn.execute(users.delete().where(users.c.id == id))
    query = conn.execute(users.select()).fetchall()
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
