from typing import List, Tuple
from year_2022.day_8.data import test_data, actual_data


def number_of_visible_trees(data: str) -> int:
    trees = [[int(j) for j in i] for i in data.split("\n")]
    width = len(trees[0])
    height = len(trees)
    num_visible = 0
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            num_visible += tree_visible(i, j, trees)
    return num_visible + 2 * (width + height - 2)


def tree_visible(i: int, j: int, trees: List[List[int]]) -> bool:
    if trees[i][j] > max(trees[i][:j]):
        return True
    if trees[i][j] > max([t[j] for t in trees[i + 1 :]]):
        return True
    if trees[i][j] > max(trees[i][j + 1 :]):
        return True
    if trees[i][j] > max([t[j] for t in trees[:i]]):
        return True
    return False


def max_scenic_view(data: str) -> int:
    trees = [[int(j) for j in i] for i in data.split("\n")]
    width = len(trees[0])
    height = len(trees)
    scenic_view_max = 0
    for i in range(height):
        for j in range(width):
            if (view := scenic_view(i, j, trees)) > scenic_view_max:
                scenic_view_max = view

    return scenic_view_max


def scenic_view(i: int, j: int, trees: List[List[int]]) -> int:
    tree_value = trees[i][j]
    scenic_view_total = 1
    for tree_view in [
        trees[i][:j][::-1],
        [t[j] for t in trees[i + 1 :]],
        trees[i][j + 1 :],
        [t[j] for t in trees[:i]][::-1],
    ]:

        seen = trees_seen(tree_value, tree_view)
        scenic_view_total *= seen
    return scenic_view_total


def trees_seen(tree_value: int, tree_view: List[int]) -> int:
    trees = 0
    for tree in tree_view:
        if tree_value > tree:
            trees += 1
        else:
            trees += 1
            return trees
    return trees


def jamie():
    # return number_of_visible_trees(actual_data)
    return max_scenic_view(actual_data)
