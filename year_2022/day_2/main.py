import datetime
from typing import List
from year_2022.day_2.data import test_data, actual_data


def parse_data(data: str) -> List[str]:
    return data.split("\n")


def result_of_game(game: str) -> int:
    match game:
        case "A X":
            return 3 + 1
        case "A Y":
            return 6 + 2
        case "A Z":
            return 0 + 3
        case "B X":
            return 0 + 1
        case "B Y":
            return 3 + 2
        case "B Z":
            return 6 + 3
        case "C X":
            return 6 + 1
        case "C Y":
            return 0 + 2
        case "C Z":
            return 3 + 3


def evaluate_strategy(data: str) -> int:
    data_list = parse_data(data)
    return sum(map(result_of_game, data_list))


def result_of_correct_game(game: str) -> int:
    match game:
        case "A X":
            return 0 + 3
        case "A Y":
            return 3 + 1
        case "A Z":
            return 6 + 2
        case "B X":
            return 0 + 1
        case "B Y":
            return 3 + 2
        case "B Z":
            return 6 + 3
        case "C X":
            return 0 + 2
        case "C Y":
            return 3 + 3
        case "C Z":
            return 6 + 1


scores = {
    "A X": 0 + 3,
    "A Y": 3 + 1,
    "A Z": 6 + 2,
    "B X": 0 + 1,
    "B Y": 3 + 2,
    "B Z": 6 + 3,
    "C X": 0 + 2,
    "C Y": 3 + 3,
    "C Z": 6 + 1,
}


def evaluate_correct_strategy(data: str) -> int:
    data_list = parse_data(data)
    return sum(map(result_of_correct_game, data_list))


def jamie():
    # evaluate_strategy(actual_data)
    return evaluate_correct_strategy(actual_data)


def alex():
    data_list = parse_data(actual_data)
    total = 0
    for data in data_list:
        total += scores[data]
    return total
