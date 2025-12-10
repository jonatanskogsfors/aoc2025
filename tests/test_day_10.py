import pytest

from aoc2025 import day_10
from tests import INPUT_DIR

TEST_INPUT_1 = INPUT_DIR / "test_input_10_1.txt"


def test_parse_input():
    parsed_input = day_10.parse_input(TEST_INPUT_1)

    assert parsed_input
    assert isinstance(parsed_input, tuple)

    assert all(len(row) == 3 for row in parsed_input)

    assert all(isinstance(row[0], str) for row in parsed_input)

    assert all(isinstance(row[1], tuple) for row in parsed_input)
    assert all(isinstance(button, tuple) for row in parsed_input for button in row[1])
    assert all(
        isinstance(component, int)
        for row in parsed_input
        for button in row[1]
        for component in button
    )


@pytest.mark.parametrize(
    "given_lights, expected_value",
    (
        ("[.##.]", 0b0110),
        ("[...#.]", 0b00010),
        ("[.###.#]", 0b011101),
    ),
)
def test_lights_value(given_lights, expected_value):
    light_value = day_10.lights_value(given_lights)
    assert light_value == expected_value


@pytest.mark.parametrize(
    "given_button, given_width, expected_mask", (((0, 3, 4), 6, 0b100110),)
)
def test_mask_from_button(given_button, given_width, expected_mask):
    mask = day_10.mask_from_button(given_button, bit_depth=given_width)
    assert mask == expected_mask


@pytest.mark.parametrize(
    "given_lights, given_button, expected_lights", (("[#.....]", (0, 3, 4), "[...##.]"),)
)
def test_button_to_number(given_lights, given_button, expected_lights):
    lights = day_10.press_button(given_lights, given_button)
    assert lights == expected_lights


@pytest.mark.parametrize(
    "given_lights, given_buttons, expected_lights",
    (
        ("[......]", ((0,),), "[#.....]"),
        ("[......]", ((0,), (0,)), "[......]"),
        ("[......]", ((1, 3, 5), (0, 2, 4)), "[######]"),
        ("[......]", ((1, 3), (0, 2), (2, 3)), "[##....]"),
    ),
)
def test_combine_two_button_presses(given_lights, given_buttons, expected_lights):
    bit_depth = len(given_lights) - 2
    combined_mask = day_10.mask_from_button(*given_buttons, bit_depth=bit_depth)
    value = day_10.lights_value(given_lights)

    value_with_combined_mask = value ^ combined_mask
    assert (
        day_10.lights_from_value(value_with_combined_mask, bit_depth) == expected_lights
    )

    value_with_serial_masks = value
    for button in given_buttons:
        mask = day_10.mask_from_button(button, bit_depth=bit_depth)
        value_with_serial_masks ^= mask

    assert value_with_combined_mask == value_with_serial_masks


@pytest.mark.parametrize(
    "given_target, given_buttons, expected_sequence",
    (
        ("[.##.]", ((3,), (1, 3), (2,), (2, 3), (0, 2), (0, 1)), 2),
        ("[...#.]", ((0, 2, 3, 4), (2, 3), (0, 4), (0, 1, 2), (1, 2, 3, 4)), 3),
        ("[.###.#]", ((0, 1, 2, 3, 4), (0, 3, 4), (0, 1, 2, 4, 5), (1, 2)), 2),
    ),
)
def test_shortest_sequence(given_target, given_buttons, expected_sequence):
    sequence = day_10.shortest_sequence(given_target, given_buttons)
    assert sequence == expected_sequence


def test_solving_part_1_gives_expected_value():
    answer = day_10.solve_part_one(TEST_INPUT_1)
    expected_answer = 7
    assert answer == expected_answer


def test_solving_part_2_gives_expected_value():
    answer = day_10.solve_part_two(TEST_INPUT_1)  # noqa: F841
    # expected_answer =
    # assert answer == expected_answer
