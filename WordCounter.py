def read_text_file(path):
    """
    :param path: text file path
    :return: read text file
    """
    f = open(path, "r")
    return f.read()


def word_count(string):
    """
    :param string: text file or input text's
    :return: word counts [dict]
    """

    counts = dict()
    words = string.split()

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
            string = input("Words: ")
            counts = word_count(string)
            print("counts: ", counts)
        except KeyboardInterrupt:
            break  # breaking the loop
