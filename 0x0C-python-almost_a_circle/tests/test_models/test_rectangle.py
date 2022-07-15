#!/usr/bin/python3


from models.rectangle import Rectangle
from models.base import Base
import unittest


class TestRectangle(unittest.TestCase):
    """Tests rectangle class"""


    def test_normal_instantiation(self):
        """Tests for different types of normal instantiation of rectangle"""


        Base.reset()        

        rect_1 = Rectangle(1, 2)
        self.assertEqual(rect_1.id, 1)
        self.assertEqual(rect_1.width, 1)
        self.assertEqual(rect_1.height, 2)
        self.assertEqual(rect_1.x, 0)
        self.assertEqual(rect_1.y, 0)

        rect_2 = Rectangle(1, 2, 5)
        self.assertEqual(rect_2.id, 2)
        self.assertEqual(rect_2.width, 1)
        self.assertEqual(rect_2.height, 2)
        self.assertEqual(rect_2.x, 5)
        self.assertEqual(rect_2.y, 0)

        rect_3 = Rectangle(1, 2, 5, 6)
        self.assertEqual(rect_3.id, 3)
        self.assertEqual(rect_3.width, 1)
        self.assertEqual(rect_3.height, 2)
        self.assertEqual(rect_3.x, 5)
        self.assertEqual(rect_3.y, 6)

        rect_4 = Rectangle(1, 2, 5, 6, 9)
        self.assertEqual(rect_4.id, 9)
        self.assertEqual(rect_4.width, 1)
        self.assertEqual(rect_4.height, 2)
        self.assertEqual(rect_4.x, 5)
        self.assertEqual(rect_4.y, 6)

        rect_5 = Rectangle(1, 2, x=5, y=6, id=10)
        self.assertEqual(rect_5.id, 10)
        self.assertEqual(rect_5.width, 1)
        self.assertEqual(rect_5.height, 2)
        self.assertEqual(rect_5.x, 5)
        self.assertEqual(rect_5.y, 6)


    def test_missing_positional_args(self):
        """Tests with some missing positional arguments"""

            
        with self.assertRaises(TypeError) as cm:
            """Type error raises when there is issue with args
                'with' eliminates need for try catch
                context manager cm provides except to handle error
            """
            rect_1 = Rectangle()

        with self.assertRaises(TypeError) as cm:
            rect_2 = Rectangle(1)

    def test_attribute_validations(self):
        """Tests to validate rectangle's attributes"""

        with self.assertRaises(ValueError) as cm:
            rect_1 = Rectangle(0, 0)
        msg = "width must be > 0"
        self.assertEqual(str(cm.exception), msg)

        with self.assertRaises(ValueError) as cm:
            rect_2 = Rectangle(1, 0)
        msg = "height must be > 0"
        self.assertEqual(str(cm.exception), msg)
                        

        with self.assertRaises(ValueError) as cm:
            rect_3 = Rectangle(0, 1)
        msg = "width must be > 0"
        self.assertEqual(str(cm.exception), msg)


