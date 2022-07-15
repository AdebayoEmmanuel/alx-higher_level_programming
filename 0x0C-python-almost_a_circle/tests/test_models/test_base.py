#!/usr/bin/python3

import unittest

from models.base import Base

class TestBase(unittest.TestCase):

    def test_instantiation(self):
        """id = 1 expected"""
        instance_1 = Base()
        """id = 2 expected"""
        instance_2 = Base()
        """id = 3 expected"""
        instance_3 = Base()
        """id = 4 expected"""
        instance_4 = Base(None)
        """id = 500 expected"""
        instance_5 = Base(500)
        """id = 5 expected"""
        instance_6 = Base()

        self.assertEqual(instance_1.id, 1)
        self.assertEqual(instance_2.id, 2)
        self.assertEqual(instance_3.id, 3)
        self.assertEqual(instance_4.id, 4)
        self.assertEqual(instance_5.id, 500)
        self.assertEqual(instance_6.id, 5)
