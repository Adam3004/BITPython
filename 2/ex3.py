import random

randomInts = list(random.randint(-10, 10) for _ in range(100))


def deduplicate_and_sort(randomInts: list):
    return sorted(set(randomInts))


if __name__ == "__main__":
    print(deduplicate_and_sort(randomInts))
