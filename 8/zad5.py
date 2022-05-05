from collections import Counter
import string

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize


def create_bag_of_words(text):
    # partition into sentences and words
    sentences = sent_tokenize(text)
    words = []
    for sentence in sentences:
        sentence_words = word_tokenize(sentence)
        words.extend(sentence_words)

    # change to lowercase
    words_1 = (word.lower() for word in words)

    # remove stop words
    stop_words = set(stopwords.words("english"))
    words_2 = (word for word in words_1 if word not in stop_words)

    # remove punctuation
    punctuation = set(string.punctuation)
    punctuation.add("...")
    words_3 = (word for word in words_2 if word not in punctuation)

    # change words to their stems
    stemmer = PorterStemmer()
    words_4 = (stemmer.stem(word) for word in words_3)

    # remove too short stems
    words_5 = (word for word in words_4 if len(word) >= 3)

    # count words
    bag_of_words = Counter(words_5)

    return bag_of_words



