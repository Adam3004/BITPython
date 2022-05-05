def check(word):
    return word == word[::-1]


def get_palindromes(words):
    # return [elem for elem in words if check(elem)]
    return list(filter(check, words))


if __name__ == '__main__':
    words = ['ez', 'esssa', 'lol', 'samolot', 'abzzba']
    print(get_palindromes(words))
