MIN_TRIANGLE_LEN = 2
MAX_TRIANGLE_LEN = 5
MIN_NODES_COUNT = 1

class InputParser:
    def __init__(self, triangle_len: int, nodes_count: int):
        self.triangle_len: int = triangle_len
        self.nodes_count: int = nodes_count

    @staticmethod
    def get_input_data():
        try:
            triangle_len = int(input(f"Введите длину стороны треугольника (от {MIN_TRIANGLE_LEN} до {MAX_TRIANGLE_LEN}): "))
            if triangle_len > MAX_TRIANGLE_LEN or triangle_len < MIN_TRIANGLE_LEN:
                raise ValueError("Введена некорректная длина треугольника")
        except ValueError as e:
            raise ValueError(f"Некорректные данные: {e}")

        try:
            nodes_count = int(input(f"Введите количество точек (от {MIN_NODES_COUNT} до {InputParser.get_max_nodes_count(triangle_len)}): "))
            if nodes_count > InputParser.get_max_nodes_count(triangle_len) or nodes_count < MIN_NODES_COUNT:
                raise ValueError("Введено некорректное количество точек")
        except ValueError as e:
            raise ValueError(f"Некорректные данные: {e}")

        return InputParser(triangle_len, nodes_count)

    @staticmethod
    def get_max_nodes_count(triangle_len: int) -> int:
        return (triangle_len ** 2) // 2


