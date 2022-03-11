from scapy.all import ICMP, ARP, IP, UDP, TCP, Ether, RandShort, RandIP, send
from threading import Thread
import socket

def DisplayHelpMenu():
    HelpMenu = \
    """
    researcher [option] [parameter]
    options:
    
    
    -p --protocol\tspecify protocol to use
    -f --flags   \tspecify flags in the packet header of the protocol you chose
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
        while Input != "exit":
            Input = input("   host@command>")
            if Input == "start attack":
                self.Attack = True
                self.AttackTarget()
            elif Input == "stop attack":
                self.Attack = False
            elif Input == "stop join":
                self.Join = False
            elif Input == "-h" or Input == "--help":
                DisplayHelpMenu()
            else:
                for i in range(len(self.members)):
                    self.members[i].send(Input.encode())
        self.Join = False
        print(122)


    def AttackTarget(self):
        while self.Attack:
            send()

    def _JoinParty(self):
        print("hi")
        self.members = []
        while self.Join:
            print("hi1")
            #client, addr = self.sock.accept()
            self.members.append(self.sock.accept()[0])
            print("hi2")
            print(self.Join)


