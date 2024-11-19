import unittest
from ..output_parser import OutputParser
from ..triangle import TriangleObject

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