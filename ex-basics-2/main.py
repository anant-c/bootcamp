import sys
from rich.console import Console
from rich.text import Text

# Create a console object for rich output
console = Console()

def main():
    # Get name argument from command line or default to "world"
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = "world"
    
    # Create rich styled text
    text = Text(f"Hello {name}!", style="bold green on black")
    console.print(text)

if __name__ == "__main__":
    main()
