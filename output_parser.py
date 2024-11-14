import Triangle
import random

class OutputParser:
    @staticmethod
    def get_triangle_pattern(triangle_len : int) -> list[str]:
        with open(f'triangle_patterns/{triangle_len}.txt') as file:
            triangle_str = file.readlines()
        return triangle_str

    def fill_triangle(self, triangle : Triangle) -> list[str]:
        free_spaces : list[tuple] = triangle.get_free_positions()
        triangle_ascii = triangle.ascii_triangle
        for i in range(triangle.nodes_count):
            random_place = random.choice(free_spaces)
            triangle_ascii[random_place[0]] = triangle_ascii[random_place[0]][:random_place[1]] + str(i) + triangle_ascii[random_place[0]][len(str(i)) + random_place[1]: ]
            free_spaces.remove(random_place)
            random_place = random.choice(free_spaces)
            triangle_ascii[random_place[0]] = triangle_ascii[random_place[0]][:random_place[1]] + str(i) + triangle_ascii[random_place[0]][len(str(i)) + random_place[1]: ]
            free_spaces.remove(random_place)
        return triangle_ascii

