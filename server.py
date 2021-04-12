import socket
import threading
import time
from rich.console import Console
import logging
from rich.logging import RichHandler

HEADER = 64
PORT = 5500
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
RICHFORMAT = "%(message)s"

console = Console()
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

logging.basicConfig(
    level="NOTSET", format=RICHFORMAT, datefmt="[%X]", handlers=[RichHandler()]
)
log = logging.getLogger("rich")

def disconnect(msg):
    if msg == 'exit':
        conn.close()

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        users = {}
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            if 'name' in msg:
                users[addr] = msg.split(',')[0]
                console.print(f"Username: {msg.split(',')[0]}", style='green bold')
            log.info(f"[{addr}: {msg}")
            console.print(msg, style='bold red')
            conn.send("Sent".encode(FORMAT))
    disconnect(msg)

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] server is starting...")
start()