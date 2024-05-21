#!/usr/bin/python3
""" Test cases for amenity class """
from tests.test_models.test_base_model import test_basemodel
from models.city import Amenity


class test_Amenity(test_basemodel):
    """ Class """
    def __init__(self, *args, **kwargs):
        """ Instance of class test_city """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_amenity_name(self):
        """Instance to test for amenity name- string """
        new = self.value
        self.assertEqual(type(new.name), str)
