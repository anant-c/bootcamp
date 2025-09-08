from typing import List
from types_processor import ProcessorFn

def apply_processors(line:str, processors:List[ProcessorFn]) -> str:
    """ Applies a list of processor functions to a line sequentially. """

    processed_line = line.strip()

    for processor in processors:
        processed_line = processor(processed_line)
    return processed_line