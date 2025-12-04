import time
from pathlib import Path


def rotate(position: int, instruction: str) -> tuple[int, int]:
    direction, distance = instruction[0], int(instruction[1:])
    if direction == "L":
        new_position = (position - distance) % 100
        (
            full_turns,
            remainder,
        ) = divmod(distance, 100)
        return new_position, full_turns + (remainder >= (position or 100))
    elif direction == "R":
        new_position = (position + distance) % 100
        (
            full_turns,
            remainder,
        ) = divmod(distance, 100)
        return new_position, full_turns + ((remainder + position) > 99)


def find_zeros(position: int, instructions: list[str]) -> int:
    zero_count = 0
    for instruction in instructions:
        position, _ = rotate(position, instruction)
        zero_count += position == 0
    return zero_count


def find_passages(position: int, instructions: list[str]) -> int:
    zero_passages = 0
    for instruction in instructions:
        position, passages = rotate(position, instruction)
        zero_passages += passages
    return zero_passages


def solve_part_one(input_data: Path) -> int:
    # 2811: Too low
    return find_zeros(50, input_data.read_text().splitlines())


def solve_part_two(input_data: Path) -> int:
    return find_passages(50, input_data.read_text().splitlines())


def main():
    t0 = time.perf_counter()
    result_1 = solve_part_one(Path("input/input_01.txt"))
    t1 = time.perf_counter()
    print(f"Part 1 {t1 - t0:>8.3f} s\t{result_1}")

    t2 = time.perf_counter()
    result_2 = solve_part_two(Path("input/input_01.txt"))  # 2811: Too low
    t3 = time.perf_counter()
    print(f"Part 2 {t3 - t2:>8.3f} s\t{result_2}")
    print(f"Total  {t3 - t0:>8.3f} s")


if __name__ == "__main__":
    main()
