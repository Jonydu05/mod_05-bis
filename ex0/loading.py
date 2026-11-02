import importlib


def check_reagent(name: str) -> tuple[bool, str | None]:
    try:
        module = importlib.import_module(name)
        version = getattr(module, "__version__", "unknown")
        return True, version
    except Exception:
        return False, None


def main() -> None:
    print("REAGENT STATUS: Loading reagents...")
    print("Checking dependencies:")

    reagents: dict[str, str] = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready"
    }

    missing: list[str] = []
    installed_info: list[str] = []

    for name, desc in reagents.items():
        is_present, version = check_reagent(name)
        if is_present:
            installed_info.append(f"[OK] {name} ({version}) - {desc}")
        else:
            missing.append(name)

    for info in installed_info:
        print(info)

    if missing:
        print("\nWARNING: Some reagents are missing!")
        print("To install them using pip:")
        print("  pip install -r ex0/requirements.txt")
        print("To install them using Poetry:")
        print("  poetry install")
    else:
        print("\npip vs Poetry:")
        print(" requirements.txt declares what to install;"
              " pip resolves it at install time.")
        print(" pyproject.toml declares the same constraints,"
              " and Poetry pins the resolved")
        print(" versions in poetry.lock so every install is identical.")
        print("\nAll reagents present and accounted for.")


if __name__ == "__main__":
    main()
