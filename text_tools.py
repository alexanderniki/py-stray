"""
Collection of misc tools and helpers wor working with text

    Classes:
        --

    Functions:
        wrap(line: str, width: int) -> str
        truncate(line: str, limit -> int) -> str
        format_line(line: str) -> str

    Misc variables and constants:
        --
"""


import textwrap


def wrap(line: str, width: int) -> str:
    """
    Wraps one line into several ones with width character per each

        Args:
            line (str): Given line
            width (int): Number of characters per each line in the result

        Returns:
            (str): Wrapped line
    """

    result: str = ""

    if width > 0 and len(line) > width:
        result = textwrap.fill(line, width=width, break_long_words=False)
    else:
        result = ""

    return result


def truncate(line: str, limit: int, truncate_char: str="…") -> str:
    """
    Truncates a line

        Args:
            line (str): Given line
            limit (str): Number of characters in the result
            truncate_char (str): What to place instead of the rest of the line. Default: "…"

        Returns:
            (str): Truncated line
    """

    result: str = ""

    if limit > 0 and len(line) > limit:
        result = line[:limit - 1] + truncate_char
    else:
        result = ""

    return result


def format_line(line: str, wrap_width: int, truncate_limit: int) -> str:
    """
    Wrap and truncate the line

        Args:
            line (str): Given line
            wrap_width (int): New line width
            truncate_limit (int): When to truncate the line

        Returns:
            (str): Formatted line
    """

    result: str = ""

    if wrap_width < truncate_limit:
        result = wrap(line, wrap_width)  # Wrap first and then truncate
        result = truncate(result, truncate_limit)
    else:
        if wrap_width >= truncate_limit:  # Ignoring wrap, just truncating
            result = truncate(result, truncate_limit)

    return result
