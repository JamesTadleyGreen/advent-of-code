from typing import List, Tuple
from year_2022.day_5.data import test_data, actual_data


def get_initial_data(lines: List[str]) -> Tuple[List[str], List[str]]:
    i = 0
    while lines[i] != "":
        i += 1
    return lines[: i - 1], lines[i + 1 :]


def parse_initial_position(lines: List[str]) -> List[List[str]]:
    number_of_stacks = len(lines[0]) // 4 + 1
    return [
        [crate[4 * i + 1] for crate in lines if crate[4 * i + 1] != " "]
        for i in range(number_of_stacks)
    ]


def parse_rearrangement_procedure(lines: List[str]) -> List[List[int]]:
    return [
        [int(split) for i, split in enumerate(line.split(" ")) if i in [1, 3, 5]]
        for line in lines
    ]


def iterate_over_positions(
    position: List[List[str]],
    rearrangement_procedure: List[List[int]],
    flip: bool,
) -> List[List[str]]:
    if flip:
        f = -1
    else:
        f = 1
    for num, start, end in rearrangement_procedure:
        position[end - 1] = position[start - 1][:num][::f] + position[end - 1]
        position[start - 1] = position[start - 1][num:]
    return position


def get_top_crates(position: List[List[str]]) -> str:
    output = ""
    for stack in position:
        output += stack.pop(0)
    return output


def top_crate(data: str, flip: bool = True) -> str:
    lines = data.split("\n")
    initial_pos_data, rearrangement_procedure = get_initial_data(lines)
    initial_pos = parse_initial_position(initial_pos_data)
    rearrangement_procedure = parse_rearrangement_procedure(rearrangement_procedure)
    final_pos = iterate_over_positions(initial_pos, rearrangement_procedure, flip)
    final_crate = get_top_crates(final_pos)
    return final_crate


def jamie():
    # return top_crate(actual_data)
    return top_crate(actual_data, flip=False)


def alex():

    text_crates, instructions = get_initial_data(actual_data.split("\n"))
    text_crates = parse_initial_position(text_crates)
    # text_crates = [i[::-1] for i in text_crates]
    for inst in instructions:
        amount, start, end = (
            inst.replace("move ", "")
            .replace(" from ", ",")
            .replace(" to ", ",")
            .split(",")
        )
        text_crates[int(end) - 1] = (
            text_crates[int(end) - 1]
            + text_crates[int(start) - 1][(int(amount) * -1) :]
        )
        for _ in range(int(amount)):
            crate = text_crates[int(start) - 1].pop()

    for crate in text_crates:
        crate[-1]


def alex1():

    text_crates, instructions = get_initial_data(actual_data.split("\n"))
    text_crates = parse_initial_position(text_crates)
    # text_crates = [i[::-1] for i in text_crates]
    for inst in instructions:
        amount, start, end = (
            inst.replace("move ", "")
            .replace(" from ", ",")
            .replace(" to ", ",")
            .split(",")
        )
        text_crates[int(end) - 1] = (
            text_crates[int(end) - 1]
            + text_crates[int(start) - 1][(int(amount) * -1) :]
        )
        # for _ in range(int(amount)):
        text_crates[int(start) - 1] = text_crates[int(start) - 1][: int(amount) + 1]

    for crate in text_crates:
        crate[-1]
