import sys
from .hruid import Generator


def main():
    print("Welcome to the HRUID library - you are in command line mode.")
    print("Available commands: generate\n")

    if len(sys.argv) == 2:
        cmd = sys.argv[1]
        if cmd == "generate":
            print(Generator().random())

    else:
        print("Incorrect usage of CLI mode.")
