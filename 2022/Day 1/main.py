from data import test_data, actual_data


def text_to_list(text: str):
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


if __name__ == "__main__":
    print(top_three_calories(actual_data))
