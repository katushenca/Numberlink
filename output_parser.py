import random

class OutputParser:
    def fill_triangle(self, triangleObject) -> list[str]:
        free_spaces : list[tuple] = triangleObject.get_free_positions()
        free_points = triangleObject.generate_all_points()
        triangle_ascii = triangleObject.ascii_triangle
        for i in range(triangleObject.nodes_count):
            random_place_index = random.randint(0, len(free_spaces) - 1)
            random_place = free_spaces[random_place_index]
            triangle_ascii[random_place[0]] = triangle_ascii[random_place[0]][:random_place[1]] + str(i) + triangle_ascii[random_place[0]][len(str(i)) + random_place[1]: ]
            triangleObject.digits_points.append((free_points[random_place_index], i))
            free_spaces.remove(random_place)
            free_points.remove(free_points[random_place_index])
            random_place_index = random.randint(0, len(free_spaces) - 1)
            random_place = free_spaces[random_place_index]
            triangle_ascii[random_place[0]] = triangle_ascii[random_place[0]][:random_place[1]] + str(i) + triangle_ascii[random_place[0]][len(str(i)) + random_place[1]: ]
            triangleObject.digits_points.append(
                (free_points[random_place_index], i))
            free_spaces.remove(random_place)
            free_points.remove(
                free_points[random_place_index])
        return triangle_ascii

