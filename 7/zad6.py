import functools


def assert_nonnegative_ints(fun):
    @functools.wraps(fun)
    def wrapper(listaList, *args, **kwargs):
        for row in listaList:
            for elem in row:
                assert isinstance(elem, int) and elem >= 0

        return fun(listaList, *args, **kwargs)

    return wrapper


@assert_nonnegative_ints
def printer(listaList):
    print(listaList)


if __name__ == '__main__':
    L = [[1, 23, 4], [0.5, 15, 25], [321, 24, 6]]
    printer(L)
