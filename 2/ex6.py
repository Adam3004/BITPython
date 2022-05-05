from operator import itemgetter


def print_k_most_repeating(listOfWords: list, k: int):
    print("Most popular words: ")
    for i in range(k):
        print(f''''{listOfWords[i][0]}' repeated {listOfWords[i][1]} times''')


if __name__ == "__main__":
    words = input().split()
    for i in range(len(words)):
        words[i] = words[i].lower()
    # wordsSet = set(words)
    # wordsRepeating = {word: 0 for word in wordsSet}
    wordsRepeating = {}
    for word in words:
        wordsRepeating[word] = wordsRepeating.get(word, 0) + 1
    wordsRepeatingList = []
    for key, value in wordsRepeating.items():
        wordsRepeatingList.append((key, value))
    wordsRepeatingList.sort(reverse=True, key=itemgetter(1))
    print_k_most_repeating(wordsRepeatingList, 5)
