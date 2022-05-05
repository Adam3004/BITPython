import random


def rand_dict(n: int):
    generatedDict = {random.randint(0, 20): random.randint(0, 20) for _ in range(n)}
    if n > 21:
        n = 21
    while len(generatedDict) < n:
        key = random.randint(0, 20)
        generatedDict[key] = random.randint(0, 20)

    return generatedDict


def reverse_dict(dictionary: dict):
    newDict = {value: key for key, value in dictionary.items()}

    return newDict


if __name__ == '__main__':
    n = 50
    dictionary = rand_dict(n)
    print(dictionary)
    print(reverse_dict(dictionary))
