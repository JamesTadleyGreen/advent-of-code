from year_2021.day_1.data import test_data, actual_data


def count_increments(data: str) -> int:
    measurements = [int(i) for i in data.split("\n")]
    increments = 0
    prior = float("inf")
    for measurement in measurements:
        if measurement > prior:
            increments += 1
        prior = measurement
    return increments


def count_moving_increments(data: str, window: int = 3) -> int:
    measurements = [int(i) for i in data.split("\n")]
    increments = 0
    prior = float("inf")
    for i in range(len(measurements) - window + 1):
        current = sum(measurements[i : i + window])
        if current > prior:
            increments += 1
        prior = current
    return increments


def jamie():
    # return count_increments(actual_data)
    return count_moving_increments(actual_data, 3)
