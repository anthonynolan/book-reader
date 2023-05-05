#!/usr/bin/env python3

import argparse

with open("wap.txt", "rt") as f:
    content = f.read()


def add_char(char):
    # count the instance of char and put them in the character json
    words = content.split()
    count = len([a for a in words if a == char])
    print(count, char)


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
