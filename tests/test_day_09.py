import pytest

from aoc2025 import day_09
from tests import INPUT_DIR

TEST_INPUT_1 = INPUT_DIR / "test_input_09_1.txt"


def test_parse_input():
    parsed_input = day_09.parse_input(TEST_INPUT_1)
    assert parsed_input
    assert isinstance(parsed_input, tuple)
    assert all(isinstance(tile, tuple) for tile in parsed_input)
    assert all(isinstance(component, int) for tile in parsed_input for component in tile)


@pytest.mark.parametrize(
    "given_corner_a, given_corner_b, expected_area",
    (
        ((0, 0), (0, 0), 1),
        ((0, 0), (1, 1), 4),
        ((0, 0), (2, 2), 9),
        ((2, 5), (9, 7), 24),
        ((7, 1), (11, 7), 35),
        ((7, 3), (2, 3), 6),
        ((2, 5), (11, 1), 50),
    ),
)
def test_calculate_area(given_corner_a, given_corner_b, expected_area):
    given_corner_a = day_09.double_point(given_corner_a)
    given_corner_b = day_09.double_point(given_corner_b)

    size = day_09.calculate_area(given_corner_a, given_corner_b)
    assert size == expected_area


@pytest.mark.parametrize(
    "given_input, given_point, expected_inside",
    (
        (TEST_INPUT_1, (7, 0), False),
        (TEST_INPUT_1, (6, 1), False),
        (TEST_INPUT_1, (7, 1), True),
        (TEST_INPUT_1, (8, 1), True),
        (TEST_INPUT_1, (7, 2), True),
        (TEST_INPUT_1, (11, 1), True),
        (TEST_INPUT_1, (9, 3), True),
        (TEST_INPUT_1, (7, 5), True),
    ),
)
def test_is_inside(given_input, given_point, expected_inside):
    given_tiles = day_09.parse_input(given_input)
    given_point = day_09.double_point(given_point)
    inside = day_09.is_inside(given_point, given_tiles)
    assert inside == expected_inside


@pytest.mark.parametrize(
    "given_input, given_corners, expected_valid",
    (
        (TEST_INPUT_1, ((7, 3), (11, 1)), True),
        (TEST_INPUT_1, ((11, 1), (7, 3)), True),  # Order is irrelevant
        (TEST_INPUT_1, ((9, 7), (9, 5)), True),
        (TEST_INPUT_1, ((9, 5), (2, 3)), True),
        (TEST_INPUT_1, ((7, 3), (9, 5)), True),
        (TEST_INPUT_1, ((2, 5), (9, 7)), False),
        (TEST_INPUT_1, ((7, 1), (11, 7)), False),
        (TEST_INPUT_1, ((2, 5), (11, 1)), False),
        (TEST_INPUT_1, ((2, 3), (7, 2)), False),
        (TEST_INPUT_1, ((11, 1), (2, 5)), False),
    ),
)
def test_rectangle_is_valid(given_input, given_corners, expected_valid):
    given_tiles = day_09.parse_input(given_input)
    given_corners = tuple(map(day_09.double_point, given_corners))
    valid = day_09.rectangle_is_valid(given_corners, given_tiles)
    assert valid == expected_valid


def test_all_tiles_are_inside():
    given_tiles = day_09.parse_input(TEST_INPUT_1)
    assert given_tiles
    for tile in given_tiles:
        assert day_09.is_inside(tile, given_tiles)


@pytest.mark.parametrize(
    "given_point, expected_point",
    (
        ((0, 0), (0, 0)),
        ((1, 1), (2, 2)),
        ((2, 3), (4, 6)),
    ),
)
def test_double_point(given_point, expected_point):
    doubled_point = day_09.double_point(given_point)
    assert doubled_point == expected_point


def test_solving_part_1_gives_expected_value():
    answer = day_09.solve_part_one(TEST_INPUT_1)
    expected_answer = 50
    assert answer == expected_answer


def test_solving_part_2_gives_expected_value():
    answer = day_09.solve_part_two(TEST_INPUT_1)
    expected_answer = 24
    assert answer == expected_answer
