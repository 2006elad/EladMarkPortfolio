def sort_string(word):
    word = sorted(word)
    word = "".join(word)
    return word


def sort_anagrams(list_of_strings):
    """
    Function that create list word with the same anigram
    :param list_of_strings: the list of word we want to order
    :return: sorted anigram list of words
    :rtype: list
    """
    list_of_anigram_word = []
    for word in list_of_strings:
        if sort_string(word) not in list_of_anigram_word:
            list_of_anigram_word.append(sort_string(word))
    list_of_sorted_anigram = [[] for i in range(len(list_of_anigram_word))]
    for word in list_of_strings:
        list_of_sorted_anigram[list_of_anigram_word.index(sort_string(word))].append(word)

    return list_of_sorted_anigram


def main():
    list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters',
                     'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']
    print(sort_anagrams(list_of_words))


if __name__ == '__main__':
    main()