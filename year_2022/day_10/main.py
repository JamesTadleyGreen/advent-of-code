from typing import List, Set, Tuple
from year_2022.day_10.data import test_data, actual_data


def check_cycle(cycle: int, register: int) -> int:
    if cycle in range(20, 280, 40):
        print(cycle, register)
        return register * cycle
    return 0


def sum_of_signal_strengths(data: str) -> int:
    operations = data.split("\n")
    register = 1
    output = 0
    cycle = 1
    for operation in operations:
        if operation == "noop":
            cycle += 1
            output += check_cycle(cycle, register)
            continue
        else:
            _, amount = operation.split(" ")
            amount = int(amount)
            cycle += 1
            output += check_cycle(cycle, register)
            register += amount
            cycle += 1
            output += check_cycle(cycle, register)

    return output


def jamie() -> int:
    return sum_of_signal_strengths(actual_data)
