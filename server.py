import socket
import threading
from time import time, ctime
from rich.console import Console
import logging
from rich.logging import RichHandler
from settings import DISCONNECT_MESSAGE, HEADER, SERVER, ADDR, FORMAT, RICHFORMAT

class ServerMaster:

    def __init__(self):
        self.users = dict()
        self.console = Console()
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(ADDR)
        logging.basicConfig(
            level="NOTSET", format=RICHFORMAT, datefmt="[%X]", handlers=[RichHandler()]
        )
        self.log = logging.getLogger("rich")
        self.chats = {}

    def disconnect():
        conn.close()

    def handle_client(self, conn, addr, users = {}):
        print(f"[NEW CONNECTION] {addr} connected.")

        connected = True
        while connected:
            msg_length = conn.recv(HEADER).decode(FORMAT)
            t = time()
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)
                if msg == DISCONNECT_MESSAGE:
                    connected = False
                if 'Joined!' in msg:
                    self.users[addr] = msg.split(',')[0]
                    self.console.print(f"Username: {msg.split(',')[0]}", style='green bold')
                self.chats[self.users[addr]] = msg
                with open("chat_history.txt", "a") as file:
                    file.write(f"{self.users[addr]} - {msg} - {ctime(t)}\n")
                self.log.info(f"User: {self.users[addr]} - {msg}")
                self.console.print(f"{self.users[addr]}: {msg}", style='bold red')
                conn.send("Sent".encode(FORMAT))
        conn.close()

    def start(self):
        self.server.listen()
        print(f"[LISTENING] Server is listening on {SERVER}")
        while True:
            conn, addr = self.server.accept()
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")