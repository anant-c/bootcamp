import sys
import yaml
import importlib
import inspect
from pathlib import Path
from typing import List, Dict, Any, Callable
from types_processor import StreamProcessor, as_stream

def _load_attr(dotted_path: str):
    try:
        module_path, attr_name = dotted_path.rsplit('.', 1)
        module = importlib.import_module(module_path)
        return getattr(module, attr_name)
    except (ImportError, AttributeError) as e:
        print(f"❌ Error: Could not import '{dotted_path}'.\n{e}", file=sys.stderr)
        sys.exit(1)

def _to_stream_processor(obj: Any, cfg: Dict[str, Any] | None) -> StreamProcessor:
    # If it's a class, instantiate (with cfg if provided), and expect __call__(Iterator[str]) -> Iterator[str]
    if inspect.isclass(obj):
        try:
            instance = obj(**(cfg or {}))
        except TypeError as e:
            print(f"❌ Error: Cannot instantiate '{obj.__name__}' with config {cfg}: {e}", file=sys.stderr)
            sys.exit(1)
        if not callable(instance):
            print(f"❌ Error: '{obj.__name__}' is not callable after instantiation.", file=sys.stderr)
            sys.exit(1)
        return instance  # type: ignore[return-value]

    # If it's a callable function, assume it's a line processor and wrap it
    if callable(obj):
        return as_stream(obj)  # type: ignore[arg-type]

    print(f"❌ Error: Loaded object '{obj}' is neither a class nor a callable.", file=sys.stderr)
    sys.exit(1)

def load_pipeline_from_config(config_path: Path) -> List[StreamProcessor]:
    try:
        with config_path.open('r', encoding='utf-8') as f:
            config: Dict[str, Any] = yaml.safe_load(f) or {}
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

    pipeline: List[StreamProcessor] = []
    for item in pipeline_config:
        if isinstance(item, dict) and 'type' in item:
            dotted = item['type']
            cfg = item.get('config') if isinstance(item.get('config'), dict) else None
            obj = _load_attr(dotted)
            sp = _to_stream_processor(obj, cfg)
            pipeline.append(sp)
        else:
            print(f"❌ Error: Invalid item in pipeline config: {item}", file=sys.stderr)
            sys.exit(1)

    return pipeline
