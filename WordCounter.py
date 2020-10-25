# -*- coding: utf-8 -*-
"""
Created on Mon Mar 6 2020

"""


# function to read text file
def read_text_file(path):
    """
    :param path: text file path
    :return: read text file
    """
    f = open(path, "r")
    return f.read()


# Word counter
def word_count(string):
    """
    :param string: text file or input text's
    :return: word counts [dict]
    """

    counts = dict()
    words = string.lower().split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    print('The Total words in the given statements are: ', len(words))

    return counts


def input_texts_count():
    while True:
        try:
            string = input("\nWords: ")
            counts = word_count(string)
            print("counts: ", counts)
        except KeyboardInterrupt:
            break  # breaking the loop
