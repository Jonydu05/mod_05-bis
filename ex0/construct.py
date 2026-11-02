import sys
import os
import site


def no_venv_detected() -> None:
    print("LABORATORY STATUS: You are working in the open\n")

    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected\n")

    print("WARNING: You are in the global environment!")
    print("Every reagent you install here leaks into the whole system.\n")

    print("To seal the laboratory, run:")
    print("python3 -m venv lab_env")
    print("source lab_env/bin/activate # On Unix")
    print("lab_env\\Scripts\\activate # On Windows\n")

    print("The run this program again.")


def venv_detected() -> None:
    name_venv = os.path.basename(sys.prefix)
    print(sys.prefix)
    print(name_venv)
    print("LABORATORY STATUS: The laboratory is sealed\n")

    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {name_venv}")
    print(f"Environment Path: {sys.prefix}\n")

    print("SUCCESS: You are working in an isolated environment!")
    print("Safe to install reagents without affecting the global system.\n")

    print("Reagent installation path: ")
    print(site.getsitepackages()[0])


if __name__ == "__main__":
    if (sys.prefix != sys.base_prefix) or ('VIRTUAL_ENV' in os.environ):
        venv_detected()
    else:
        no_venv_detected()
