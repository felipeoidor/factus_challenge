from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from flask import Flask, render_template, request  # noqa: E402
from services.catalogs_service import (  # noqa: E402
    documents_labels,
    numbering_range_labels,
    department_labels,
    municipality_labels,
    tributes_labes,
    measurement_units_labels,
    documents_dict,
    numbering_range_dict,
    department_dict,
    tributes_dict,
    measurement_units_dict

    
)


# get value
def get_form_option(option: str, name: str, data: list):
    if request.method == "POST":
        client_option = request.form.get(option)
        for id in data:
            if client_option == id[name]:
                a = id["id"]
                return a



app = Flask(__name__)


@app.route("/crear-factura", methods=["GET", "POST"])
def index():
    docs = documents_labels
    document = get_form_option(option = "document", name="name", data=documents_dict.get("data"))
    print(document)
    
    num_range = numbering_range_labels
    number = get_form_option(option = "numbering-range", name="document", data=numbering_range_dict.get("data").get("data"))
    print(number)

    departments = department_labels
    #department = get_form_option(option = "department", data=department_dict)
    #print(department)

    municipalities = municipality_labels
    municipality = get_form_option(option = "municipality", name="name", data=department_dict.get("data"))
    print(municipality)

    tributes = tributes_labes
    tribute = get_form_option(option = "tribute", name="name", data=tributes_dict.get("data"))
    print(tribute)

    measurement_units = measurement_units_labels
    unit = get_form_option(option = "measurement_units", name="name", data=measurement_units_dict)
    print(unit)

    return render_template(
        "index.html",
        docs=docs,
        num_range=num_range,
        departments=departments,
        municipalities=municipalities,
        tributes=tributes,
        measurement_units=measurement_units,
    )
