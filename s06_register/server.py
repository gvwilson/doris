"""Register callback functions to handle chart updates."""

from flask import Flask, request
from flask_cors import CORS
import htpy as h
from pathlib import Path

from static.shared import datagen, util


TITLE = "Doris"
Callbacks = {}


def register(name):
    """Register callback function."""
    def decorator(func):
        Callbacks[name] = func
        return func
    return decorator


@register("chart-top")
def handle_top(data):
    """Callback handler for top chart."""
    return [
        {"label": key, "data": util.select_data(data, "sex", key, x="weight", y="length")}
        for key in util.interesting_keys(request)
    ]


@register("chart-bottom")
def handle_bottom(data):
    """Callback handler for bottom chart."""
    return [
        {"label": key, "data": util.select_data(data, "sex", key, x="length", y="weight")}
        for key in util.interesting_keys(request)
    ]


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
        """Invoke callback to get data for chart."""
        chartId = request.args["_chart"]
        datasets = Callbacks[chartId](data)
        return {
            "_chart": chartId,
            "data": {
                "datasets": datasets
            },
            "options": {
                "dataColors": util.select_colors(data, "sex", [d["label"] for d in datasets])
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
    for sex in util.ordered_unique(data, "sex"):
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
    options = util.parse_args()
    data = datagen.generate(options.seed)
    app = create_app(data)
    app.run()
