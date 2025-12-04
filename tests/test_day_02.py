import pytest

from aoc2025 import day_02
from tests import INPUT_DIR

TEST_INPUT_1 = INPUT_DIR / "test_input_02_1.txt"


def test_parse_input():
    parsed_input = day_02.parse_input(TEST_INPUT_1)
    assert isinstance(parsed_input, tuple)
    for id_range in parsed_input:
        assert isinstance(id_range, tuple)
        left, right = id_range
        assert isinstance(left, int)
        assert isinstance(right, int)


@pytest.mark.parametrize(
    "given_range, expected_repeats",
    (
        ((11, 22), {11, 22}),
        ((95, 115), {99}),
        ((998, 1012), {1010}),
        ((1188511880, 1188511890), {1188511885}),
        ((222220, 222224), {222222}),
        ((1698522, 1698528), set()),
        ((446443, 446449), {446446}),
        ((38593856, 38593862), {38593859}),
    ),
)
def test_doubles_in_range(given_range, expected_repeats):
    repeats = day_02.doubles_in_range(given_range)
    assert repeats == expected_repeats


@pytest.mark.parametrize(
    "given_range, expected_repeats",
    (
        ((11, 22), {11, 22}),
        ((95, 115), {99, 111}),
        ((998, 1012), {999, 1010}),
        ((1188511880, 1188511890), {1188511885}),
        ((222220, 222224), {222222}),
        ((1698522, 1698528), set()),
        ((446443, 446449), {446446}),
        ((38593856, 38593862), {38593859}),
        ((565653, 565659), {565656}),
        ((824824821, 824824827), {824824824}),
        ((2121212118, 2121212124), {2121212121}),
    ),
)
def test_repeats_in_range(given_range, expected_repeats):
    repeats = day_02.repeats_in_range(given_range)
    assert repeats == expected_repeats


def test_solving_part_1_gives_expected_value():
    answer = day_02.solve_part_one(TEST_INPUT_1)
    expected_answer = 1227775554
    assert answer == expected_answer


def test_solving_part_2_gives_expected_value():
    answer = day_02.solve_part_two(TEST_INPUT_1)
    expected_answer = 4174379265
    assert answer == expected_answer
