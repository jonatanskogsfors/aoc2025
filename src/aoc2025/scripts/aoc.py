import argparse
import sys
import time
from http import HTTPStatus
from pathlib import Path

import jinja2
import requests

import aoc2025

COOKIE_PATH = Path("session.txt")
INPUT_DIR = Path("input")
ENDPOINT_PATTERN = "https://adventofcode.com/2025/day/{}/input"


def main():
    arguments = handle_arguments()

    match arguments.command:
        case "download":
            download_input(arguments.day)
        case "run":
            if arguments.day is None:
                run_all()
            else:
                run_solution(arguments.day)
        case "create":
            create_day(arguments.day)


def download_input(day: int):
    input_path = INPUT_DIR / f"input_{day:02}.txt"

    if input_path.exists():
        sys.exit(f"Input data for day {day} already downloaded.")

    cookie = COOKIE_PATH.read_text().strip()
    cookies = {"session": cookie}
    url = ENDPOINT_PATTERN.format(day)
    response = requests.get(url, cookies=cookies)
    if response.status_code == HTTPStatus.OK:
        INPUT_DIR.mkdir(exist_ok=True)
        print(f"Writing '{input_path}'")
        input_path.write_text(response.text)
    else:
        sys.exit(f"Failed to download input for day {day}:\n{response.text}")


def run_all():
    days = aoc2025.__all__
    t0 = time.perf_counter()
    for day in days:
        if day_module := getattr(aoc2025, day):
            print(f"{day.replace('_', ' ').title()}:")
            day_module.main()
            print()
    t1 = time.perf_counter()
    print(f"All days  {t1 - t0:>8.3f} s")


def run_solution(day: int):
    if day_module := getattr(aoc2025, f"day_{day:02}"):
        day_module.main()


def create_day(day: int):
    environment = jinja2.Environment(loader=jinja2.PackageLoader("aoc2025"))

    day_path = aoc2025.ROOT_DIR / f"day_{day:02}.py"
    if not day_path.exists():
        template = environment.get_template("day.py")
        new_day = template.render(day=day)
        day_path.write_text(new_day)

    test_path = aoc2025.TEST_DIR / f"test_day_{day:02}.py"
    if not test_path.exists():
        template = environment.get_template("test_day.py")
        new_test = template.render(day=day)
        test_path.write_text(new_test)


def handle_arguments():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(title="Commands", dest="command")
    subparsers.required = True

    download_parser = subparsers.add_parser("download", help="Download input.")
    download_parser.add_argument("day", type=int)

    run_parser = subparsers.add_parser("run", help="Run solution for day")
    run_parser.add_argument("day", type=int, nargs="?")

    run_parser = subparsers.add_parser("create", help="Create template for day")
    run_parser.add_argument("day", type=int)

    return parser.parse_args()


if __name__ == "__main__":
    main()
