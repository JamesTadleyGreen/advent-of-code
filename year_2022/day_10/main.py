from year_2022.day_10.data import test_data, actual_data


def check_collision(cycle: int, register: int) -> bool:
    return abs(register - (cycle % 40)) <= 1


def capital_letters(data: str) -> str:
    operations = data.split("\n")
    output = []
    cycle = 1
    s = ""
    register = 1
    for operation in operations:
        cycles = 1
        if operation != "noop":
            _, amount = operation.split(" ")
            amount = int(amount)
            cycles = 2
        for c in range(cycles):
            if check_collision(cycle - 1, register):
                char = "#"
            else:
                char = "."
            s += char
            if not (cycle % 40):
                output.append(s)
                s = ""
            if c == 1:
                register += amount
            cycle += 1
    return output


def jamie():
    return capital_letters(actual_data)
