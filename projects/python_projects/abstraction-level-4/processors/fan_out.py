from typing import Iterator

class Splitter:
    """
    Fan-out processor that splits a line and emits multiple lines.
    - delimiter: string delimiter to split on
    - keep_empty: emit empty tokens if True
    - strip: strip whitespace around tokens if True
    """
    def __init__(self, delimiter: str = ",", keep_empty: bool = False, strip: bool = True):
        self.delimiter = delimiter
        self.keep_empty = keep_empty
        self.strip_tokens = strip

    def __call__(self, lines: Iterator[str]) -> Iterator[str]:
        for line in lines:
            parts = line.split(self.delimiter)
            for p in parts:
                token = p.strip() if self.strip_tokens else p
                if token or self.keep_empty:
                    yield token
