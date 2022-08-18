def translate(sentence):
    """
    Function that translate sentence with the word dict
    :param sentence: Sentence we want to translate we using generator
    :type: str
    :return: translated sentence
    :rtype: str
    """
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    sentence_list = sentence.split()
    new_sentence = (words[word_to_translate] for word_to_translate in sentence_list)
    print(type(new_sentence))
    return " ".join(new_sentence)


def main():
    print(translate("el gato esta en la casa"))


if __name__ == '__main__':
    main()
