"""Fetch table dynamically."""

from flask import Flask
from flask_cors import CORS
import htpy as h
from pathlib import Path

from static.shared.datagen import datagen
from static.shared.util import parse_args


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
            h.body[
                h.h1[TITLE],
                h.p[
                    h.button(type="button", onclick="display()")["display"],
                ],
                h.div("#display"),
            ],
        ])

    @app.get("/data")
    def get_data():
        """Get data as HTML table."""
        html = data._repr_html_()
        start = html.find("<tbody>")
        end = html.find("</div>")
        return {"table": f"<table>{html[start:end]}"}

    return app


def make_head():
    """Make head of page."""
    return h.head[
        h.title[TITLE],
        h.link(rel="icon", type="image/x-icon", href="/static/shared/favicon.ico"),
        h.link(rel="stylesheet", href="/static/shared/dashboard.css"),
        h.script(src="/static/dashboard.js"),
    ]


if __name__ == "__main__":
    options = parse_args()
    data = datagen(options.seed)
    app = create_app(data)
    app.run()
