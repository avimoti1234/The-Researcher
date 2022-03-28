import os
if os.name != "posix" or os.getuid():
    print("[!]Your system does not meet the standard requirements for this tool to run.\n[*]Try to to run this on unix based system with sudo.")
    exit(-1)
from sys import path
path.append('enter/the/path/to/the/src/folder/here')
from src import AndroidControlTool, MlwareAndNetcat, NetworkingStuff, Menus

class MainFunctions:
    def __init__(self):
        option = int(input(Menus.logo + Menus.menu))

        if option == 1:
            NetworkingStuff.Ddos()
        elif option == 9:
            NetworkingStuff.Dos()
        elif option == 99:
            exit(1)


if __name__ == "__main__":
    Main = MainFunctions()
