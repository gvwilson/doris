"""Create and manage multiple charts with multiple controls."""

from flask import Flask, request
from flask_cors import CORS
import htpy as h
from pathlib import Path

from static.shared.datagen import datagen
from static.shared.util import parse_args, select_data


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
            h.body(onload="displayAll()")[
                h.h1[TITLE],
                make_chart("top"),
                make_controls(data, "top"),
                make_chart("bottom"),
                make_controls(data, "bottom"),
            ],
        ])

    @app.get("/data")
    def get_data():
        """Get weight and length by sex as JSON."""
        datasets = [
            {"label": key, "data": select_data(data, "sex", key, x="weight", y="length")}
            for key in request.args.keys()
            if not key.startswith("_")
        ]
        return {
            "_chart": request.args["_chart"],
            "data": {
                "datasets": datasets
            }
        }

    return app


def make_chart(name):
    """Create placeholder for chart."""
    return h.div(".chart-container")[
        h.svg(f"#chart-{name}", class_="chart"),
    ]


def make_controls(data, name):
    """Create form controls for chart."""
    buttons = []
    for sex in data["sex"].unique().to_list():
        buttons.append(h.label(for_=sex)[sex])
        buttons.append(
            h.input(type="checkbox", id=f"check-{name}-{sex}", name=sex, value=sex, checked=True)
        )

    callback = f"display('#controls-{name}'); return false;"
    return h.form(f"#controls-{name}", class_="controls", onsubmit=callback)[
        *buttons,
        h.button(type="submit")["submit"],
        h.input(type="hidden", name="_chart", value=f"chart-{name}"),
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
