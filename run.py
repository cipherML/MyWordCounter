# -*- coding: utf-8 -*-
"""
MY WORD COUNTER
"""
# WordCounter.py is the basic word counter where you can simply pass the text file or type paragraph or
# list of statement and *word counter* will read the text and find the total words, dict of words
# and how many word are repeated.

# RUN

from WordCounter import read_text_file, word_count

if __name__ == '__main__':
    print("<<<<< BASIC WORD COUNTER >>>>> \n")

    # if there is a text file
    file_path = "sampleTEXT.txt"

    # read the text file
    file = read_text_file(path=file_path)
    print("Paragraph: \n", file)
    word_counts = word_count(string=file)
    print("Basic_word_counter: ", word_counts)

