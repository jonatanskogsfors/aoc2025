import pytest

from aoc2025 import day_12
from tests import INPUT_DIR

TEST_INPUT_1 = INPUT_DIR / "test_input_12_1.txt"


def test_parse_input():
    parsed_input = day_12.parse_input(TEST_INPUT_1)
    assert len(parsed_input) == 2
    shapes, spaces = parsed_input

    assert shapes
    assert isinstance(shapes, tuple)
    assert all(isinstance(shape, tuple) for shape in shapes)
    assert all(isinstance(row, tuple) for shape in shapes for row in shape)
    assert all(isinstance(block, int) for shape in shapes for row in shape for block in row)

    assert spaces
    assert isinstance(spaces, tuple)
    assert all(isinstance(space, tuple) for space in spaces)

    assert all(len(space) == 2 for space in spaces)
    assert all(len(space[0]) == 2 for space in spaces)
    assert all(isinstance(dimension, int) for space in spaces for dimension in space[0])

    assert all(len(space[1]) == len(shapes) for space in spaces)
    assert all(isinstance(amount, int) for space in spaces for amount in space[1])


@pytest.mark.parametrize(
    "given_shape, given_rotations, expected_shape",
    (
        (((0, 0, 1),(1, 0, 0),(1, 0, 1)), 0, ((0, 0, 1),(1, 0, 0),(1, 0, 1))),
        (((0, 0, 1),(1, 0, 0),(1, 0, 1)), 1, ((1, 1, 0), (0, 0, 0), (1, 0, 1))),
        (((0, 0, 1),(1, 0, 0),(1, 0, 1)), 2, ((1, 0, 1),(0, 0, 1), (1, 0, 0))),
        (((0, 0, 1),(1, 0, 0),(1, 0, 1)), 3, ((1, 0, 1),(0, 0, 0), (0, 1, 1))),
        (((0, 0, 1),(1, 0, 0),(1, 0, 1)), 4, ((0, 0, 1),(1, 0, 0),(1, 0, 1))),
    )
)
def test_rotate_shape(given_shape, given_rotations, expected_shape):
    rotated_shape = day_12.rotate(given_shape, given_rotations)
    assert rotated_shape == expected_shape

@pytest.mark.parametrize(
    "given_shape, expected_size",
    (
        (((0, 0, 0),(0, 0, 0),(0, 0, 0)), 0),
        (((0, 0, 0),(0, 1, 0),(0, 0, 0)), 1),
        (((1, 0, 0),(0, 1, 0),(0, 0, 1)), 3),
        (((1, 1, 1),(1, 1, 1),(1, 1, 1)), 9),
    )
)
def test_shape_size(given_shape, expected_size):
    shape_size = day_12.shape_size(given_shape)
    assert shape_size == expected_size

def test_solving_part_1_gives_expected_value():
    answer = day_12.solve_part_one(TEST_INPUT_1)
    # expected_answer =
    # assert answer == expected_answer


def test_solving_part_2_gives_expected_value():
    answer = day_12.solve_part_two(TEST_INPUT_1)
    # expected_answer =
    # assert answer == expected_answer
