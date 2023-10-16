from CheckLib import installLibs
installLibs()
from Database import launch
import argparse


def main():
    parser = argparse.ArgumentParser(description= "Password Manager Application")
    parser.add_argument("database", help= "path to the database file")
    args = parser.parse_args()
    launch(args.database)


if __name__ == "__main__":
    main()
