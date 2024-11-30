from input_parser import InputParser
from triangle import TriangleObject
from output_parser import OutputParser
from path_finder import PathFinder


def get_input_data() -> InputParser:
    while True:
        try:
            parser = InputParser.get_input_data()
            return parser
        except Exception as e:
            print(f"Некорректные входные данные: {e.args[0]}")
            continue

def get_filled_triangle():
    isRandom = input('Хотите сгенерировать автоматически? (Y/N)')
    if isRandom == 'Y':
        parser = get_input_data()
        triangle = TriangleObject(parser.triangle_len, parser.nodes_count)
        o_parser = OutputParser()
        triangle.ascii_triangle = o_parser.fill_triangle(triangle)
        return triangle
    else:
        print('Нужно написать головоломку в папке Input')
        triangle_len = input('Введите имя файла (без расширения), которое вы изменили')
        nodes_count = input('Введите количество добавленных точек')
        try:
            with open(f'C:\\Users\\shute\\Desktop\\repo\\Numberlink\\Numberlink\\Input\\{triangle_len}.txt') as file:
                triangle_ascii = []
                for line in file:
                    if '.' in line:
                        break
                    triangle_ascii.append(line)
        except Exception as e:
            print(e.args[0])
        triangle = TriangleObject(int(triangle_len), int(nodes_count))
        triangle.ascii_triangle = triangle_ascii

        user_points = triangle.get_user_points()
        triangle.digits_points = user_points
        return triangle
    #TODO написать функцию, которая будет заполнять triangle.digits_points

triangle = get_filled_triangle()
print(*triangle.ascii_triangle)

finder = PathFinder()

a = triangle.triangle_len * 2 - 1
b = triangle.triangle_len
print(f'digits points {triangle.digits_points}')
all_paths = finder.find_paths(triangle.digits_points[0][0], triangle.digits_points[1][0], a, b, triangle)


parser = OutputParser()
solutions = finder.find_solutions(triangle.digits_points, a, b, triangle)
print('solutions')
lines = 'abcdefghijklmnopqrstuvwxyz'
count = 0

for solution in solutions:
    print(f'Решение # {count}')
    digit_name = 0
    for path in solution:
        path_input = ' -> '.join(f'({x},{y})' for x, y in path)
        print(f'{digit_name}: {path_input}')
        digit_name += 1
    letter = 0
    ascii_triangle = triangle.ascii_triangle.copy()
    for path in solution:
        ascii = parser.fill_path(path, lines[letter], ascii_triangle)
        ascii_triangle = ascii
        letter += 1
    print(*ascii_triangle)
    count += 1
