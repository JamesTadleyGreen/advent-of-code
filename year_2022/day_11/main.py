from typing import Dict, List, Set, Tuple, TypedDict
from year_2022.day_11.data import test_data, actual_data

from math import gcd

# import numpy

# from fractions import gcd # Python versions below 3.5
from functools import reduce  # Python version 3.x


def lcm(denominators: List[int]) -> int:
    # https://stackoverflow.com/questions/37237954/calculate-the-lcm-of-a-list-of-given-numbers-in-python
    return reduce(lambda a, b: a * b // gcd(a, b), denominators)


class MonkeyNotes(TypedDict):
    transformation: Tuple[str, int]
    test: int
    true: int
    false: int
    handles: int


def parse_data(data: str) -> Tuple[Dict[int, List[int]], Dict[int, MonkeyNotes]]:
    monkey_list = data.split("\n\n")
    monkey_queue = {}
    monkey_notes = {}
    for i, monkey in enumerate(monkey_list):
        monkey_data = monkey.split("\n")
        operation, amount = monkey_data[2].split(" ")[-2:]
        if amount == "old":
            amount = -1
        else:
            amount = int(amount)
        monkey_queue[i] = [int(i) for i in monkey_data[1].split(":")[1].split(",")]
        monkey_notes[i] = {
            "transformation": (operation, amount),
            "test": int(monkey_data[3].split(" ")[-1]),
            "true": int(monkey_data[4].split(" ")[-1]),
            "false": int(monkey_data[5].split(" ")[-1]),
            "handles": 0,
        }
    return monkey_queue, monkey_notes


def update_item_value(item: int, transformation: Tuple[str, int], lcm: int) -> int:
    operation, value = transformation
    if value == -1:
        value = item
    match operation:
        case "+":
            item += value
        case "*":
            item *= value
    return item % lcm


def enumerate_round(
    queue: Dict[int, List[int]], notes: Dict[int, MonkeyNotes], lcm: int
) -> Tuple[Dict[int, List[int]], Dict[int, MonkeyNotes]]:
    for monkey, q in queue.items():
        while q != []:
            notes[monkey]["handles"] += 1
            item = q.pop(0)
            item = update_item_value(item, notes[monkey]["transformation"], lcm)
            if item % notes[monkey]["test"] == 0:
                update_monkey = notes[monkey]["true"]
            else:
                update_monkey = notes[monkey]["false"]
            queue[update_monkey].append(item)
    return queue, notes


def enumerate_rounds(
    queue: Dict[int, List[int]],
    notes: Dict[int, MonkeyNotes],
    number_of_rounds: int,
    lcm: int,
) -> Tuple[Dict[int, List[int]], Dict[int, MonkeyNotes]]:
    for _ in range(number_of_rounds):
        queue, notes = enumerate_round(queue, notes, lcm)
    return queue, notes


def product_of_top_two_inspections(data: str) -> int:
    queue, monkey_notes = parse_data(data)
    list_of_tests = [i["test"] for i in monkey_notes.values()]
    LCM = lcm(list_of_tests)
    print(list_of_tests)
    queue, monkey_notes = enumerate_rounds(queue, monkey_notes, 10_000, LCM)
    list_of_handles = sorted(
        [v["handles"] for v in monkey_notes.values()], reverse=True
    )
    print(monkey_notes)
    print(queue)
    print(list_of_handles)
    return list_of_handles[0] * list_of_handles[1]


def jamie() -> int:
    return product_of_top_two_inspections(actual_data)
