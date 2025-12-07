import time
from collections import defaultdict
from pathlib import Path


def parse_input(input_path: Path):
    raw_diagram = input_path.read_text().splitlines()
    start_position = None
    splitters = set()
    for y, row in enumerate(raw_diagram):
        for x, point in enumerate(row):
            match point:
                case "S":
                    start_position = (x, y)
                case "^":
                    splitters.add((x, y))
    return splitters, start_position


def beam(splitters: set, position: tuple[int, int]):
    height = (max(y for _, y in splitters) if splitters else 0) + 1
    positions = {position}
    visited = set()
    splits = 0
    while positions:
        position = positions.pop()
        x, y = position
        while y < height:
            y += 1
            if (x, y) in visited:
                break
            visited.add((x, y))
            if (x, y) in splitters:
                splits += 1
                for new_position in ((x - 1, y), (x + 1, y)):
                    if new_position not in visited:
                        positions.add(new_position)
                break

    return splits


def quantum_beam(splitters: set, position: tuple[int, int]):
    height = (max(y for _, y in splitters) if splitters else 0) + 1
    active_timelines = defaultdict(int)
    active_timelines[position] += 1
    finished_timelines = 0
    while active_timelines:
        position = next(iter(active_timelines.keys()))
        multiplier = active_timelines.pop(position)
        x, y = position
        while y < height:
            y += 1
            if (x, y) in splitters:
                for new_position in ((x - 1, y), (x + 1, y)):
                    active_timelines[new_position] += multiplier
                break
        else:
            finished_timelines += multiplier
    return finished_timelines


def solve_part_one(input_path: Path):
    splitters, start_position = parse_input(input_path)
    return beam(splitters, start_position)


def solve_part_two(input_path: Path):
    splitters, start_position = parse_input(input_path)
    return quantum_beam(splitters, start_position)


def main():
    t0 = time.perf_counter()
    result_1 = solve_part_one(Path("input/input_07.txt"))
    t1 = time.perf_counter()
    print(f"Part 1 {t1 - t0:>8.3f} s\t{result_1}")

    t2 = time.perf_counter()
    result_2 = solve_part_two(Path("input/input_07.txt"))
    t3 = time.perf_counter()
    print(f"Part 2 {t3 - t2:>8.3f} s\t{result_2}")
    print(f"Total  {t3 - t0:>8.3f} s")


if __name__ == "__main__":
    main()
