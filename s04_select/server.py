"""Allow user to select subsets of data."""

from flask import Flask, request
from flask_cors import CORS
import htpy as h
from pathlib import Path

from static.shared.datagen import datagen
from static.shared.util import ordered_unique, parse_args, select_data


TITLE = "Doris"


def create_app(data):
    """Create Flask application."""
    app = Flask(TITLE, static_folder=Path("static").resolve(), static_url_path="/static")
    CORS(app)

    @app.get("/")
    def get_root():
        """Display home page."""
        return str(h.html[
            make_head(),
            h.body(onload="display()")[
                h.h1[TITLE],
                h.div(".chart-container")[
                    h.svg("#chart"),
                ],
                make_form(data),
            ],
        ])

    @app.get("/data")
    def get_data():
        """Get weight and length by sex as JSON."""
        datasets = [
            {"label": key, "data": select_data(data, "sex", key, x="weight", y="length")}
            for key in request.args.keys()
        ]
        return {
            "data": {
                "datasets": datasets
            }
        }

    return app


def make_form(data):
    """Create form controls."""
    buttons = []
    for sex in ordered_unique(data, "sex"):
        buttons.append(h.label(for_=sex)[sex])
        buttons.append(h.input(type="checkbox", id=f"check-{sex}", name=sex, value=sex, checked=True))

    return h.form("#selections", onsubmit="display(); return false;")[
        *buttons,
        h.button(type="submit")["submit"]
    ]


def make_head():
    """Make head of page."""
    return h.head[
        h.title[TITLE],
        h.link(rel="icon", type="image/x-icon", href="/static/shared/favicon.ico"),
        h.link(rel="stylesheet", href="/static/shared/dashboard.css"),
        h.script(src="/static/shared/runtime.js"),
        h.script(src="/static/shared/chart.xkcd.min.js"),
        h.script(src="/static/dashboard.js"),
    ]


if __name__ == "__main__":
    options = parse_args()
    data = datagen(options.seed)
    app = create_app(data)
    app.run()
