from flask import Flask, render_template, request
from myapp.services.catalogs_service import (
    documents_labels,
    numbering_range_labels,
    department_labels,
    municipality_labels,
    tributes_labes,
    measurement_units_labels
)


# get value
def af(option: str):
    if request.method == "POST":
        client_option = request.form.get(option)
        return client_option


app = Flask(__name__)


@app.route("/crear-factura", methods=["GET", "POST"])
def index():

    docs = documents_labels

    num_range = numbering_range_labels

    departments = department_labels

    municipality = municipality_labels

    tributes = tributes_labes

    measuremente_units = measurement_units_labels

    return render_template(
        "index.html",
        docs=docs,
        num_range=num_range,
        departments=departments,
        municipality=municipality,
        tributes=tributes,
        measuremente_units=measuremente_units
    )
