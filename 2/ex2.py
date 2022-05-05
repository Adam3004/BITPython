import math

a, b, c = tuple(map(float, input().split()))


def pole(a: float, b: float, c: float):
    s = (a + b + c) / 2
    return round(math.sqrt(s * (s - a) * (s - b) * (s - c)), 3)


if __name__ == "__main__":
    print(pole(a, b, c))
