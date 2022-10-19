#!/usr/bin/python3

"""module for text_indentation method."""


def text_indentation(text):
    """
    Method for adding 2 new lines after '.?:' chars.
    Args:
        text: The str text.
    Raises:
        TypeError: If text is not a str.
    """

    if type(text) != str:
        raise TypeError("text must be a string")

    for delim in ".?:":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end="")
