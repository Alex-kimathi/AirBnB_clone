#!/usr/bin/python3
""" creates class User """
from models.base_model import BaseModel


class User(BaseModel):
    """Defines user attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
