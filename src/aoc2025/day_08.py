import heapq
import itertools
import math
import time
from pathlib import Path


class Circuits:
    def __init__(self):
        self._circuits = []

    def connect(self, a, b):
        circuit_a = None
        circuit_b = None

        for circuit in self._circuits:
            if a in circuit:
                circuit_a = circuit
            if b in circuit:
                circuit_b = circuit

        if not circuit_a and not circuit_b:
            self._circuits.append({a, b})

        if circuit_a is circuit_b:
            return

        if circuit_a and not circuit_b:
            circuit_a.add(b)

        if circuit_b and not circuit_a:
            circuit_b.add(a)

        if circuit_a and circuit_b:
            circuit_a |= circuit_b
            self._circuits.remove(circuit_b)

    def __len__(self):
        return len(self._circuits)

    @property
    def size(self):
        return math.prod(sorted(len(circuit) for circuit in self._circuits)[-3:])

    def connected(self, all_junctions: set[tuple[int, int, int]]) -> bool:
        return all_junctions in self._circuits


def parse_input(input_path: Path) -> tuple[tuple[int, int, int], ...]:
    return tuple(
        tuple(map(int, row.split(","))) for row in input_path.read_text().splitlines()
    )


def calculate_distance(given_point_a, given_point_b):
    x1, y1, z1 = given_point_a
    x2, y2, z2 = given_point_b
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)


def created_heap(given_points):
    heap = []
    for a, b in itertools.combinations(given_points, 2):
        heapq.heappush(heap, (calculate_distance(a, b), {a, b}))
    return heap


def get_closest(heap):
    return heapq.heappop(heap)[1]


def solve_part_one(input_path: Path, number_of_junctions: int):
    junctions = parse_input(input_path)
    heap = created_heap(junctions)

    circuits = Circuits()

    for _ in range(number_of_junctions):
        a, b = get_closest(heap)
        circuits.connect(a, b)

    return circuits.size


def solve_part_two(input_path: Path):
    junctions = parse_input(input_path)
    heap = created_heap(junctions)

    circuits = Circuits()

    all_junctions = set(junctions)
    x1, x2 = 0, 0
    while not circuits.connected(all_junctions):
        a, b = get_closest(heap)
        circuits.connect(a, b)
        x1 = a[0]
        x2 = b[0]

    return x1 * x2


def main():
    t0 = time.perf_counter()
    result_1 = solve_part_one(Path("input/input_08.txt"), 1000)
    t1 = time.perf_counter()
    print(f"Part 1 {t1 - t0:>8.3f} s\t{result_1}")

    t2 = time.perf_counter()
    result_2 = solve_part_two(Path("input/input_08.txt"))
    t3 = time.perf_counter()
    print(f"Part 2 {t3 - t2:>8.3f} s\t{result_2}")
    print(f"Total  {t3 - t0:>8.3f} s")


if __name__ == "__main__":
    main()
