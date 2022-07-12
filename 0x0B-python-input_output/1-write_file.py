#!/usr/bin/python3
"""a function that writes a string to  a text file"""


def write_file(filename="", text=""):
    """writes a string to a text file and returns
    the number of characters written"""
    with open(filename, encoding="utf-8", mode="w+") as f:
        return f.write(text)
