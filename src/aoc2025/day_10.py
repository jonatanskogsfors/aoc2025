import re
import time
from itertools import combinations_with_replacement
from pathlib import Path

BUTTONS_PATTERN = re.compile(r"\d+")
LIGHTS_PATTERN = re.compile(r"\[([.#]*)\]")


def parse_input(input_path: Path):
    rows = input_path.read_text().splitlines()
    instructions = []
    for row in rows:
        target, *buttons, _ = row.split()
        buttons = [tuple(map(int, BUTTONS_PATTERN.findall(button))) for button in buttons]
        instructions.append((target, tuple(buttons), None))
    return tuple(instructions)


def lights_value(lights: str):
    match = LIGHTS_PATTERN.match(lights)
    diodes = match.group(1)
    return int(diodes.replace(".", "0").replace("#", "1"), base=2)


def mask_from_button(*buttons: tuple[int, ...], bit_depth: int):
    mask = int("0" * bit_depth, base=2)
    for button in buttons:
        button_mask = ["0"] * bit_depth
        for n in button:
            button_mask[n] = "1"
        button_mask = int("".join(button_mask), base=2)
        mask ^= button_mask
    return mask


def lights_from_value(value: int, bit_depth: int) -> str:
    bit_pattern = f"{value:0{bit_depth}b}"
    return f"[{bit_pattern.replace('0', '.').replace('1', '#')}]"


def press_button(given_lights, given_button):
    lights = lights_value(given_lights)
    bit_depth = len(given_lights) - 2
    toggle_mask = mask_from_button(given_button, bit_depth=bit_depth)
    new_lights = lights ^ toggle_mask
    return lights_from_value(new_lights, bit_depth)


def shortest_sequence(target, buttons) -> int:
    bit_depth = len(target) - 2
    target = lights_value(target)
    for n in range(1, 10):
        for buttons_sequence in combinations_with_replacement(buttons, n):
            mask = mask_from_button(*buttons_sequence, bit_depth=bit_depth)
            if mask == target:
                return n

    return None


def solve_part_one(input_path: Path):
    rows = parse_input(input_path)
    return sum(shortest_sequence(target, buttons) for target, buttons, _ in rows)


def solve_part_two(input_path: Path):
    pass


def main():
    t0 = time.perf_counter()
    result_1 = solve_part_one(Path("input/input_10.txt"))
    t1 = time.perf_counter()
    print(f"Part 1 {t1 - t0:>8.3f} s\t{result_1}")

    t2 = time.perf_counter()
    result_2 = solve_part_two(Path("input/input_10.txt"))
    t3 = time.perf_counter()
    print(f"Part 2 {t3 - t2:>8.3f} s\t{result_2}")
    print(f"Total  {t3 - t0:>8.3f} s")


if __name__ == "__main__":
    main()
