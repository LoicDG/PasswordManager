import importlib
import subprocess
from time import sleep
from os import system


def check_dependency(library_name):
    try:
        importlib.import_module(library_name)
        return True
    except ImportError:
        return False


def installLibs():
    # List of libraries to check
    libraries_to_check = ["cryptography", "pyperclip", "maskpass", "passlib", "argon2-cffi"]

    missing_libraries = [lib for lib in libraries_to_check if not check_dependency(lib)]

    if missing_libraries:
        print(f"The following libraries are missing: {', '.join(missing_libraries)}")
        print("Installing missing libraries...")

        for library in missing_libraries:
            if library == "argon2-cffi":
                subprocess.run(["pip", "install", library, "--ignore-installed"])
            else:
                subprocess.run(["pip", "install", library])

        print("Libraries installed.")
        sleep(2)
        system("cls")
    else:
        pass