#!/usr/bin/env python3
import sys
import random
import argparse
import textwrap

def main():
    """
    Main
    """
    parser = argparse.ArgumentParser(description="Pick a random line from a file.")
    parser.add_argument("file", help="Path to the text file")
    parser.add_argument("-w", "--width", type=int, default=0,
                        help="Wrap text to N characters per line")
    args = parser.parse_args()

    try:
        with open(args.file, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    if not lines:
        print("No quotes found", file=sys.stderr)
        sys.exit(1)

    quote = random.choice(lines)

    if args.width > 0:
        # wrap: split strings by spaces and place them on the next line
        quote = textwrap.fill(quote, width=args.width)

    print(quote, end="")


if __name__ == "__main__":
    main()
