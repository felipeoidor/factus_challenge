from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from config.loader import load_json  # noqa: E402
from services.api_client import base_header, fetch_catalog_data  # noqa: E402
from services.tokens import get_refreshed_token  # noqa: E402


headers = base_header(get_refreshed_token())


def endpoint(url: str):
    endpoints = load_json(json_file="json/endpoints.json").get(url)
    return endpoints.get("endpoint")


documents_dict = load_json(json_file="json/code.json")
documents_labels = [doc["name"] for doc in documents_dict.get("data")]

numbering_range_dict = fetch_catalog_data(endpoint("numbering_range"), headers)
numbering_range_labels = [num["document"] for num in numbering_range_dict.get("data").get("data")]

department_dict = fetch_catalog_data(endpoint("municipality"), headers)
department_labels = sorted({department["department"] for department in department_dict.get("data")})
municipality_labels = sorted([mun["name"] for mun in department_dict.get("data")])

tributes_dict = fetch_catalog_data(endpoint("tributes"), headers)
tributes_labes = [
    tribute['name'] for tribute in tributes_dict.get("data")
]

measurement_units_dict = fetch_catalog_data(endpoint("measurement units"), headers).get(
    "data"
)
measurement_units_labels = [
   unit['name'] for unit in measurement_units_dict
]




