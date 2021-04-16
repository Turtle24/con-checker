import socket
from settings import DISCONNECT_MESSAGE, HEADER, SERVER, ADDR, FORMAT, RICHFORMAT
from rich.console import Console
from rich.theme import Theme

class ClientMaster:
    def __init__(self):
        custom_theme = Theme({
            "info" : "dim cyan",
            "warning": "magenta",
            "danger": "bold red"
        })
        self.console = Console(theme=custom_theme)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(ADDR)

    def username(self, name):
        name = name + ', name'
        username = name.encode(FORMAT)
        msg_length = len(username) + 6
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        self.client.send(send_length)
        self.client.send(username)
        print(self.client.recv(2048).decode(FORMAT))

    def send(self, msg: str, username='default'):
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        self.client.send(send_length)
        self.client.send(message)
        print(self.client.recv(2048).decode(FORMAT))

    def chatting(self):
        chatting = True
        self.console.print(f"Chat connecting", style="info")
        self.console.print('Username:', style="magenta")
        name = input()
        self.username(name)
        self.console.print(f"Welcome! {name}", style="info")
        while chatting:
            message = input()
            if message == 'exit':
                chatting = False
            self.send(message)

c = ClientMaster()
c.chatting()