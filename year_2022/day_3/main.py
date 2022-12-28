from typing import List, Set
import string
from year_2022.day_3.data import test_data, actual_data


def value(char: str) -> int:
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 65 + 27


def priority(backpack: str) -> int:
    size = len(backpack)
    compartment_size = size // 2
    compartments = [
        set(i) for i in [backpack[:compartment_size], backpack[compartment_size:]]
    ]
    common = set.intersection(
        *compartments
    ).pop()  # Okay as question assures uniqueness
    return value(common)


def summed_priorities(data: str) -> int:
    lines = data.split("\n")
    priority_sum = 0
    for line in lines:
        priority_sum += priority(line)
    return priority_sum


def common(backpacks: List[Set[str]]) -> int:
    return value(
        set.intersection(*backpacks).pop()
    )  # Okay as question assures uniqueness


def summed_three_common_priorities(data: str) -> int:
    lines = [set(line) for line in data.split("\n")]
    common_sum = 0
    for i in range(0, len(lines), 3):
        common_sum += common(lines[i : i + 3])
    return common_sum


def jamie():
    summed_priorities(actual_data)
    summed_three_common_priorities(actual_data)


points = {i: points + 1 for points, i in enumerate(string.ascii_letters)}


def alex():
    def part_1():
        backpacks = actual_data.split("\n")
        total = 0
        for backpack in backpacks:
            total += points[
                list(
                    set(list(backpack)[: (len(backpack) // 2)])
                    & set(list(backpack)[(len(backpack) // 2) :])
                )[0]
            ]
        return total

    def part_2():
        backpacks = actual_data.split("\n")
        total = 0
        for i in range(0, len(backpacks), 3):
            total += points[
                list(
                    set(list(backpacks[i]))
                    & set(list(backpacks[i + 1]))
                    & set(list(backpacks[i + 2]))
                )[0]
            ]
        return total

    part_1()
    part_2()
