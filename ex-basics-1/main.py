import typer

def main(name: str = typer.Argument(default="world")):
    typer.echo(f"Hello {name}")

if __name__ == "__main__":
    typer.run(main)
