from rich import print

import random
import time

from rich.live import Live
from rich.table import Table

print("[bold red]Just Chatting[/bold red] [bold blue]Welcome To LAN CHAT[/bold blue]")

def generate_table() -> Table:
    """Make a new table."""
    table = Table()
    table.add_column("Username")
    table.add_column("Message")
    table.add_column("Status")
    chats = open('chat_history.txt', 'r')
    for chat in chats:
        user, message = chat.split('-')[0], chat.split('-')[1]
        table.add_row(
            f"{user}", f"{message}", "[red]ERROR" if user is None else "[green]SUCCESS"
        )
    return table

with Live(generate_table(), refresh_per_second=4) as live:
    for _ in range(40):
        time.sleep(0.4)
        live.update(generate_table())