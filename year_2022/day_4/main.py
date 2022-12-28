from year_2022.day_4.data import test_data, actual_data

#! This day I struggled with, unsure why. The equality tests below are GROSS.


def count_of_containing_pairs(data: str) -> int:
    lines = data.split("\n")
    count = 0
    for line in lines:
        fst, snd = line.split(",")
        l1, h1 = [int(i) for i in fst.split("-")]
        l2, h2 = [int(i) for i in snd.split("-")]
        if (l1 >= l2 and h1 <= h2) or (l1 <= l2 and h1 >= h2):
            count += 1
    return count


def count_of_seperate_pairs(data: str) -> int:
    lines = data.split("\n")
    count = 0
    for line in lines:
        fst, snd = line.split(",")
        l1, h1 = [int(i) for i in fst.split("-")]
        l2, h2 = [int(i) for i in snd.split("-")]
        if (l2 <= h1 <= h2) or (l2 <= l1 <= h2) or (l1 <= l2 <= h1) or (l1 <= h2 <= h1):
            count += 1
    return count


def jamie():
    # return count_of_containing_pairs(actual_data)
    return count_of_seperate_pairs(actual_data)
