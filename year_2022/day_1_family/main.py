from year_2022.day_1_family.data import test_data, actual_data


def jamie():
    split_data = actual_data.split("\n")
    output = 0
    max_value = 0
    for data in split_data:
        if data == "":
            # print("OUTPUT:", output)
            if output > max_value:
                max_value = output
            # print("MAX VALUE:", max_value)
            output = 0
        else:
            output = output + int(data)
    # print(max_value)
    return max_value
