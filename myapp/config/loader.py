import os
import json
import copy


def load_json(
    json_file: str, file_mode: str = "r", encoding: str = "UTF-8", get: str = None
) -> dict:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, json_file)

    try:
        with open(file_path, mode=file_mode, encoding=encoding) as f:
            data = json.load(f)
            data = copy.deepcopy(data)

            if get is None:
                return data

            return data.get(get)

    except FileNotFoundError:
        raise FileNotFoundError(f"JSON FILE not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Error decoding JSON in the file: {file_path}")
