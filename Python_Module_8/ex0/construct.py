import sys
import os


def main() -> None:
    print("MATRIX STATUS: Entering the Construct...\n")

    # Detectar si estamos en un virtual environment
    in_venv = sys.prefix != sys.base_prefix

    if in_venv:
        venv_name = os.path.basename(sys.prefix)
        print("MATRIX STATUS: Welcome to the construct")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {sys.prefix}")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")

        # Package installation path
        py_version = f"{sys.version_info.major}.{sys.version_info.minor}"
        site_path = f"{sys.prefix}/lib/python{py_version}/site-packages"
        print(f"Package installation path: {site_path}")

    else:
        print("MATRIX STATUS: You're still plugged in")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")

        print("To enter the construct, run:")
        print("    python -m venv matrix_env")
        print("    source matrix_env/bin/activate          # On Unix")
        print("    matrix_env\\Scripts\\activate            # On Windows")
        print("Then run this program again.")


if __name__ == "__main__":
    main()
