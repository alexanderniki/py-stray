#!/usr/bin/env python3
import sys
import random
import argparse
import textwrap

from text_tools import *


def main():
    """
    Main
    """
    parser = argparse.ArgumentParser(description="Pick a random line from a text source.")
    parser.add_argument("source", help="Path to the input file")
    parser.add_argument("-w", "--width", type=int, default=0,
                        help="Wrap text to N characters per line")
    parser.add_argument("-t", "--truncate", type=int, default=0,
                        help="Truncate text to N characters (adds '…' if cut)")
    args = parser.parse_args()

    try:
        with open(args.source, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    if not lines:
        print("No quotes found", file=sys.stderr)
        sys.exit(1)

    quote = random.choice(lines)
    original_len = len(quote)

    # 1. Обрезаем, если включён truncate и исходная строка длиннее лимита
    if args.truncate > 0 and original_len > args.truncate:
        quote = quote[:args.truncate - 1] + "…"
        #quote = truncate(quote, args.truncate)

    # 2. Делаем перенос строк, если включён width и он строго меньше truncate
    #    (если width >= truncate, перенос игнорируется по условию)
    if args.width > 0:
        #if args.truncate == 0 or args.width < args.truncate:
        if args.width < args.truncate:
            quote = textwrap.fill(quote, width=args.width, break_long_words=False)
            #quote = wrap(quote, args.width)

    #format_line(quote, args.width, args.truncate)

    print(quote, end="")


if __name__ == "__main__":
    main()
