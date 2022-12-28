from typing import List, Set, Tuple
from year_2022.day_13.data import test_data, actual_data

def compare(x: str, y: str) -> bool:
    for i in range(len(x)):
        if x[0] == '[':
            _x = ''
            c = x[1]
            while c != ']':
                c = 

def sum_of_indices_of_ordered_pairs(data: str) -> int:
    lines = data.split("\n")
    print(lines)
    for i in range(0, len(lines), 3):
        left = lines[i]
        right = lines[i + 1]
        compare(left, right)
        if left[0] == '[':
            # Then list
        print(left, right)


def jamie() -> int:
    return sum_of_indices_of_ordered_pairs(test_data)
