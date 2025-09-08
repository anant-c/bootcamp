from pathlib import Path
from typing import Iterator, List, Optional
from core import run_pipeline
from types_processor import StreamProcessor

def read_lines(path: Path) -> Iterator[str]:
    """Read lines from a file, yielding each line without trailing newline."""
    with path.open('r', encoding='utf-8') as f:
        for line in f:
            yield line.rstrip('\n')

def write_output(lines: Iterator[str], output_path: Optional[Path]) -> None:
    """Write lines to a file or stdout, one per line."""
    if output_path:
        with output_path.open("w", encoding='utf-8') as f:
            first = True
            for line in lines:
                if not first:
                    f.write("\n")
                f.write(line)
                first = False
    else:
        for line in lines:
            print(line)

def process_file(input_path: Path, output_path: Optional[Path], pipeline: List[StreamProcessor]) -> None:
    lines_iterator = read_lines(input_path)
    transformed_lines = run_pipeline(lines_iterator, pipeline)
    write_output(transformed_lines, output_path)
