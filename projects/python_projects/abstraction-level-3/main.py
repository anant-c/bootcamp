from pathlib import Path
from typing import Iterator, List, Optional

from core import apply_processors
from types_processor import ProcessorFn

def read_lines(path: Path) -> Iterator[str]:
    """ Read lines from a file and yield each line."""

    with path.open('r') as f:
        for line in f:
            yield line 

def write_output(lines: Iterator[str], output_path: Optional[Path]) -> None:
    """ Writes an iterator of lines to a file or to standard output. """

    if output_path:
        with output_path.open("w") as f:
            output_content = "\n".join(lines)
            f.write(output_content)
    else:
        for line in lines:
            print(line)

def process_file(input_path: Path, output_path: Optional[Path], pipeline: List[ProcessorFn]) -> None:
    """
    Reads a file, applies a processing pipeline to each line, and writes the output.
    """

    lines_iterator = read_lines(input_path)

    transformed_lines = (apply_processors(line, pipeline) for line in lines_iterator)

    write_output(transformed_lines, output_path)