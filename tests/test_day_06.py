import pytest

from aoc2025 import day_06
from tests import INPUT_DIR

TEST_INPUT_1 = INPUT_DIR / "test_input_06_1.txt"


def test_parse_input():
    parsed_input = day_06.parse_input(TEST_INPUT_1)

    assert parsed_input
    assert isinstance(parsed_input, tuple)
    assert all(isinstance(row, tuple) for row in parsed_input)

    numbers = parsed_input[:-1]
    assert all(isinstance(element, int) for row in numbers for element in row)

    operators = parsed_input[-1]
    assert all(isinstance(element, str) for row in operators for element in row)


def test_parse_input_vertically():
    parsed_input = day_06.parse_input_vertically(TEST_INPUT_1)

    assert parsed_input
    assert isinstance(parsed_input, tuple)

    assert all(
        isinstance(element, int) for column in parsed_input for element in column[:-1]
    )
    assert all(isinstance(column[-1], str) for column in parsed_input)


@pytest.mark.parametrize(
    "given_rows, expected_columns",
    (
        (((1, 2), (3, 4)), ((1, 3), (2, 4))),
        (
            ((1, 2, 3), (3, 4, 5), ("+", "*", "*")),
            ((1, 3, "+"), (2, 4, "*"), (3, 5, "*")),
        ),
    ),
)
def test_rows_to_columns(given_rows, expected_columns):
    columns = day_06.rows_to_columns(given_rows)
    assert columns == expected_columns


@pytest.mark.parametrize(
    "given_column, expected_answer",
    (
        ((123, 45, 6, "*"), 33210),
        ((328, 64, 98, "+"), 490),
        ((51, 387, 215, "*"), 4243455),
        ((64, 23, 314, "+"), 401),
    ),
)
def test_calculate_column(given_column, expected_answer):
    answer = day_06.calculate_column(given_column)
    assert answer == expected_answer


def test_solving_part_1_gives_expected_value():
    answer = day_06.solve_part_one(TEST_INPUT_1)
    expected_answer = 4277556
    assert answer == expected_answer


def test_solving_part_2_gives_expected_value():
    answer = day_06.solve_part_two(TEST_INPUT_1)
    expected_answer = 3263827
    assert answer == expected_answer
