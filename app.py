from flask import Flask, render_template
from models import get_numbering_range, get_municipality
from tokens import refreshed_access_token


app = Flask(__name__)


@app.route("/")
def index():
    data = get_municipality(refreshed_access_token)
    numrange = get_numbering_range(refreshed_access_token)

    numbering_range = [f"{x['id']}: {x['document']}" for x in numrange]

    # department - municipality
    locations = [
        {"department": item["department"], "municipality": item["name"]}
        for item in data
    ]

    # select index.html (option)
    department = sorted({item["department"] for item in locations})
    municipality = [item["municipality"] for item in locations]

    return render_template(
        "index.html",
        numbering_range=numbering_range,
        department=department,
        municipality=municipality,
    )
