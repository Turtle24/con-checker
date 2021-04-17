from rich import print

import random

from rich.live import Live
from rich.table import Table

print("[bold red]Just Chatting[/bold red] [bold blue]Welcome To LAN CHAT[/bold blue]")

def clear_chat():
    with open("chat_history.txt", "r") as file:
        data = file.readlines()
    if len(data) > 10: 
        with open("chat_history.txt", "w") as file:
            for line in data[-10:]:
                file.write(line)

def generate_table() -> Table:
    """Make a new table."""
    table = Table()
    table.add_column("Username")
    table.add_column("Message")
    table.add_column('Time')
    table.add_column("Status")
    chats = open('chat_history.txt', 'r')
    for chat in chats:
        user, message, sent_time = chat.split('-')[0], chat.split('-')[1], chat.split('-')[2]
        table.add_row(
            f"{user}", f"{message}", f"{sent_time}", "[red]OFFLINE" if 'exit' in message else "[green]ONLINE"
        )
    return table

with Live(generate_table(), refresh_per_second=1) as live:
    chatting = True
    while chatting:
        live.update(generate_table())
        clear_chat()
        
        