import time
from pathlib import Path


def parse_input(input_path: Path):
    return tuple(input_path.read_text().splitlines())


def find_max_joltage(battery_bank: str):
    batteries = tuple(map(int, battery_bank))
    max_joltage = 0
    for n, first_battery in enumerate(batteries[:-1]):
        for second_battery in batteries[n + 1 :]:
            max_joltage = max(max_joltage, first_battery * 10 + second_battery)
    return max_joltage


def find_extra_max_danger_danger_joltage(battery_bank: str, number_of_batteries: int):
    if number_of_batteries == 0:
        return 0

    end = -(number_of_batteries - 1) if number_of_batteries > 1 else None
    selected_battery = max(battery_bank[:end])
    selected_index = battery_bank.index(selected_battery)

    batteries_left = number_of_batteries - 1
    joltage = int(selected_battery) * 10**batteries_left

    return joltage + find_extra_max_danger_danger_joltage(
        battery_bank[selected_index + 1 :], batteries_left
    )


def solve_part_one(input_path: Path):
    battery_banks = parse_input(input_path)
    return sum(find_max_joltage(battery_bank) for battery_bank in battery_banks)


def solve_part_two(input_path: Path):
    battery_banks = parse_input(input_path)
    return sum(
        find_extra_max_danger_danger_joltage(battery_bank, 12)
        for battery_bank in battery_banks
    )


def main():
    t0 = time.perf_counter()
    result_1 = solve_part_one(Path("input/input_03.txt"))
    t1 = time.perf_counter()
    print(f"Part 1 {t1 - t0:>8.3f} s\t{result_1}")

    t2 = time.perf_counter()
    result_2 = solve_part_two(Path("input/input_03.txt"))
    t3 = time.perf_counter()
    print(f"Part 2 {t3 - t2:>8.3f} s\t{result_2}")
    print(f"Total  {t3 - t0:>8.3f} s")


if __name__ == "__main__":
    main()
