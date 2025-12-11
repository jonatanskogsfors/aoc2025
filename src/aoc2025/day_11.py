import time
from functools import lru_cache
from pathlib import Path


def parse_input(input_path: Path):
    server_rack = {}
    for row in input_path.read_text().splitlines():
        key, value = row.split(": ")
        server_rack[key] = value.split()
    return server_rack


@lru_cache(maxsize=None)
def dfs(current: str, target: str, server_rack: tuple):
    # Target found
    if current == target:
        return 1

    # Because LRU cache won't accept dictionaries, a tuple is used instead
    target_machines = []
    for machine, *targets in server_rack:
        if machine == current:
            target_machines = targets

    # Recursive lookup for each reachable machine
    count = 0
    for next_machine in target_machines:
        count += dfs(next_machine, target, server_rack)
    return count


def solve_part_one(input_path: Path):
    server_rack = parse_input(input_path)
    server_rack = tuple((key, *values) for key, values in server_rack.items())
    count = dfs("you", "out", server_rack)
    return count


def solve_part_two(input_path: Path):
    server_rack = parse_input(input_path)
    server_rack = tuple((key, *values) for key, values in server_rack.items())
    a = dfs("svr", "fft", server_rack)
    b = dfs("fft", "dac", server_rack)
    c = dfs("dac", "out", server_rack)
    return a * b * c


def main():
    t0 = time.perf_counter()
    result_1 = solve_part_one(Path("input/input_11.txt"))  # 164 too low
    t1 = time.perf_counter()
    print(f"Part 1 {t1 - t0:>8.3f} s\t{result_1}")

    t2 = time.perf_counter()
    result_2 = solve_part_two(Path("input/input_11.txt"))
    t3 = time.perf_counter()
    print(f"Part 2 {t3 - t2:>8.3f} s\t{result_2}")
    print(f"Total  {t3 - t0:>8.3f} s")


if __name__ == "__main__":
    main()
