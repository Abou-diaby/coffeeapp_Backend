from django.contrib import admin
# from django.contrib.auth.models import
from django.urls import path
from .models import *
from ninja import NinjaAPI

from api.schema import CustomUserSchema

api = NinjaAPI()


@api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}


@api.post("/sign_up", response=CustomUserSchema)
def sign_up(request, username: str, phone_number: int, password: str):
    user = CustomUser.objects.create(username=username, phone_number=str(phone_number))
    user.set_password(password)
    user.save()

    return user