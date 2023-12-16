import unittest
from shape import *
from area_calculator import *


class TestVisitorPattern(unittest.TestCase):

    def test_circle_initialization(self):
        circle = Circle(5)
        self.assertEqual(circle.radius, 5)
