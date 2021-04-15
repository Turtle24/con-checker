import socket
from settings import DISCONNECT_MESSAGE, HEADER, SERVER, ADDR, FORMAT, RICHFORMAT

class ClientMaster:

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    @staticmethod
    def username(name):
        name = name + ', name'
        username = name.encode(FORMAT)
        msg_length = len(username) + 6
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        client.send(send_length)
        client.send(username)
        print(client.recv(2048).decode(FORMAT))

    @staticmethod
    def send(msg: str, username='default'):
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        client.send(send_length)
        client.send(message)
        print(client.recv(2048).decode(FORMAT))
