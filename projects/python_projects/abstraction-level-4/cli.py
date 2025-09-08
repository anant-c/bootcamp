import sys
from pathlib import Path
from typing import Optional
import typer
from typing import Annotated
from main import process_file
from pipeline import load_pipeline_from_config

app = typer.Typer()

@app.command()
def main(
    input_path: Annotated[
        Path,
        typer.Option("--input", "-i", help="Path to the input file",
                     exists=True, file_okay=True, dir_okay=False, readable=True, resolve_path=True)
    ],
    config_path: Annotated[
        Path,
        typer.Option("--config", "-c", help="Path to the YAML config defining the processing pipeline",
                     exists=True, file_okay=True, dir_okay=False, readable=True, resolve_path=True)
    ],
    output_path: Annotated[
        Optional[Path],
        typer.Option("--output", "-o", help="Path to the output file (prints to stdout if omitted)",
                     resolve_path=True)
    ] = None
):
    """Run a streaming text processing pipeline."""
    pipeline = load_pipeline_from_config(config_path)
    process_file(input_path, output_path, pipeline)
    if output_path:
        print(
            f"✅ Success: Processed '{input_path.name}' to '{output_path.name}' using '{config_path.name}'.",
            file=sys.stderr
        )

if __name__ == "__main__":
    app()
