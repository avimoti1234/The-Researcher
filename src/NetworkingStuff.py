from scapy.all import ICMP, ARP, IP, UDP, TCP, Ether, RandShort, RandIP, send
from threading import Thread
import socket

class PortScanner:
    def __init__(self):
        pass

class Ddos:
    def __init__(self):
        mode = input("\n   [*]choose mode(server or client): ")
        if mode == "server":
           self._ServerMode()
        elif mode == "client":
            #self.ClientMode()
            pass
     
    def _ServerMode(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Ip = input("\n   [*]ip to be bound: ")

        Port = int(input("\n   [*]port to listen on: "))

        self.sock.bind((Ip, Port))

        NumOfPeople = int(input("\n   [*]max number of members to join: "))

        self.sock.listen(NumOfPeople)

        self.sock.close()


