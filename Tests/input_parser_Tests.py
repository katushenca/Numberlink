import unittest
from unittest.mock import patch
from ..input_parser import InputParser

class TestInputParser(unittest.TestCase):
    def test_get_input_data_valid_input(self):
        with patch('builtins.input', side_effect=['3', '4']):
            parser = InputParser.get_input_data()
            self.assertEqual(parser.triangle_len, 3)
            self.assertEqual(parser.nodes_count, 4)

    def test_get_input_data_invalid_triangle_len(self):
        with patch('builtins.input', side_effect=['6', '4']):  # 6 - некорректная длина
            with self.assertRaises(ValueError) as context:
                InputParser.get_input_data()
            self.assertIn("Введена некорректная длина треугольника", str(context.exception))

    def test_get_input_data_invalid_nodes_count(self):
        with patch('builtins.input', side_effect=['3', '10']):  # 10 - некорректное количество точек для длины 3
            with self.assertRaises(ValueError) as context:
                InputParser.get_input_data()
            self.assertIn("Введено некорректное количество точек", str(context.exception))

if __name__ == '__main__':
    unittest.main()
