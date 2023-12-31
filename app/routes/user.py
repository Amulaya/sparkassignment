from app.schemas.user import User
from fastapi import APIRouter
from app.models.user import Users
from app.config.database import engine

user = APIRouter()
user_schema = Users()


def show_data(result):
    res = []
    for info in result:
        if info is not None:
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
    with engine.connect() as conn:
        result = conn.execute(user_schema.get_instance().select()).fetchall()
        return show_data(result)


@user.get('/{id}')
def fetch_single_user(id: int):
    with engine.connect() as conn:
        result = conn.execute(user_schema.get_instance().select().where(user_schema.get_instance().c.id == id)).first()
        return show_data([result])


@user.post('/')
def create_user(usr: User):
    with engine.connect() as conn:
        conn.execute(user_schema.get_instance().insert().values(
            name=usr.name,
            email=usr.email,
            password=usr.password
        ))
        result = conn.execute(user_schema.get_instance().select()).fetchall()
        conn.commit()
        return show_data(result)


@user.put('/{id}')
def update_user(id: int, user: User):
    with engine.connect() as conn:
        conn.execute(user_schema.get_instance().update().values(
            name=user.name,
            email=user.email,
            password=user.password
        ).where(user_schema.get_instance().c.id == id))
        conn.commit()
        result = conn.execute(user_schema.get_instance().select()).fetchall()
        return show_data(result)


@user.delete('/{id}')
def delete_user(id: int):
    with engine.connect() as conn:
        conn.execute(user_schema.get_instance().delete().where(user_schema.get_instance().c.id == id))
        conn.commit()
        result = conn.execute(user_schema.get_instance().select()).fetchall()
        return show_data(result)
