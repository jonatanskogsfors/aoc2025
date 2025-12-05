import pytest

from aoc2025 import day_05
from tests import INPUT_DIR

TEST_INPUT_1 = INPUT_DIR / "test_input_05_1.txt"


def test_parse_input():
    parsed_input = day_05.parse_input(TEST_INPUT_1)

    assert isinstance(parsed_input, tuple)
    assert len(parsed_input) == 2
    fresh_ranges, ingredients = parsed_input

    assert fresh_ranges
    assert isinstance(fresh_ranges, tuple)
    assert all(isinstance(fresh_range, list) for fresh_range in fresh_ranges)
    assert all(
        isinstance(element, int)
        for fresh_range in fresh_ranges
        for element in fresh_range
    )

    assert ingredients
    assert isinstance(ingredients, tuple)
    assert all(isinstance(ingredient, int) for ingredient in ingredients)


@pytest.mark.parametrize(
    "given_ingredient, given_fresh_range, expected_freshness",
    (
        (1, [2, 4], False),
        (2, [2, 4], True),
        (3, [2, 4], True),
        (4, [2, 4], True),
        (5, [2, 4], False),
    ),
)
def test_is_fresh_with_one_range(given_ingredient, given_fresh_range, expected_freshness):
    freshness = day_05.is_fresh(given_ingredient, [given_fresh_range])
    assert freshness == expected_freshness


@pytest.mark.parametrize(
    "given_ingredient, given_fresh_ranges, expected_freshness",
    (
        (2, [[1, 2], [4, 5]], True),
        (3, [[1, 2], [4, 5]], False),
        (4, [[1, 2], [4, 5]], True),
    ),
)
def test_is_fresh_with_multiple_ranges(
    given_ingredient, given_fresh_ranges, expected_freshness
):
    freshness = day_05.is_fresh(given_ingredient, given_fresh_ranges)
    assert freshness == expected_freshness


@pytest.mark.parametrize(
    "given_ranges, expected_ranges",
    (
        ([[1, 2]], [[1, 2]]),
        ([[1, 2], [4, 5]], [[1, 2], [4, 5]]),
        ([[1, 3], [2, 4]], [[1, 4]]),
        ([[1, 4], [2, 3]], [[1, 4]]),
        ([[1, 2], [3, 4]], [[1, 4]]),
        ([[1, 3], [2, 6], [5, 7]], [[1, 7]]),
        ([[3, 5], [10, 14], [16, 20], [12, 18]], [[3, 5], [10, 20]]),
    ),
)
def test_reduce_ranges(given_ranges, expected_ranges):
    reduced_ranges = day_05.reduce_ranges(given_ranges)
    assert reduced_ranges == expected_ranges


@pytest.mark.parametrize(
    "given_fresh_ranges, expected_ingredients",
    (
        (((1, 2),), 2),
        (((1, 2), (4, 5)), 4),
        (((1, 2), (2, 3)), 3),
    ),
)
def test_all_fresh_ingredients(given_fresh_ranges, expected_ingredients):
    fresh_ingredients = day_05.all_fresh_ingredients(given_fresh_ranges)
    assert fresh_ingredients == expected_ingredients


def test_solving_part_1_gives_expected_value():
    answer = day_05.solve_part_one(TEST_INPUT_1)
    expected_answer = 3
    assert answer == expected_answer


def test_solving_part_2_gives_expected_value():
    answer = day_05.solve_part_two(TEST_INPUT_1)
    expected_answer = 14
    assert answer == expected_answer
