from typing import *


def changer(list_of_lists: list[list]) -> Set(FrozenSet):
    newSet = set()
    for lista in list_of_lists:
        tempSet = frozenset(lista)
        newSet.add(tempSet)
    return newSet


if __name__ == '__main__':
    lista = [[1, 2], [2, 3], [4, 6]]
    print(changer(lista))
