import time
from pathlib import Path
from typing import Any


def parse_input(input_path: Path) -> tuple[tuple[Any, ...], tuple[Any, ...]]:
    *raw_shapes, raw_spaces = input_path.read_text().split("\n\n")

    shapes = []
    for raw_shape in raw_shapes:
        _, *rows = raw_shape.splitlines()
        shape = tuple(tuple(map(int, row.replace(".", "0").replace("#", "1"))) for row in rows)
        shapes.append(shape)

    spaces = []
    for raw_space in raw_spaces.splitlines():
        raw_dimension, raw_amounts = raw_space.split(":")
        dimension = tuple(map(int, raw_dimension.split("x")))
        amounts = tuple(map(int, raw_amounts.strip().split()))
        spaces.append((dimension, amounts))

    return tuple(shapes), tuple(spaces)


def rotate(shape: tuple[tuple[int, ...], ...], rotations: int):
    for _ in range(rotations):
        shape = tuple(zip(*reversed(shape)))
    return shape

def shape_size(shape: tuple[tuple[int, ...], ...]) -> int:
    return sum(block for row in shape for block in row)

def solve_part_one(input_path: Path):
    pass


def solve_part_two(input_path: Path):
    pass


def main():
    t0 = time.perf_counter()
    result_1 = solve_part_one(Path("input/input_12.txt"))
    t1 = time.perf_counter()
    print(f"Part 1 {t1 - t0:>8.3f} s\t{result_1}")

    t2 = time.perf_counter()
    result_2 = solve_part_two(Path("input/input_12.txt"))
    t3 = time.perf_counter()
    print(f"Part 2 {t3 - t2:>8.3f} s\t{result_2}")
    print(f"Total  {t3 - t0:>8.3f} s")


if __name__ == "__main__":
    main()


