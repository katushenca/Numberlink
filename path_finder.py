from collections import deque, defaultdict
import triangle
class PathFinder:
    def find_paths(self, start, end, a, b, triangle):
        triangle_points = triangle.generate_all_points()
        bad_moves = self.get_bad_moves(triangle)
        queue = deque([(start, [start])])
        all_paths = []

        while queue:
            current, path = queue.popleft()
            x, y = current

            if current == end:
                all_paths.append(path)
                continue

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= ny <= a and 0 <= nx <= b and (nx, ny) not in path and (nx, ny) in triangle_points:
                    if self.check_is_point_other_digit(start, end, triangle, (nx, ny)):
                        if len(path) > 0 and (path[-1], (nx, ny)) not in bad_moves:
                            queue.append(((nx, ny), path + [(nx, ny)]))
        return all_paths


    def check_is_point_other_digit(self, start_point, end_point, triangle, current_point):
        digits_points = triangle.digits_points
        other_digits = [point[0] for point in digits_points if point[0] != start_point and point[0] != end_point]
        if current_point in other_digits:
            return False
        return True

    def get_bad_moves(self, triangle):
        result = []  # [((), ()), ...]
        points = triangle.generate_all_points()
        y = triangle.triangle_len
        x = triangle.triangle_len * 2 - 1
        for y in range(0, y+1, 2):
            for x in range(0, x+1, 2):
                if (y, x) in points and (y + 1, x) in points:
                    result.append(((y, x), (y + 1, x)))
                    result.append(((y + 1, x), (y, x)))

        for y in range(1, y, 2):
            for x in range(1, x, 2):
                if (y, x) in points and (y + 1, x) in points:
                    result.append(((y, x), (y + 1, x)))
                    result.append(((y + 1, x), (y, x)))

        return result

    def find_solutions(self, points, a, b, triangle):
        points_by_digit = defaultdict(list)
        for coord, digit in points:
            points_by_digit[digit].append(coord)

        all_solutions = []
        def backtrack(index, current_solution, used_points):
            if index == len(points_by_digit):
                all_solutions.append(current_solution[:])
                return

            digit = list(points_by_digit.keys())[index]
            point_pairs = points_by_digit[digit]
            start, end = point_pairs
            possible_paths = self.find_paths(start, end, a, b,
                                             triangle)
            for path in possible_paths:
                if all(p not in used_points for p in
                       path):
                    current_solution.append(path)
                    used_points.update(path)
                    backtrack(index + 1, current_solution, used_points)
                    current_solution.pop()
                    used_points.difference_update(path)
        backtrack(0, [], set())
        return all_solutions