import os
if os.name != "posix" or os.getuid():
    print("[!]Your system does not meet the standard requirements for this tool to run.\n[*]Try to to run this on unix based system with sudo.")
from scapy.all import ICMP, ARP, IP, UDP, TCP, Ether, RandShort, RandIP
from threading import Thread


