# processors/fan_in.py
from typing import Iterator, List

class PairJoiner:
    """
    Fan-in processor that joins N lines into one using a separator.
    - join_every: how many input lines to join per output
    - sep: separator between joined lines
    - emit_remainder: if True, emit the last partial group as-is
    """
    def __init__(self, join_every: int = 2, sep: str = " ", emit_remainder: bool = True):
        assert join_every > 0
        self.join_every = join_every
        self.sep = sep
        self.emit_remainder = emit_remainder

    def __call__(self, lines: Iterator[str]) -> Iterator[str]:
        buf: List[str] = []
        for line in lines:
            buf.append(line)
            if len(buf) == self.join_every:
                yield self.sep.join(buf)
                buf.clear()
        if buf and self.emit_remainder:
            yield self.sep.join(buf)
