from collections import deque
import triangle
class PathFinder:
    def find_paths(self, start, end, a, b, triangle):
        triangle_points = triangle.generate_all_points()
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
                # Проверяем, что новая точка лежит в пределах карты и не была посещена ранее в этом пути
                if 0 <= nx <= a and 0 <= ny <= b and (nx, ny) not in path and (nx, ny) in triangle_points:
                    queue.append(((nx, ny), path + [(nx,
                                                     ny)]))  # Добавляем в очередь новую точку и обновленный путь

        return all_paths

start_point = (0, 1)
end_point = (1, 2)

finder = PathFinder()
triangle = triangle.TriangleObject(4, 3)
a = triangle.triangle_len * 2 - 1
b = triangle.triangle_len
all_paths = finder.find_paths(start_point, end_point, a, b, triangle)
for idx, p in enumerate(all_paths):
    print(f"Path {idx + 1}: {p}")

