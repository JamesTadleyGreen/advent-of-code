from functools import partial

from typing import Any, List, Optional, Tuple
from year_2022.day_7.data import test_data, actual_data


class Tree:
    def __init__(
        self,
        name: str,
        size: int,
        parent: Optional[Any] = None,
        children: Optional[List[Any]] = None,
    ):
        self.name = name
        self.size = size
        self.parent = parent
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)

    def __str__(self, level=0):
        ret = "\t" * level + self.__repr__(level) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def __repr__(self, level):
        if self.children == []:
            return f"<{self.name}:{self.size}:{level}>"
        else:
            return f"[{self.name}:{self.size}:{level}]"

    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)

    def get_children(self):
        return self.children


def directory_structure(commands: List[str]) -> Tree:
    root = Tree("/", 0)
    dir = root
    for command in commands[1:]:
        action, name = command.split(" ", 1)
        if action == "$":
            if name == "ls":
                pass
            else:
                _, new_dir = name.split(" ")
                if new_dir == "..":
                    dir = dir.parent
                else:
                    dir = [child for child in dir.children if child.name == new_dir][0]
        elif action == "dir":
            dir.add_child(Tree(name, 0, dir))
        else:
            dir.add_child(Tree(name, int(action), dir))
    return root


def propagate_sizes(node: Tree, max_size: int | float) -> Tree:
    if node.children != []:
        if (size := tree_fold(sum, node)) < max_size:
            node.size = size
        for b in node.children:
            propagate_sizes(b, max_size)
    return node


def size_of_node(node: Tree, size: int = 0) -> int:
    # print(node.name, node.size, size)
    if node.children == []:
        return node.size
    for b in node.children:
        size += size_of_node(b, size)
        print(node.name, size, b.name)
    return size


def tree_fold(func: Any, tree: Tree) -> int:
    if tree.children == []:
        return tree.size
    reduced_children = [tree_fold(func, child) for child in tree.children]
    return func(reduced_children)


def sum_folders(node: Tree, size: int = 0, level: int = 0) -> int:
    if node.children == []:
        return 0
    else:
        size = node.size
    for b in node.children:
        size += sum_folders(b, size, level + 1)
    return size


def total_size_under_max(data: str, max_size: int) -> int:
    commands = data.split("\n")
    directory = directory_structure(commands)
    directory = propagate_sizes(directory, max_size)
    return sum_folders(directory)


def min_size_folder(node: Tree, min_size: int, folder_size: int | float) -> int:
    if node.children != []:
        print(type(min_size), type(node.size), folder_size, min_size <= node.size)
        if min_size <= node.size <= folder_size:
            print(node.size)
            folder_size = node.size
    for b in node.children:
        folder_size = min_size_folder(b, min_size, folder_size)
    return folder_size


def smaller_directory(limit: int, l: List[int]) -> int | float:
    print(l)
    smallest = float("inf")
    if len(l) == 1:
        return smallest
    for i in l:
        print(i, smallest)
        if (i < smallest) and (i > limit):
            smallest = i
    return smallest


def smallest_directory_over_size(data: str, min_size: int) -> int:
    commands = data.split("\n")
    directory = directory_structure(commands)
    directory = propagate_sizes(directory, float("inf"))
    required_space = directory.size - 40_000_000
    print(required_space)
    print(directory)
    smallest_directory = tree_fold(
        partial(smaller_directory, required_space), directory
    )
    print(smallest_directory)
    # return min_size_folder(directory, min_size, float("inf"))


def jamie() -> int:
    # return total_size_under_max(actual_data, 100_000)
    return smallest_directory_over_size(test_data, 30_000_000)
