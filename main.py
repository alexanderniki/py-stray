#!/usr/bin/env python3
import sys
import random


def main():
    """
    Main
    """
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file_path>", file=sys.stderr)
        sys.exit(1)

    filepath = sys.argv[1]

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            # Read all lines, strip whitespace, and filter out empty lines
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"File not found: {filepath}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Read error: {e}", file=sys.stderr)
        sys.exit(1)

    if not lines:
        print("File is empty or contains no valid lines", file=sys.stderr)
        sys.exit(1)

    # Print a single random line WITHOUT appending a trailing newline
    print(random.choice(lines), end="")

if __name__ == "__main__":
    main()
