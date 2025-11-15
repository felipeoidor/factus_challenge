from flask import Flask, render_template, request
from utils.json_loader import load_json
from models import base_header, fetch_catalog_data
from tokens import refreshed_token


app = Flask(__name__)


@app.route("/crear-factura", methods=["GET", "POST"])
def index():
    endpoints = load_json(json_file="config/endpoints.json")
    headers = base_header(refreshed_token)

    # Documents
    documents = load_json(json_file="config/code.json", get="documents")
    documents = [
        f"{document['code']} - {document['document']}" for document in documents
    ]
    if request.method == "POST":
        document = request.form.get("document")
        print(document)

    # Numbering range
    num_endpoint = endpoints.get("numbering_range").get("endpoint")
    num_range = fetch_catalog_data(num_endpoint, headers).get("data")
    num_range = [num["document"] for num in num_range.get("data")]
    if request.method == "POST":
        num = request.form.get("numbering-range")
        print(num)

    # Municipality
    mun_endpoint = endpoints.get("municipality").get("endpoint")
    mun_data = fetch_catalog_data(mun_endpoint, headers).get("data")
    department = sorted({mun["department"] for mun in mun_data})
    municipality = sorted({num["name"] for num in mun_data})
    if request.method == "POST":
        department_value = request.form.get("department")
        municipality_value = request.form.get("municipality")
        print(department_value)
        print(municipality_value)

    return render_template(
        "index.html",
        documents=documents,
        num_range=num_range,
        department=department,
        municipality=municipality,
    )
