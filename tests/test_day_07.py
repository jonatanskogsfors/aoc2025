import pytest

from aoc2025 import day_07
from tests import INPUT_DIR

TEST_INPUT_1 = INPUT_DIR / "test_input_07_1.txt"


def test_parse_input():
    parsed_input = day_07.parse_input(TEST_INPUT_1)

    assert parsed_input
    assert len(parsed_input) == 2
    splitters, start = parsed_input

    assert isinstance(splitters, set)

    assert len(start) == 2
    x, y = start
    assert isinstance(x, int)
    assert isinstance(y, int)


@pytest.mark.parametrize(
    "given_splitters, given_position, expected_splits",
    (
        (set(), (1, 0), 0),
        ({(1, 1)}, (1, 0), 1),
        ({(2, 1), (1, 2), (2, 3), (3, 4)}, (2, 0), 4),
    ),
)
def test_beam(given_splitters, given_position, expected_splits):
    splits = day_07.beam(given_splitters, given_position)
    assert splits == expected_splits


@pytest.mark.parametrize(
    "given_splitters, given_position, expected_timelines",
    (
        (set(), (1, 0), 1),
        ({(1, 1)}, (1, 0), 2),
        ({(2, 1), (1, 2), (2, 3), (3, 4)}, (2, 0), 6),
    ),
)
def test_quantum_beam(given_splitters, given_position, expected_timelines):
    timelines = day_07.quantum_beam(given_splitters, given_position)
    assert timelines == expected_timelines


def test_solving_part_1_gives_expected_value():
    answer = day_07.solve_part_one(TEST_INPUT_1)
    expected_answer = 21
    assert answer == expected_answer


def test_solving_part_2_gives_expected_value():
    answer = day_07.solve_part_two(TEST_INPUT_1)
    expected_answer = 40
    assert answer == expected_answer
