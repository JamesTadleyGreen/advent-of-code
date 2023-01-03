from typing import List, Set, Tuple
from year_2022.day_13.data import test_data, actual_data

def display_cave(lines: List[str]) -> str:
    pass

def part1(data: str) -> int:
    lines = data.split('\n')
    print(display_cave(lines))

def jamie() -> int:
    return part1(test_data)
