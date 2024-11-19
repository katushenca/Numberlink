from input_parser import InputParser
from triangle import TriangleObject
from output_parser import OutputParser

def get_input_data() -> InputParser:
    while True:
        try:
            parser = InputParser.get_input_data()
            return parser
        except Exception as e:
            print(f"Некорректные входные данные: {e.args[0]}")
            continue

def get_filled_triangle():
    parser = get_input_data()
    triangle = TriangleObject(parser.triangle_len, parser.nodes_count)
    o_parser = OutputParser()
    triangle.ascii_triangle = o_parser.fill_triangle(triangle)
    return triangle

#triangle = get_filled_triangle()
#print(*triangle.ascii_triangle)
#print(triangle.generate_all_points())
#print(triangle.digits_points)