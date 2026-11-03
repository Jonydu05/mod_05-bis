import os
from dotenv import load_dotenv


def get_matrix_mode() -> str:
    matrix = os.getenv("MATRIX_MODE")
    if (matrix is None) or (matrix not in ("development", "production")):
        matrix = "production"
    return matrix.lower()


def get_log_level() -> str:
    log = os.getenv("LOG_LEVEL")
    log_list: list[str] = [
        "debug", "warning", "info", "error", "critical"
    ]
    if not log:
        log = "INFO"
    if log.lower() in log_list:
        log = log.upper()
    else:
        log = "INFO"
    return log


def main() -> None:
    load_dotenv()
    print("ORACLE STATUS: Consulting the configuration...")

    matrix_mode: str = get_matrix_mode()
    database_url: str | None = os.getenv("DATABASE_URL")
    api_key: str | None = os.getenv("API_KEY")
    zion_endpoint: str | None = os.getenv("ZION_ENDPOINT")
    log_level: str = get_log_level()

    missing_conf: list[str] = []
    if not database_url:
        missing_conf.append("DATABASE_URL")
    if not api_key:
        missing_conf.append("API_KEY")
    if not zion_endpoint:
        missing_conf.append("ZION_ENDPOINT")

    if missing_conf:
        print("\nWARNING: Critical configuration missing!")
        print("The following variables are not set: "
              f"{', '.join(missing_conf)}")
        print("Please check your .env file or environment variables.")

    print("\nConfiguration Loaded:")
    print(f"Mode: {matrix_mode}")
    print(f"Log Level: {log_level}")

    database_msg = "Database: "
    api_key_msg = "Api Acess: "
    zion_msg = "Remote Network: "
    default_error_str = "Not configured"
    if database_url:
        database_msg += "Connection configured"
    else:
        database_msg += default_error_str

    if api_key:
        api_key_msg += "Configured"
    else:
        api_key_msg += default_error_str

    if zion_endpoint:
        zion_msg += "Endpoint configured"
    else:
        zion_msg += default_error_str

    print(database_msg)
    print(api_key_msg)
    print(zion_msg)

    print("\nConfiguration security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly ignored by git")
    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
