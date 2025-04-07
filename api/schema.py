from ninja import ModelSchema
from .models import *

class CustomUserSchema(ModelSchema):
    class Config:
        model = CustomUser
        model_fields = ["username", "phone_number"]