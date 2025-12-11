from aoc2025 import day_11
from tests import INPUT_DIR

TEST_INPUT_1 = INPUT_DIR / "test_input_11_1.txt"
TEST_INPUT_2 = INPUT_DIR / "test_input_11_2.txt"


def test_parse_input():
    parsed_input = day_11.parse_input(TEST_INPUT_1)
    assert isinstance(parsed_input, dict)
    assert "you" in parsed_input


def test_solving_part_1_gives_expected_value():
    answer = day_11.solve_part_one(TEST_INPUT_1)
    expected_answer = 5
    assert answer == expected_answer


def test_solving_part_2_gives_expected_value():
    answer = day_11.solve_part_two(TEST_INPUT_2)
    expected_answer = 2
    assert answer == expected_answer
