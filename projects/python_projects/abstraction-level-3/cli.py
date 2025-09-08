import os
import sys
from pathlib import Path
from typing import List, Optional

import typer
from typing import Annotated

from main import process_file
from pipeline import load_pipeline_from_config

app = typer.Typer()

@app.command()
def main(
    input_path: Annotated[
        Path,
        typer.Option(
            "--input",
            "-i",   
            help="Path to the input file",
            exists=True,
            file_okay=True,
            dir_okay=False,
            readable=True,
            resolve_path=True
        )
    ],

    config_path: Annotated[
        Path,
        typer.Option(
            "--config",
            "-c",
            help="Path to the YAML config file defining the processing pipeline",
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
            "-o",
            help="Path to the output file (if not provided, output will be printed to stdout)",
            resolve_path=True
        )
    ] = None
):
    """
    Processes a text file by transforming its lines based on the selected mode.
    """

    pipeline = load_pipeline_from_config(config_path)

    process_file(input_path, output_path, pipeline)

    if output_path:
        print(f"✅ Success: Processed '{input_path.name}' to '{output_path.name}' in '{config_path.name}' mode.",
            file=sys.stderr)

if __name__ == "__main__":
    app()