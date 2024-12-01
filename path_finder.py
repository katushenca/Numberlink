from collections import deque, defaultdict
import triangle


class PathFinder:
    def find_paths(self, start, end, a, b, triangle, max_length):
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

            if len(path) >= max_length:
                continue

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= ny <= a and 0 <= nx <= b and (nx, ny) not in path and (
                nx, ny) in triangle_points:
                    if self.check_is_point_other_digit(start, end, triangle,
                                                       (nx, ny)):
                        if len(path) > 0 and (
                        path[-1], (nx, ny)) not in bad_moves:
                            queue.append(((nx, ny), path + [(nx, ny)]))
        return all_paths

    def check_is_point_other_digit(self, start_point, end_point, triangle,
                                   current_point):
        digits_points = triangle.digits_points
        other_digits = [point for point, digit in digits_points if
                        point != start_point and point != end_point]
        if current_point in other_digits:
            return False
        return True

    def get_bad_moves(self, triangle):
        result = []  # [((), ()), ...]
        points = triangle.generate_all_points()
        y_limit = triangle.triangle_len
        x_limit = triangle.triangle_len * 2 - 1
        for y in range(0, y_limit + 1, 2):
            for x in range(0, x_limit + 1, 2):
                if (y, x) in points and (y + 1, x) in points:
                    result.append(((y, x), (y + 1, x)))
                    result.append(((y + 1, x), (y, x)))

        for y in range(1, y_limit, 2):
            for x in range(1, x_limit, 2):
                if (y, x) in points and (y + 1, x) in points:
                    result.append(((y, x), (y + 1, x)))
                    result.append(((y + 1, x), (y, x)))

        return result

    def find_solutions(self, points, a, b, triangle, max_length):
        points_by_digit = defaultdict(list)
        for coord, digit in points:
            points_by_digit[digit].append(coord)

        all_solutions = []

        def backtrack(index, current_solution, used_points):
            if index == len(points_by_digit):
                all_solutions.append(
                    [path.copy() for path in current_solution])
                return

            digit = list(points_by_digit.keys())[index]
            point_pairs = points_by_digit[digit]
            if len(point_pairs) != 2:
                return
            start, end = point_pairs
            possible_paths = self.find_paths(start, end, a, b, triangle,
                                             max_length)
            for path in possible_paths:
                if all(p not in used_points for p in path):
                    current_solution.append(path)
                    used_points.update(path)
                    backtrack(index + 1, current_solution, used_points)
                    current_solution.pop()
                    used_points.difference_update(path)

        backtrack(0, [], set())
        return all_solutions


