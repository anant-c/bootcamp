import sys
from typing import List


from core import to_snakecase, to_uppercase
from types_processor import ProcessorFn


def get_pipeline(mode:str)-> List[ProcessorFn]:
    """
    Returns a processing pipeline based on the specified mode.
    """

    if mode == "uppercase":
        return [to_uppercase]
    elif mode == "snakecase":
        return [to_snakecase]
    else:
        print(f"Error: Invalid mode '{mode}'. Exiting.", file=sys.stderr)
        sys.exit(1)