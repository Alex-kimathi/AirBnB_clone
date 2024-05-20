#!/usr/bin/python3
"""Defines class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Reviews users give about a place"""
    place_id = ""
    user_id = ""
    text = ""
