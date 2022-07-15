from threading import Thread
import socket
import subprocess


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
        self.IP = input("   [*]What ip do you want to listen on? ")
        self.PortNumber = int(input("   [*]What port do you to listen on? "))

        self.sock.bind((self.IP, self.PortNumber))
        print("   [*]Socket has been bound successfully")
        NumOfPeopleToJoin = int(input("   [*]How many people would you like to join? "))

        self.sock.listen(NumOfPeopleToJoin)
        print("   [*]Socket has been initiated, look for incoming connection...\n")
        sock_handler, _ = self.sock.accept()



