import os
if os.name != "posix" or os.getuid():
    print("[!]Your system does not meet the standard requirements for this tool to run.\n[*]Try to to run this on unix based system with sudo.")
    exit(1)
from src import AndroidControlTool, MlwareAndNetcat, NetworkingStuff

logo = """_________          _______    _______  _______  _______  _______  _______  _______  _______           _______  _______ 
\__   __/|\     /|(  ____ \  (  ____ )(  ____ \(  ____ \(  ____ \(  ___  )(  ____ )(  ____ \|\     /|(  ____ \(  ____ )
   ) (   | )   ( || (    \/  | (    )|| (    \/| (    \/| (    \/| (   ) || (    )|| (    \/| )   ( || (    \/| (    )|
   | |   | (___) || (__      | (____)|| (__    | (_____ | (__    | (___) || (____)|| |      | (___) || (__    | (____)|
   | |   |  ___  ||  __)     |     __)|  __)   (_____  )|  __)   |  ___  ||     __)| |      |  ___  ||  __)   |     __)
   | |   | (   ) || (        | (\ (   | (            ) || (      | (   ) || (\ (   | |      | (   ) || (      | (\ (   
   | |   | )   ( || (____/\  | ) \ \__| (____/\/\____) || (____/\| )   ( || ) \ \__| (____/\| )   ( || (____/\| ) \ \__
   )_(   |/     \|(_______/  |/   \__/(_______/\_______)(_______/|/     \||/   \__/(_______/|/     \|(_______/|/   \__/
                                                                                                                       
   made by Omer Lachover          v0.1(beta)                                                                                                                    
                                                                                                                       """

menu = """
\n   1.ddos\t\t2.Android(adb)
   3.packet sniffing    4.port scanner
   5.MITHM\t\t6.netcat
   7.proxy server\t8.change MAC address
   9.dos\t\t10.virus integrated through github
   
   99.Exit
   
   [*]Enter the number of one of the following options: """


class MainFunctions:
    def __init__(self):
        option = int(input(logo + menu))

        if option == 1:
            mode = input("\n\n   [*]server or client: ")
            if mode == "server":
                NetworkingStuff.Ddos().StartServer()
            elif mode == "client":
                NetworkingStuff.Ddos().ClientMode()
        elif option == 9:
            NetworkingStuff.Ddos().dos()


if __name__ == "__main__":
    Main = MainFunctions()
