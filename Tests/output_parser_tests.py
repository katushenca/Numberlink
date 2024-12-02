import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from Numberlink.output_parser import OutputParser
from Numberlink.triangle import TriangleObject
class TestOutputParser(unittest.TestCase):
    def test_get_output_with_good_triangle_1(self):
        triangle = TriangleObject(3, 2)
        parser = OutputParser()
        filled_triangle = parser.fill_triangle(triangle)
        self.assertEqual(4, sum(char.isdigit() for line in filled_triangle for char in line))

    def test_get_output_with_good_triangle_2(self):
        triangle = TriangleObject(5, 9)
        parser = OutputParser()
        filled_triangle = parser.fill_triangle(triangle)
        self.assertEqual(18, sum(
            char.isdigit() for line in filled_triangle for char in line))