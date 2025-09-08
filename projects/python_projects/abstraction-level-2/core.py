from typing import List
from types_processor import ProcessorFn

def to_uppercase(line:str) -> str:
    """ Converts a line to uppercase. """

    return line.upper()


def to_snakecase(line:str) -> str:
    """ Converts a line to snake_case. """

    return line.lower().replace(" ", "_")

def apply_processors(line:str, processors:List[ProcessorFn]) -> str:
    """ Applies a list of processor functions to a line sequentially. """

    processed_line = line.strip()

    for processor in processors:
        processed_line = processor(processed_line)
    return processed_line