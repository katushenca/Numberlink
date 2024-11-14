import input_parser

while True:
    try:
        parser = input_parser.InputParser.get_input_data()
    except Exception as e:
        print(f"Некорректные входные данные: {e.args[0]}")
        continue
    break
