#from CheckLib import installLibs
#installLibs()
from Database import launch
import platform
from pathlib import Path
import os


def main():
    if platform == "Windows":
        home_dir = Path(os.environ.get('APPDATA', Path.home() / 'AppData' / 'Roaming'))
    else:
        home_dir = Path.home()

    app_dir = home_dir / ".PManager"
    app_dir.mkdir(parents=True, exist_ok=True)

    db = app_dir / ".PManager.db"
    launch(str(db))

if __name__ == "__main__":
    main()
