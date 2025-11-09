from flask import Flask, render_template
from models import get_numbering_range
from tokens import refreshed_access_token


app = Flask(__name__)


@app.route("/")
def index():
    numbering_range = [
        f"{x['id']}: {x['document']}" for x in get_numbering_range(refreshed_access_token)
    ]

    return render_template("index.html", numbering_range=numbering_range)
