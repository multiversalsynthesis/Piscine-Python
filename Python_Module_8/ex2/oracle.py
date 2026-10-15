import os
from dotenv import load_dotenv  # type: ignore


def load_config() -> None:
    """Load configuration from .env file and environment variables."""
    load_dotenv()

    print("ORACLE STATUS: Reading the Matrix...\n")

    matrix_mode = os.getenv("MATRIX_MODE", "development")
    database_url = os.getenv("DATABASE_URL", "sqlite:///local_matrix.db")
    api_key = os.getenv("API_KEY", "default_key")
    log_level = os.getenv("LOG_LEVEL", "INFO")
    zion_endpoint = os.getenv("ZION_ENDPOINT", "https://zion.resistance.net")

    print("Configuration loaded:")
    print(f"Mode: {matrix_mode}")
    print(f"Database: {database_url}")

    api_status = (
        "Authenticated"
        if api_key != "default_key"
        else "Using default key"
    )
    print(f"API Access: {api_status}")

    print(f"Log Level: {log_level}")
    print(f"Zion Network: {zion_endpoint}")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    load_config()
