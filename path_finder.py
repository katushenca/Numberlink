from collections import deque
import triangle
class PathFinder:
    def find_paths(self, start, end, a, b, triangle):
        triangle_points = triangle.generate_all_points()
        bad_moves = self.get_bad_moves(triangle)
        print(bad_moves, "bad moves")
        print('aaaaa', bad_moves)
        queue = deque([(start, [
            start])])  # Очередь: каждый элемент - (текущая точка, путь до неё)
        all_paths = []  # Список для хранения всех путей

        while queue:
            current, path = queue.popleft()  # Достаем текущую точку и путь
            x, y = current

            # Если достигли конечной точки, сохраняем путь
            if current == end:
                all_paths.append(path)
                continue

            # Генерация всех возможных направлений
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy

                #print('lalala',path, (nx, ny), self.check_is_point_other_digit(start, end, triangle, (nx, ny)), (path[-1], (nx, ny)) not in bad_moves)
                # Проверяем, что новая точка лежит в пределах карты и не была посещена ранее в этом пути
                if 0 <= ny <= a and 0 <= nx <= b and (nx, ny) not in path and (nx, ny) in triangle_points:
                    if self.check_is_point_other_digit(start, end, triangle, (nx, ny)):
                        #(path, (nx, ny), 'fsdlfksdlf')
                        if len(path) > 0 and (path[-1], (nx, ny)) not in bad_moves:
                            queue.append(((nx, ny), path + [(nx, ny)]))  # Добавляем в очередь новую точку и обновленный путь

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