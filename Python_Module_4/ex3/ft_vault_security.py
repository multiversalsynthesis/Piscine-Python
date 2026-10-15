#!/usr/bin/env python3
"""
Exercise 3: Vault Security
Data Archivist Project
"""


def secure_archive(
    filename: str, action: str = "read", content: str = ""
) -> tuple[bool, str]:
    """
    Safe file operation using the 'with' statement.
    action: "read" or "write"
    """
    try:
        if action == "read":
            with open(filename, 'r') as f:
                return True, f.read()
        elif action == "write":
            with open(filename, 'w') as f:
                f.write(content)
            return True, "Content successfully written to file"
        else:
            return False, f"Unknown action: {action}"
    except Exception as e:
        return False, str(e)


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))

    # Prepare a regular file to read
    fragment_file: str = "ancient_fragment.txt"
    fragments: str = (
        "[FRAGMENT 001] Digital preservation protocols established 2087\n"
        "[FRAGMENT 002] Knowledge must survive the entropy wars\n"
        "[FRAGMENT 003] Every byte saved is a victory against oblivion\n"
    )
    secure_archive(fragment_file, "write", fragments)

    print("\nUsing 'secure_archive' to read from a regular file:")
    result: tuple[bool, str] = secure_archive(fragment_file)
    print(result)

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_archive.txt", "write", result[1]))


if __name__ == "__main__":
    main()
