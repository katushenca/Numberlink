import re


class TriangleObject:
    @staticmethod
    def get_triangle_pattern(triangle_len: int) -> list[str]:
        with open(f'C:\\Users\\shute\\Desktop\\repo\\Numberlink\\Numberlink\\triangle_patterns\\{triangle_len}.txt') as file:
            triangle_str = file.readlines()
        return triangle_str

    def __init__(self, triangle_len: int, nodes_count: int):
        self.triangle_len = triangle_len
        self.nodes_count = nodes_count
        self.ascii_triangle = TriangleObject.get_triangle_pattern(self.triangle_len)
        #self.free_points_coords = []
        self.digits_points = []


    def get_free_positions(self) -> list[tuple]:
        free_positions = []
        digit_x = 0
        digit_y = 0
        triangle_wo_start_spaces = [line.lstrip() for line in
                                    self.ascii_triangle]

        for i in range(2, len(self.ascii_triangle), 3):
            first_white_space_count = len(self.ascii_triangle[i]) - len(
                self.ascii_triangle[i].lstrip())
            spaces = re.split(r"[/\\]", triangle_wo_start_spaces[i])[1:-1]
            for j in range(len(spaces)):
                if spaces[j].count(' ') == 2:
                    free_positions.append(
                        (i, first_white_space_count + 1 + 3 * j))
                    #self.free_points_coords.append((digit_x, digit_y))
                    digit_x += 1
            digit_y += 1
        return free_positions

    def generate_all_points(self):
        points = []
        x = self.triangle_len * 2 - 1
        y = self.triangle_len
        start = 0
        for j in range(y):
            for i in range(start, x):
                points.append((j, i))
            start += 1
            x -= 1

        return points