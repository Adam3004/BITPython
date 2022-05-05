def frange(start: float, stop: float, step: float):
    while start < stop:
        yield start
        start += step
    return 'out of range'


if __name__ == '__main__':
    f = frange(1.5, 3.1, 0.5)
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
