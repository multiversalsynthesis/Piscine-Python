#!/usr/bin/env python3
"""
Exercise 2: Stream Management
Data Archivist Project
"""

import sys
from typing import IO


def main() -> None:
    print("=== Cyber Archives Recovery & Preservation ===")

    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>", file=sys.stderr)
        return

    filename: str = sys.argv[1]
    print(f"Accessing file '{filename}'")

    file_obj: IO[str] | None = None
    content: str = ""
    try:
        file_obj = open(filename, 'r')
        content = file_obj.read()
        print("---")
        print()
        print(content.rstrip('\n'))
        print()
        print("---")
    except Exception as e:
        print(
            f"[STDERR] Error opening file '{filename}': {e}",
            file=sys.stderr
        )
        return
    finally:
        if file_obj is not None:
            file_obj.close()
            print(f"File '{filename}' closed.")

    # Add the archive character (#) at the end of each line
    lines: list[str] = content.splitlines()
    transformed: list[str] = [line + '#' for line in lines]
    print("\nTransform data:")
    print("---")
    print()
    print('\n'.join(transformed))
    print()
    print("---")

    # Read the answer from stdin without input()
    print("Enter new file name (or empty): ", end='', file=sys.stdout)
    sys.stdout.flush()
    raw: str = sys.stdin.readline()
    if raw == "":
        print()
    new_filename: str = raw.strip()

    if not new_filename:
        print("Not saving data.")
        return

    print(f"Saving data to '{new_filename}'")
    output: str = ''.join(line + '\n' for line in transformed)
    save_obj: IO[str] | None = None
    try:
        save_obj = open(new_filename, 'w')
        save_obj.write(output)
        save_obj.close()
        print(f"Data saved in file '{new_filename}'.")
    except Exception as e:
        print(
            f"[STDERR] Error opening file '{new_filename}': {e}",
            file=sys.stderr
        )
        print("Data not saved.")
    finally:
        if save_obj is not None:
            save_obj.close()


if __name__ == "__main__":
    main()
