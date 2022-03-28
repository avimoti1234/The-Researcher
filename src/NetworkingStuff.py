from scapy.all import ICMP, ARP, IP, UDP, TCP, Ether, RandShort, RandIP, send
from threading import Thread
import socket
import Menus


def DisplayHelpMenu():
    print(Menus.HelpMenu)


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

    def AttackTarget(self):
        print("in attack function")
        while self.Attack:
            send()

    def _JoinParty(self):
        self.members = []
        self.sock.setblocking(False)
        while True:
            if self.Join:
                try:
                    self.members.append(self.sock.accept()[0])
                except Exception:
                    pass
            else:
                pass


