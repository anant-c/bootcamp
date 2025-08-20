import typer
from rich.console import Console
from rich.text import Text

# Create a console object for rich output
console = Console()

def main(name: str = typer.Argument(default="world")):
    # Create rich styled text
    text = Text(f"Hello {name}!", style="bold green on black")
    console.print(text)

if __name__ == "__main__":
    typer.run(main)
