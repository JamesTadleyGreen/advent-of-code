import datetime
from typing import List, Tuple

from data import test_text, actual_text

test_text = test_text.split("\n")
actual_text = actual_text.split("\n")


def check(text, col: str, x: tuple) -> bool:
    try:
        return col < text[x[0]][x[1]]
    except IndexError:
        return True


def naive_check(text: List[str]) -> int:
    counter = 0
    for i, row in enumerate(text):
        for j, col in enumerate(row):
            if all(
                [
                    check(text, col, x)
                    for x in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
                ]
            ):
                counter += int(col) + 1
    return counter


def basin_size(
    total: int,
    visited_nodes: List[Tuple[int, int]],
    text: List[str],
    coords: List[Tuple[int, int]],
    s: Tuple[int, int],
) -> int:
    if s[0] < 0 or s[1] < 0:
        return 0
    try:
        if text[s[0]][s[1]] == "9":
            return 0
    except IndexError:
        return 0
    for x in [(s[0], s[1] - 1), (s[0] - 1, s[1]), (s[0], s[1] + 1), (s[0] + 1, s[1])]:
        print(x)
        if x not in visited_nodes:
            visited_nodes += [x]
            total = total + basin_size(total, visited_nodes, text, coords, x) + 1
    return total


def basin_check(text: List[str]) -> int:
    coords = [(i, j) for i in range(len(text[0])) for j in range(len(text))]
    basin_sizes = []
    while len(coords) > 0:
        s = coords.pop(0)
        basin_sizes.append(basin_size(0, [], text, coords, s))
    basin_sizes.sort()
    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]


if __name__ == "__main__":
    print(basin_check(test_text))
    # print(basin_check(actual_text))
