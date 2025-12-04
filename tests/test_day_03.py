import pytest

from aoc2025 import day_03
from tests import INPUT_DIR

TEST_INPUT_1 = INPUT_DIR / "test_input_03_1.txt"


def test_parse_input():
    parsed_input = day_03.parse_input(TEST_INPUT_1)
    assert isinstance(parsed_input, tuple)
    assert all(isinstance(row, str) for row in parsed_input)


@pytest.mark.parametrize(
    "given_bank, expected_joltage",
    (
        ("987654321111111", 98),
        ("811111111111119", 89),
        ("234234234234278", 78),
        ("818181911112111", 92),
    ),
)
def test_find_max_joltage(given_bank, expected_joltage):
    joltage = day_03.find_max_joltage(given_bank)
    assert joltage == expected_joltage


@pytest.mark.parametrize(
    "given_bank, expected_joltage",
    (
        ("987654321111111", 987654321111),
        ("811111111111119", 811111111119),
        ("234234234234278", 434234234278),
        ("818181911112111", 888911112111),
    ),
)
def test_find_extra_max_danger_danger_joltage(given_bank, expected_joltage):
    joltage = day_03.find_extra_max_danger_danger_joltage(given_bank, 12)
    assert joltage == expected_joltage


def test_solving_part_1_gives_expected_value():
    answer = day_03.solve_part_one(TEST_INPUT_1)
    expected_answer = 357
    assert answer == expected_answer


def test_solving_part_2_gives_expected_value():
    answer = day_03.solve_part_two(TEST_INPUT_1)
    expected_answer = 3121910778619
    assert answer == expected_answer
