from fastapi import APIRouter

user = APIRouter()


@user.get('/')
def fetch_user():
    return "Hello World"
