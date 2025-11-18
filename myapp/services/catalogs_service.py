from myapp.config.loader import load_json
from myapp.services.api_client import base_header, fetch_catalog_data
from myapp.services.tokens import refreshed_token


headers = base_header(refreshed_token)


def endpoint(url: str):
    endpoints = load_json(json_file="json/endpoints.json").get(url)
    return endpoints.get("endpoint")


documents_dict = load_json(json_file="json/code.json")
documents_labels = [doc["document"] for doc in documents_dict.get("documents")]

numbering_range_dict = fetch_catalog_data(endpoint("numbering_range"), headers).get(
    "data"
)
numbering_range_labels = [num["document"] for num in numbering_range_dict.get("data")]

department_dict = fetch_catalog_data(endpoint("municipality"), headers).get("data")
department_labels = sorted({department["department"] for department in department_dict})
municipality_labels = sorted([mun["name"] for mun in department_dict])

tributes_dict = fetch_catalog_data(endpoint("tributes"), headers).get("data")
tributes_labes = [
    f"{tribute['name']} ({tribute['description']})" for tribute in tributes_dict
]

measurement_units_dict = fetch_catalog_data(endpoint("measurement units"), headers).get(
    "data"
)
measurement_units_labels = [
    f"{unit['code']} ({unit['name']})" for unit in measurement_units_dict
]

print(measurement_units_dict)
