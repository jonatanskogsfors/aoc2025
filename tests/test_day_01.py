import pytest

from aoc2025 import day_01
from tests import INPUT_DIR

TEST_INPUT_1 = INPUT_DIR / "test_input_01_1.txt"


@pytest.mark.parametrize(
    "given_position, given_instruction, expected_position, expected_passages",
    (
        (50, "L68", 82, 1),
        (82, "L30", 52, 0),
        (52, "R48", 0, 1),
        (0, "L5", 95, 0),
        (95, "R60", 55, 1),
        (55, "L55", 0, 1),
        (0, "L1", 99, 0),
        (99, "L99", 0, 1),
        (0, "R14", 14, 0),
        (14, "L82", 32, 1),
        (50, "R1000", 50, 10),
    ),
)
def test_rotation_updates_position(
    given_position, given_instruction, expected_position, expected_passages
):
    position, passages = day_01.rotate(given_position, given_instruction)
    assert position == expected_position
    assert passages == expected_passages


def test_solving_part_1_gives_expected_value():
    answer = day_01.solve_part_one(TEST_INPUT_1)
    expected_answer = 3
    assert answer == expected_answer


def test_solving_part_2_gives_expected_value():
    answer = day_01.solve_part_two(TEST_INPUT_1)
    expected_answer = 6
    assert answer == expected_answer
