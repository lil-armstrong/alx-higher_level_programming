#!/usr/bin/python3

def text_indentation(text):
    """Print a text with 2 new lines\
    after each of these characters: (., ? and :).

    Args:
    text: text string
    """
    if (not isinstance(text, (str))):
        raise TypeError("text must be a string")

    flag = 0
    for char in text:
        if (char in ('.', '?', ':')):
            print("{}\n\n".format(char))
            flag = 1
        else:
            if (char == " " and flag):
                continue
            print(char, end="")
            flag = 0
