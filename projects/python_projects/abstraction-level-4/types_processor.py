from typing import Callable, Iterator, Protocol, Any, Dict

LineProcessor = Callable[[str], str]

StreamProcessor = Callable[[Iterator[str]], Iterator[str]]

def as_stream(fn: LineProcessor) -> StreamProcessor:
    """Wrap a line-based function so it can be used as a stream processor."""
    def _stream(lines: Iterator[str]) -> Iterator[str]:
        for line in lines:
            yield fn(line)
    _stream.__name__ = f"as_stream({getattr(fn, '__name__', 'processor')})"
    return _stream
