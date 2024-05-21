#!/usr/bin/python3
""" Test cases for city class """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_city(test_basemodel):
    """ Class """
    def __init__(self, *args, **kwargs):
        """ Instance of class test_city """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """Instance to test for city name- string """
        new = self.value
        self.assertEqual(type(new.name), str)
