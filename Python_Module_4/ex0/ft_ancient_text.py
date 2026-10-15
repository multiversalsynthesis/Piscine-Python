#!/usr/bin/env python3
"""
Exercise 0: Ancient Text Recovery
Data Archivist Project
"""

import sys
from typing import IO


def main() -> None:
    print("=== Cyber Archives Recovery ===")

    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    filename: str = sys.argv[1]
    print(f"Accessing file '{filename}'")

    file_obj: IO[str] | None = None
    try:
        file_obj = open(filename, 'r')
        content: str = file_obj.read()
        print("---")
        print()
        print(content.rstrip('\n'))
        print()
        print("---")
    except Exception as e:
        print(f"Error opening file '{filename}': {e}")
    finally:
        if file_obj is not None:
            file_obj.close()
            print(f"File '{filename}' closed.")


if __name__ == "__main__":
    main()
