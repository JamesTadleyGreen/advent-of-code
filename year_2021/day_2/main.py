from year_2021.day_3.data import test_data, actual_data


def power_consumption(data: str) -> int:
    lines = data.split("\n")
    number_of_lines = len(lines)
    majority = number_of_lines // 2
    counter = [0] * len(lines[0])
    print(counter)
    for line in lines:
        for i, char in enumerate([int(i) for i in line]):
            counter[i] += char
    gamma_list = "".join(["1" if i > majority else "0" for i in counter])
    epsilon_list = "".join(["0" if i == "1" else "1" for i in gamma_list])
    return int(gamma_list, 2) * int(epsilon_list, 2)


def jamie():
    return power_consumption(actual_data)
