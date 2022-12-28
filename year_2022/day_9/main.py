from typing import List, Set, Tuple
from year_2022.day_9.data import test_data, test_data_1, actual_data

direction_lookup = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}


def number_of_tail_positions(data: str) -> int:
    position = ((0, 0), (0, 0))
    position_set = set()
    for instruction in data.split("\n"):
        direction, amount = instruction.split(" ")
        amount = int(amount)
        for _ in range(amount):
            head_position = move_position(position[0], direction)
            tail_position = new_tail_position((head_position, position[1]), direction)
            position = (head_position, tail_position)
            position_set.add(position[1])
    return len(position_set)


def move_position(
    position: Tuple[int, int], direction: str, amount: int = 1
) -> Tuple[int, int]:
    direction_tuple = direction_lookup[direction]
    return tuple(position[i] + amount * direction_tuple[i] for i in [0, 1])


def l_1_distance(first: Tuple[int, int], second: Tuple[int, int]) -> int:
    return abs(first[0] - second[0]) + abs(first[1] - second[1])


def new_tail_position(
    position: Tuple[Tuple[int, int], Tuple[int, int]], direction: str
) -> Tuple[int, int]:
    head, tail = position
    # Easy, horizontal or vertical case
    for i in [0, 1]:
        if head[i] == tail[i]:
            if l_1_distance(head, tail) > 1:
                return move_position(tail, direction)
    # Hard(er) diagonal case
    if l_1_distance(head, tail) > 2:
        if head[1] - tail[1] == 2:
            return (head[0], head[1] - 1)
        elif head[1] - tail[1] == -2:
            return (head[0], head[1] + 1)
        elif head[0] - tail[0] == 2:
            return (head[0] - 1, head[1])
        else:
            return (head[0] + 1, head[1])
    return tail


def show_board(
    positions: List[Tuple[int, int]],
    width,
    height,
    visited: Set[Tuple[int, int]],
):
    blank_board = [("." * width) for _ in range(height)]
    for v in visited:
        blank_board[v[0] + (height // 2)] = replace_char(
            blank_board[v[0] + (height // 2)], "#", v[1] + (width // 2)
        )
    for i, loc in enumerate(positions):
        loc = (loc[0] + width // 2, loc[1] + width // 2)
        if i == 0:
            tag = "H"
        else:
            tag = str(i)
        blank_board[loc[0]] = replace_char(blank_board[loc[0]], tag, loc[1])
    # blank_board[height // 2] = replace_char(blank_board[height // 2], "c", width // 2)
    for row in blank_board:
        for i in row:
            print(i, end=" ")
        print("")


def replace_char(s: str, replace: str, position: int) -> str:
    return "".join([replace if i == position else j for i, j in enumerate(s)])


def number_of_tail_positions_in_ten_knot_rope(data: str) -> int:
    position = [(0, 0) for _ in range(10)]
    print(position)
    position_set = set()
    for instruction in data.split("\n"):
        direction, amount = instruction.split(" ")
        amount = int(amount)
        for _ in range(amount):
            position[0] = move_position(position[0], direction)
            for i in range(1, 10):
                position[i] = new_tail_position(
                    (position[i - 1], position[i]), direction
                )
            position_set.add(position[-1])
            show_board(position, 21, 21, position_set)
            input()
    return len(position_set)


def jamie():
    # return number_of_tail_positions(actual_data)
    return number_of_tail_positions_in_ten_knot_rope(test_data_1)
