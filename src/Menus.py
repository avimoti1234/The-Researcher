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
HelpMenu = \
    """
researcher [option] [parameter]
options:


-protocol                                 \tspecify protocol to use
-flag                                     \tspecify flags in the packet header of the protocol you chose
    FIN, SYN, RST, PSH, ACK, URG, ECE, CWR\tpossible arguments for the -flag option
-port                                     \tspecify port number for the attack
    1. -port/(nothing)                    \tif -port set to nothing the port will be set to default
    2. -port random                       \tif -port set to random the attack will use random port to attack
"""