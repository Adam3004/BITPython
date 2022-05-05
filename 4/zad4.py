import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer
from collections import Counter

# stopwords initialization
# nltk.download('stopwords')
english_stopwords = stopwords.words("english")

# steemer initialization
steemer = PorterStemmer()

# nltk.download("punkt")


# def get_bag_of_words2(text: str):
#     lines = tuple(text.split('.'))
#     words_in_sentences = [sentence.split() for sentence in lines]
#     words = [words_in_sentences[i][j] for i in range(len(words_in_sentences)) for j in
#              range(len(words_in_sentences[i]))]
#     words = [word.lower() for word in words]
#     words = [word for word in words if word not in english_stopwords]
#     for sign in string.punctuation:
#         words = [word.replace(sign, '') for word in words]
#     sign = '...'
#     words = [word.replace(sign, '') for word in words]
#     words = [steemer.stem(word) for word in words]
#     words = [word for word in words if len(word) >= 3]
#     counted_words = Counter(words)
#     return counted_words

def get_bag_of_words(text: str):
    words = word_tokenize(text)
    words = [word.lower() for word in words]
    words = [word for word in words if word not in english_stopwords]
    for sign in string.punctuation:
        words = [word.replace(sign, '') for word in words]
    sign = '...'
    words = [word.replace(sign, '') for word in words]
    words = [steemer.stem(word) for word in words]
    words = [word for word in words if len(word) >= 3]
    counted_words = Counter(words)
    return counted_words


if __name__ == "__main__":
    with open('SPOILER_lorem.txt', 'r') as f:
        tekst = ''
        for i in f.readlines():
            tekst += i.rstrip()
    bag_of_words = get_bag_of_words(tekst)
    # bag_of_words2 = get_bag_of_words2(tekst)

    print(bag_of_words)
    # print(bag_of_words2)
