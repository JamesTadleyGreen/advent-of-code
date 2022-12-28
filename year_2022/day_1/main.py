import datetime
from typing import List
from year_2022.day_1.data import test_data, actual_data


def text_to_list(text: str) -> List[List[str]]:
    lines = text.split("\n")
    output = []
    tmp = []
    for i in lines:
        if i == "":
            output.append(tmp)
            tmp = []
        else:
            tmp.append(int(i))
    output.append(tmp)
    return output


def text_to_list(text: str) -> List[List[int]]:
    return [[int(j) for j in i.split("\n")] for i in text.split("\n\n")]


def most_calories(text: str) -> int:
    list_of_lists = text_to_list(text)
    max_elf = 0
    for l in list_of_lists:
        if (s := sum(l)) > max_elf:
            max_elf = s
    return max_elf


def top_three_calories(text: str) -> int:
    list_of_lists = text_to_list(text)
    summed_list = sorted(list(map(sum, list_of_lists)))
    return sum(summed_list[-3:])


def jamie():
    top_three_calories(actual_data)


def jack():
    data = actual_data
    list_line = data.split("\n\n")
    sum_list = []
    for line in list_line:
        new_list = line.split("\n")
        new_list = [int(x) for x in new_list]
        new_list_sum = sum(new_list)
        sum_list.append(new_list_sum)
    sum_list.sort()
    return sum(sum_list[-3:])


if __name__ == "__main__":
    jamie()
