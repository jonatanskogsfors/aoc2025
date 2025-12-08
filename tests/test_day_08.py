import pytest

from aoc2025 import day_08
from tests import INPUT_DIR

TEST_INPUT_1 = INPUT_DIR / "test_input_08_1.txt"


def test_parse_input():
    parsed_input = day_08.parse_input(TEST_INPUT_1)
    assert isinstance(parsed_input, tuple)
    assert all(isinstance(row, tuple) for row in parsed_input)
    assert all(isinstance(element, int) for row in parsed_input for element in row)


@pytest.mark.parametrize(
    "given_point_a, given_point_b, expected_distance",
    (
        ((0, 0, 0), (0, 0, 0), 0),
        ((0, 0, 0), (1, 2, 2), 3),
        ((-2, -10, -11), (0, 0, 0), 15),
    ),
)
def test_calculate_distance(given_point_a, given_point_b, expected_distance):
    distance = day_08.calculate_distance(given_point_a, given_point_b)
    assert distance == expected_distance


@pytest.mark.parametrize(
    "given_points, expected_closest_pair",
    ((((0, 0, 0), (100, 100, 100), (1, 1, 1)), {(0, 0, 0), (1, 1, 1)}),),
)
def test_remember_shortest_distance(given_points, expected_closest_pair):
    heap = day_08.created_heap(given_points)
    closest_pair = day_08.get_closest(heap)
    assert closest_pair == expected_closest_pair


def test_get_closest_junctions_in_test_input():
    # Given the junctions in the test input
    given_junctions = day_08.parse_input(TEST_INPUT_1)

    # When pushing the junctions into a heap
    heap = day_08.created_heap(given_junctions)

    # Then the expected distance order can be retrieved
    expected_order = (
        {(162, 817, 812), (425, 690, 689)},
        {(162, 817, 812), (431, 825, 988)},
        {(906, 360, 560), (805, 96, 715)},
        {(431, 825, 988), (425, 690, 689)},
    )

    order = (
        day_08.get_closest(heap),
        day_08.get_closest(heap),
        day_08.get_closest(heap),
        day_08.get_closest(heap),
    )

    assert order == expected_order


def test_create_circuit():
    # Given three points
    given_junction_a = (0, 0, 0)
    given_junction_b = (1, 1, 1)
    given_junction_c = (2, 2, 2)
    given_junction_d = (3, 3, 3)

    # Given a circuits object
    circuits = day_08.Circuits()

    # When connecting two junctions
    circuits.connect(given_junction_a, given_junction_b)

    # Then the len of the circuits is one
    assert len(circuits) == 1

    # And the size of the circuits is two
    assert circuits.size == 1 * 2

    # When connection two different circuits
    circuits.connect(given_junction_c, given_junction_d)

    # Then the number of circuits is two
    assert len(circuits) == 2

    # And the size of the circuits is four
    assert circuits.size == 2 * 2

    # When connection two junctions that are already in two different junctions
    circuits.connect(given_junction_a, given_junction_d)

    # Then the number of circuits combines into one
    assert len(circuits) == 1

    # And the size of the circuit is four
    assert circuits.size == 1 * 4


def test_solving_part_1_gives_expected_value():
    answer = day_08.solve_part_one(TEST_INPUT_1, 10)
    expected_answer = 40
    assert answer == expected_answer


def test_solving_part_2_gives_expected_value():
    answer = day_08.solve_part_two(TEST_INPUT_1)
    expected_answer = 25272
    assert answer == expected_answer
