import math
import time
from pathlib import Path


def parse_input(input_path: Path):
    all_rows = input_path.read_text().splitlines()
    numbers = tuple(tuple(map(int, row.split())) for row in all_rows[:-1])
    operators = tuple(all_rows[-1].split())
    return (*numbers, operators)


def parse_input_vertically(input_path: Path):
    all_rows = input_path.read_text().splitlines()
    columns = []
    current_column = []
    current_operator = None
    for column in zip(*all_rows):
        if all(element.isspace() for element in column):
            columns.append((*current_column, current_operator))
            current_column = []
            current_operator = None
        else:
            current_column.append(int("".join(column[:-1])))
            if not current_operator:
                current_operator = column[-1]
    columns.append((*current_column, current_operator))

    return tuple(columns)


def rows_to_columns(rows):
    return tuple(zip(*rows))


def calculate_column(column):
    *numbers, operator = column
    match operator:
        case "+":
            operation = sum
        case "*":
            operation = math.prod

    return operation(numbers)


def solve_part_one(input_path: Path):
    rows = parse_input(input_path)
    columns = rows_to_columns(rows)
    return sum(calculate_column(column) for column in columns)


def solve_part_two(input_path: Path):
    columns = parse_input_vertically(input_path)
    return sum(calculate_column(column) for column in columns)


def main():
    t0 = time.perf_counter()
    result_1 = solve_part_one(Path("input/input_06.txt"))
    t1 = time.perf_counter()
    print(f"Part 1 {t1 - t0:>8.3f} s\t{result_1}")

    t2 = time.perf_counter()
    result_2 = solve_part_two(Path("input/input_06.txt"))
    t3 = time.perf_counter()
    print(f"Part 2 {t3 - t2:>8.3f} s\t{result_2}")
    print(f"Total  {t3 - t0:>8.3f} s")


if __name__ == "__main__":
    main()
