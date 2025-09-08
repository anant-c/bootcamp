import os
import sys
from pathlib import Path
from typing import Iterator, Optional

import typer
from dotenv import load_dotenv
from typing_extensions import Annotated

load_dotenv()


def read_lines(path: Path) -> Iterator[str]:
    """Reads a file and yields its lines one by one."""
    with path.open() as f:
        for line in f:
            yield line


def transform_line(line: str, mode: str) -> str:
    """Transforms a single line based on the selected mode."""
    processed_line = line.strip()
    if mode == "uppercase":
        return processed_line.upper()
    elif mode == "snakecase":
        return processed_line.lower().replace(" ", "_")
    else:
        print(f"Error: Invalid mode '{mode}'. Exiting.", file=sys.stderr)
        raise typer.Exit(code=1)


def write_output(lines: Iterator[str], output_path: Optional[Path]) -> None:
    """Writes an iterator of lines to a file or to standard output."""
    if output_path:
        with output_path.open("w") as f:
            for i, line in enumerate(lines):
                if i > 0:
                    f.write("\n")
                f.write(line)
    else:
        for line in lines:
            print(line)


# Create a Typer application
app = typer.Typer()


@app.command()
def process(
    input_path: Annotated[
        Path,
        typer.Option(
            "--input",
            help="Path to the input file.",
            exists=True,
            file_okay=True,
            dir_okay=False,
            readable=True,
            resolve_path=True,
        ),
    ],
    output_path: Annotated[
        Optional[Path],
        typer.Option(
            "--output",
            help="Path to the output file. Prints to stdout if not provided.",
            resolve_path=True,
        ),
    ] = None,
    mode: Annotated[
        str,
        typer.Option(
            "--mode",
            help="Processing mode: 'uppercase' or 'snakecase'.",
        ),
    ] = os.getenv("MODE", "uppercase"),
):
    """
    Processes a text file by transforming its lines based on the selected mode.
    """
    lines_iterator = read_lines(input_path)

    transformed_lines = (transform_line(line, mode) for line in lines_iterator)

    write_output(transformed_lines, output_path)
    
    if output_path:
        print(f"✅ Success: Processed '{input_path.name}' to '{output_path.name}' in '{mode}' mode.", file=sys.stderr)


if __name__ == "__main__":
    app()
