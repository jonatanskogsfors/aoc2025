import time
from pathlib import Path


def parse_input(input_path: Path):
    raw_fresh_ranges, raw_ingredients = input_path.read_text().split("\n\n")
    fresh_ranges = tuple(
        list(map(int, fresh_range.split("-")))
        for fresh_range in raw_fresh_ranges.splitlines()
    )

    ingredients = tuple(map(int, raw_ingredients.splitlines()))
    return fresh_ranges, ingredients


def is_fresh(ingredient: int, fresh_ranges: list[list[int]]):
    for fresh_range in fresh_ranges:
        start, end = fresh_range
        if start <= ingredient <= end:
            return True
    return False


def all_fresh_ingredients(fresh_ranges):
    reduced_fresh_ingredients = reduce_ranges(fresh_ranges)
    fresh_ingredients = 0
    for fresh_range in reduced_fresh_ingredients:
        start, end = fresh_range
        fresh_ingredients += (end - start) + 1
    return fresh_ingredients


def merge_ranges(ranges):
    sorted_ranges = sorted(ranges)
    merged_ranges = []
    for start, end in sorted_ranges:
        if not merged_ranges:
            merged_ranges.append([start, end])
            continue

        _, last_end = merged_ranges[-1]
        if start <= last_end + 1:
            merged_ranges[-1][1] = max(end, last_end)
        else:
            merged_ranges.append([start, end])
    return merged_ranges


def reduce_ranges(ranges):
    new_ranges = merge_ranges(ranges)
    while new_ranges != ranges:
        ranges = new_ranges
        new_ranges = merge_ranges(ranges)
    return new_ranges


def solve_part_one(input_path: Path):
    fresh_ranges, ingredients = parse_input(input_path)
    reduced_fresh_ingredients = reduce_ranges(fresh_ranges)
    return len(
        [
            ingredient
            for ingredient in ingredients
            if is_fresh(ingredient, reduced_fresh_ingredients)
        ]
    )


def solve_part_two(input_path: Path):
    fresh_ranges, _ = parse_input(input_path)
    return all_fresh_ingredients(fresh_ranges)


def main():
    t0 = time.perf_counter()
    result_1 = solve_part_one(Path("input/input_05.txt"))
    t1 = time.perf_counter()
    print(f"Part 1 {t1 - t0:>8.3f} s\t{result_1}")

    t2 = time.perf_counter()
    result_2 = solve_part_two(Path("input/input_05.txt"))
    t3 = time.perf_counter()
    print(f"Part 2 {t3 - t2:>8.3f} s\t{result_2}")
    print(f"Total  {t3 - t0:>8.3f} s")


if __name__ == "__main__":
    main()
