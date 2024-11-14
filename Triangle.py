from output_parser import OutputParser
import re
class Triangle:
    def __init__(self, triangle_len : int, nodes_count : int):
        self.triangle_len = triangle_len
        self.nodes_count = nodes_count
        self.ascii_triangle = OutputParser.get_triangle_pattern(self.triangle_len)


    def get_free_positions(self) -> list[tuple]:
        free_positions = []
        triangle_wo_start_spaces = [line.lstrip() for line in self.ascii_triangle]

        for i in range(2, len(self.ascii_triangle), 3):
            first_white_space_count = len(self.ascii_triangle[i]) - len(self.ascii_triangle[i].lstrip())
            spaces = re.split(r"[/\\]", triangle_wo_start_spaces[i])[1:-1]
            for j in range(len(spaces)):
                if spaces[j].count(' ') == 2:
                    free_positions.append((i, first_white_space_count + 2 + 3*j))
        return free_positions







