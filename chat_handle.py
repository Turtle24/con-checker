from client import send, username
from rich.console import Console
from rich.theme import Theme

console = Console()
custom_theme = Theme({
    "info" : "dim cyan",
    "warning": "magenta",
    "danger": "bold red"
})
console = Console(theme=custom_theme)

def chatting():
    chatting = True
    console.print(f"Chat connecting", style="info")
    console.print('Username:', style="magenta")
    name = input()
    username(name)
    console.print(f"Welcome! {name}", style="info")
    while chatting:
        message = input()
        if message == 'exit':
            chatting = False
        send(message)

chatting()