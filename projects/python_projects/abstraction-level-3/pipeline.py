import sys
import yaml
import importlib
from pathlib import Path
from typing import List, Dict, Any

from types_processor import ProcessorFn

def _load_processor_from_path(dotted_path: str) -> ProcessorFn:
    """Dynamically loads a processor function from a dotted import path."""
    try:
        module_path, function_name = dotted_path.rsplit('.', 1)
        module = importlib.import_module(module_path)
        return getattr(module, function_name)
    except (ImportError, AttributeError) as e:
        print(f"❌ Error: Could not import processor '{dotted_path}'.\n{e}", file=sys.stderr)
        sys.exit(1)

def load_pipeline_from_config(config_path: Path) -> List[ProcessorFn]:
    """
    Parses a YAML config file and returns the corresponding processing pipeline.
    """
    try:
        with config_path.open('r') as f:
            config: Dict[str, Any] = yaml.safe_load(f)
    except FileNotFoundError:
        print(f"❌ Error: Config file not found at '{config_path}'.", file=sys.stderr)
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"❌ Error: Could not parse YAML config file.\n{e}", file=sys.stderr)
        sys.exit(1)

    pipeline_config = config.get('pipeline')
    if not isinstance(pipeline_config, list):
        print("❌ Error: Config file must contain a 'pipeline' key with a list of processors.", file=sys.stderr)
        sys.exit(1)


    pipeline: List[ProcessorFn] = []
    for item in pipeline_config:
        if isinstance(item, dict) and 'type' in item:
            processor_path = item['type']
            processor_fn = _load_processor_from_path(processor_path)
            pipeline.append(processor_fn)
        else:
            print(f"❌ Error: Invalid item in pipeline config: {item}", file=sys.stderr)
            sys.exit(1)
            
    return pipeline