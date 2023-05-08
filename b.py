#!/usr/bin/env python3

import argparse
from dat import load_data, save_data
from util import call_logger

with open("wap.txt", "rt") as f:
    content = f.read()


def _load_chars():
    try:
        characters = load_data("characters")
    except:
        characters = {}
    return characters


def list_chars():
    characters = _load_chars()
    for k, v in characters.items():
        print(f"{k} appears {v} times")


# @call_logger
def add_char(char):
    # count the instance of char and put them in the character json
    import pdb

    # pdb.set_trace()
    characters = _load_chars()
    print(characters)
    if char not in characters:
        words = content.split()
        count = len([a for a in words if a == char])
        characters[char] = count
        save_data("characters", characters)

    print(characters)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="ProgramName",
        description="What the program does",
        epilog="Text at the bottom of help",
    )

    parser.add_argument("action")
    parser.add_argument("character")

    args = parser.parse_args()

    if args.action == "count":
        add_char(args.character)

    if args.action == "list":
        list_chars()
