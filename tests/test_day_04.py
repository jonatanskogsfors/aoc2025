import pytest

from aoc2025 import day_04
from tests import INPUT_DIR

TEST_INPUT_1 = INPUT_DIR / "test_input_04_1.txt"


def test_parse_input():
    paper_map = day_04.parse_input(TEST_INPUT_1)
    assert isinstance(paper_map, set)
    assert all(isinstance(point, tuple) for point in paper_map)
    assert all(isinstance(component, int) for point in paper_map for component in point)


@pytest.mark.parametrize(
    "given_map, given_position, expected_accessibility",
    (
        ({(0, 0)}, (0, 0), True),
        ({(0, 0)}, (1, 0), False),
        ({(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1)}, (0, 0), True),
        ({(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1)}, (1, 0), False),
    ),
)
def test_is_accessible(given_map, given_position, expected_accessibility):
    max_x = max(x for x, _ in given_map)
    max_y = max(y for _, y in given_map)
    accessibility = day_04.is_accessible(given_map, given_position, (max_x, max_y))
    assert accessibility == expected_accessibility


def test_solving_part_1_gives_expected_value():
    answer = day_04.solve_part_one(TEST_INPUT_1)
    expected_answer = 13
    assert answer == expected_answer


def test_solving_part_2_gives_expected_value():
    answer = day_04.solve_part_two(TEST_INPUT_1)
    expected_answer = 43
    assert answer == expected_answer
