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
            print("[!] The following input is invalid mode.\nplease choose valid mode(server/client).")

    def ServerMode(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)





