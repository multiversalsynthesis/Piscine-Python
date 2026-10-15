#!/usr/bin/env python3
"""
Exercise 1: Archive Creation
Data Archivist Project
"""

import sys
from typing import IO


def main() -> None:
    print("=== Cyber Archives Recovery & Preservation ===")

    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
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
        print(f"Error opening file '{filename}': {e}")
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

    # Ask for the destination file (EOF is treated as an empty answer)
    new_filename: str = ""
    try:
        new_filename = input("Enter new file name (or empty): ").strip()
    except EOFError:
        print()

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
        print(f"Error opening file '{new_filename}': {e}")
        print("Data not saved.")
    finally:
        if save_obj is not None:
            save_obj.close()


if __name__ == "__main__":
    main()
