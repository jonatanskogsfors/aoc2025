import itertools
import time
from pathlib import Path


def parse_input(input_path: Path) -> tuple[tuple[int, int], ...]:
    return tuple(
        map(
            double_point,
            tuple(
                tuple(map(int, row.split(",")))
                for row in input_path.read_text().splitlines()
            ),
        )
    )


def double_point(point: tuple[int, int]):
    x, y = point
    return x * 2, y * 2


def half_point(point: tuple[int, int]):
    x, y = point
    return x // 2, y // 2


def calculate_area(corner_a: tuple[int, int], corner_b: tuple[int, int]) -> int:
    x1, y1 = half_point(corner_a)
    x2, y2 = half_point(corner_b)
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)


def is_inside(point, tiles):
    if point in tiles:
        return True
    x, y = point

    number_of_tiles = len(tiles)

    if len(
        [
            tile
            for (n, tile) in enumerate(tiles)
            if tile[1] == y
            and (next_tile := tiles[(n + 1) % number_of_tiles])
            and next_tile[1] == tile[1]
            and min((tile[0], next_tile[0])) < x < max(tile[0], next_tile[0])
        ]
    ):
        return True

    tiles_to_the_right = [(n, tile) for n, tile in enumerate(tiles) if tile[0] >= x]
    vertical_lines_to_the_right = [
        tile[0]
        for (n, tile) in tiles_to_the_right
        if (next_tile := tiles[(n + 1) % number_of_tiles])
        and next_tile[0] == tile[0]
        and min((tile[1], next_tile[1])) <= y <= max(tile[1], next_tile[1])
    ]

    return x in vertical_lines_to_the_right or len(vertical_lines_to_the_right) % 2 == 1


def rectangle_is_valid(corners, tiles):
    tile_a, tile_b = corners

    # Both corners must be red tiles
    if tile_a not in tiles or tile_b not in tiles:
        return False

    # The other corner must be inside the rectangle
    tile_c = tile_a[0], tile_b[1]
    tile_d = tile_b[0], tile_a[1]
    if not is_inside(tile_c, tiles) or not is_inside(tile_d, tiles):
        return False

    # If other tiles are inside the rectangle, the rectangle might be invalid
    x1, x2 = sorted((tile_a[0], tile_b[0]))
    y1, y2 = sorted((tile_a[1], tile_b[1]))
    tiles_inside = False
    for tile in tiles:
        if tile in (tile_a, tile_b):
            continue
        x, y = tile
        if x1 < x < x2 and y1 < y < y2:
            tiles_inside = True
            break
    if tiles_inside:
        return False

    # The middle point must be inside the rectangle
    middle_point = (x1 + x2) // 2, (y1 + y2) // 2
    if not is_inside(middle_point, tiles):
        return False

    return True


def solve_part_one(input_path: Path):
    tiles = parse_input(input_path)
    max_area = 0
    for tile_a, tile_b in itertools.combinations(tiles, 2):
        area = calculate_area(tile_a, tile_b)
        max_area = max(area, max_area)
    return max_area


def solve_part_two(input_path: Path):
    tiles = parse_input(input_path)
    max_area = 0
    for tile_a, tile_b in itertools.combinations(tiles, 2):
        if not rectangle_is_valid((tile_a, tile_b), tiles):
            continue
        area = calculate_area(tile_a, tile_b)
        max_area = max(area, max_area)
    return max_area


def main():
    t0 = time.perf_counter()
    result_1 = solve_part_one(Path("input/input_09.txt"))
    t1 = time.perf_counter()
    print(f"Part 1 {t1 - t0:>8.3f} s\t{result_1}")

    t2 = time.perf_counter()
    result_2 = solve_part_two(Path("input/input_09.txt"))  # 2847552260 too high
    t3 = time.perf_counter()
    print(f"Part 2 {t3 - t2:>8.3f} s\t{result_2}")
    print(f"Total  {t3 - t0:>8.3f} s")


if __name__ == "__main__":
    main()
