import json
import copy


def load_json(
    json_file: str, file_mode: str = "r", encoding: str = "UTF-8", get: str = None
) -> dict:
    with open(json_file, mode=file_mode, encoding=encoding) as f:
        data = json.load(f)
        data = copy.deepcopy(data)

        if get is None:
            return data

        return data.get(get)
