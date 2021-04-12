from client import send
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
    console.print(f"Choose a style: {['red bold']}", style="info")
    style = input()
    console.print('Noice choice!', style="danger")
    message = input()
    send(message)

chatting()