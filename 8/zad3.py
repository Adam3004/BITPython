from itertools import chain
from typing import *


def changer(list_of_lists: list[list]) -> Set:
    return set(chain.from_iterable(list_of_lists))


if __name__ == '__main__':
    lista = [[1, 2], [2, 3], [4, 6]]
    print(changer(lista))
