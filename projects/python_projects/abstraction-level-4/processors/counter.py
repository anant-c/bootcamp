from typing import Iterator

class LineCounter:
    """Stateful processor that prefixes each line with a running count."""
    def __init__(self, start: int = 1, fmt: str = "{n}\t{line}"):
        self.n = start
        self.fmt = fmt

    def __call__(self, lines: Iterator[str]) -> Iterator[str]:
        for line in lines:
            yield self.fmt.format(n=self.n, line=line)
            self.n += 1
