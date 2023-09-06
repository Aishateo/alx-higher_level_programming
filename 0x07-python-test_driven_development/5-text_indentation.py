#!/usr/bin/python3
"""Defines a text-indentation function."""

def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    _x = 0
    while _x < len(text) and text[_x] == ' ':
        _x += 1

    while _x < len(text):
        print(text[_x], end="")
        if text[_x] == "\n" or text[_x] in ".?:":
            if text[c] in ".?:":
                print("\n")
            _x += 1
            while _x < len(text) and text[_x] == ' ':
                _x += 1
            continue
        _x += 1
