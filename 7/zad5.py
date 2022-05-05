import functools


def print_hello(fun):
    @functools.wraps(fun)
    def wrapper(*args, **kwargs):
        print('hello')
        return fun(*args, **kwargs)

    return wrapper


def do_twice(fun):
    @functools.wraps(fun)
    def wrapper(*args, **kwargs):
        fun(*args, **kwargs)
        return fun(*args, **kwargs)

    return wrapper


@do_twice
@print_hello
def print_a():
    print('a')


if __name__ == '__main__':
    print_a()
