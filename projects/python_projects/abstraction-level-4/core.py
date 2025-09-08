# core.py
from typing import Iterator, List, Callable
from types_processor import StreamProcessor

def run_pipeline(lines: Iterator[str], processors: List[StreamProcessor]) -> Iterator[str]:
    """Run a stream of lines through a sequence of stream processors."""
    for processor in processors:
        lines = processor(lines)
    return lines
