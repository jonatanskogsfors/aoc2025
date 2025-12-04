import time
from pathlib import Path


def parse_input(input_path: Path):
    paper_map = set()
    for y, row in enumerate(input_path.read_text().splitlines()):
        for x, point in enumerate(row):
            if point == "@":
                paper_map.add((x, y))
    return paper_map


def is_accessible(
    paper_map: set[tuple[int, int]], position: tuple[int, int], corner: tuple[int, int]
) -> bool:
    x, y = position
    if position not in paper_map:
        return False
    adjacent_positions = {
        (x - 1, y - 1),
        (x, y - 1),
        (x + 1, y - 1),
        (x - 1, y),
        (x + 1, y),
        (x - 1, y + 1),
        (x, y + 1),
        (x + 1, y + 1),
    }
    max_x, max_y = corner
    adjacent_positions = {
        (x, y) for x, y in adjacent_positions if 0 <= x <= max_x and 0 <= y <= max_y
    }
    return len(adjacent_positions & paper_map) < 4


def solve_part_one(input_path: Path):
    paper_map = parse_input(input_path)
    max_x = max(x for x, _ in paper_map)
    max_y = max(y for _, y in paper_map)
    return len(
        [
            paper_roll
            for paper_roll in paper_map
            if is_accessible(paper_map, paper_roll, (max_x, max_y))
        ]
    )


def solve_part_two(input_path: Path):
    paper_map = parse_input(input_path)
    max_x = max(x for x, _ in paper_map)
    max_y = max(y for _, y in paper_map)
    total_removed = 0
    while True:
        removable = {
            paper_roll
            for paper_roll in paper_map
            if is_accessible(paper_map, paper_roll, (max_x, max_y))
        }
        if not removable:
            break
        total_removed += len(removable)
        paper_map -= removable
    return total_removed


def main():
    t0 = time.perf_counter()
    result_1 = solve_part_one(Path("input/input_04.txt"))
    t1 = time.perf_counter()
    print(f"Part 1 {t1 - t0:>8.3f} s\t{result_1}")

    t2 = time.perf_counter()
    result_2 = solve_part_two(Path("input/input_04.txt"))
    t3 = time.perf_counter()
    print(f"Part 2 {t3 - t2:>8.3f} s\t{result_2}")
    print(f"Total  {t3 - t0:>8.3f} s")


if __name__ == "__main__":
    main()
