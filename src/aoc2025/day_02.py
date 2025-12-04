import time
from pathlib import Path


def parse_input(input_path: Path):
    return tuple(
        tuple(map(int, id_range.split("-")))
        for id_range in input_path.read_text().split(",")
    )


def doubles_in_range(given_range: tuple[int, int]) -> set[int]:
    repeats = set()
    start, end = given_range
    for number in range(start, end + 1):
        string_number = str(number)
        string_length = len(string_number)
        if (
            string_length % 2 == 0
            and string_number[: string_length // 2] == string_number[string_length // 2 :]
        ):
            repeats.add(number)
    return repeats


def repeats_in_range(given_range: tuple[int, int]) -> set[int]:
    repeats = set()
    start, end = given_range
    for number in range(start, end + 1):
        string_number = str(number)
        string_length = len(string_number)
        for divisor_candidate in range(1, string_length // 2 + 1):
            if string_length % divisor_candidate == 0:
                if (
                    string_number[:divisor_candidate]
                    * (string_length // divisor_candidate)
                    == string_number
                ):
                    repeats.add(number)
    return repeats


def solve_part_one(input_path: Path):
    id_ranges = parse_input(input_path)
    repeat_sum = 0
    for id_range in id_ranges:
        reapeats = doubles_in_range(id_range)
        repeat_sum += sum(reapeats)
    return repeat_sum


def solve_part_two(input_path: Path):
    id_ranges = parse_input(input_path)
    repeat_sum = 0
    for id_range in id_ranges:
        reapeats = repeats_in_range(id_range)
        repeat_sum += sum(reapeats)
    return repeat_sum


def main():
    t0 = time.perf_counter()
    result_1 = solve_part_one(Path("input/input_02.txt"))
    t1 = time.perf_counter()
    print(f"Part 1 {t1 - t0:>8.3f} s\t{result_1}")

    t2 = time.perf_counter()
    result_2 = solve_part_two(Path("input/input_02.txt"))
    t3 = time.perf_counter()
    print(f"Part 2 {t3 - t2:>8.3f} s\t{result_2}")
    print(f"Total  {t3 - t0:>8.3f} s")


if __name__ == "__main__":
    main()
