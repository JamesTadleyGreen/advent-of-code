from year_2021.day_2.data import test_data, actual_data


def multiplied_final_position(data: str) -> int:
    lines = data.split("\n")
    horizontal, vertical = 0, 0
    for line in lines:
        if line.startswith("forward"):
            horizontal += int(line[-1])
        elif line.startswith("up"):
            vertical -= int(line[-1])
        else:
            vertical += int(line[-1])
    return horizontal * vertical


def multiplied_final_position_with_aim(data: str) -> int:
    lines = data.split("\n")
    horizontal, vertical, aim = 0, 0, 0
    for line in lines:
        if line.startswith("forward"):
            horizontal += int(line[-1])
            vertical += int(line[-1]) * aim
        elif line.startswith("up"):
            aim -= int(line[-1])
        else:
            aim += int(line[-1])
    return horizontal * vertical


def jamie():
    # return multiplied_final_position(actual_data)
    return multiplied_final_position_with_aim(actual_data)
