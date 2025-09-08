import os
import sys
from pathlib import Path
from typing import List, Optional

import typer
from dotenv import load_dotenv
from typing import Annotated

from main import process_file
from pipeline import get_pipeline

load_dotenv()

app = typer.Typer()

@app.command()
def process(
    input_path: Annotated[
        Path,
        typer.Option(
            "--input",
            help="Path to the input file",
            exists=True,
            file_okay=True,
            dir_okay=False,
            readable=True,
            resolve_path=True
        )
    ],
    output_path: Annotated[
        Optional[Path],
        typer.Option(
            "--output",
            help="Path to the output file (if not provided, output will be printed to stdout)",
            resolve_path=True
        )
    ] = None,

    mode: Annotated[
        str,
        typer.Option(
            "--mode",
            help="Processing mode.",
            case_sensitive=False
        ),
    ] = os.getenv("MODE", "uppercase").lower()
):
    """
    Processes a text file by transforming its lines based on the selected mode.
    """

    pipeline = get_pipeline(mode)

    process_file(input_path, output_path, pipeline)

    if output_path:
        print(f"✅ Success: Processed '{input_path.name}' to '{output_path.name}' in '{mode}' mode.",
            file=sys.stderr)

if __name__ == "__main__":
    app()