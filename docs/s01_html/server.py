"""Generate HTML programmatically."""

from flask import Flask
from flask_cors import CORS
import htpy as h
from markupsafe import Markup
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
        """Display home page with static HTML table."""
        html = data._repr_html_()
        start = html.find("<tbody>")
        end = html.find("</div>")
        html = f"<table>{html[start:end]}"
        return wrap([Markup(html)])

    return app


def wrap(content):
    """Wrap request-specific content."""
    return str(h.html[
        h.head[
            h.title[TITLE],
            h.link(rel="icon", type="image/x-icon", href="/static/shared/favicon.ico"),
            h.link(rel="stylesheet", href="/static/shared/dashboard.css"),
        ],
        h.body[
            h.h1[TITLE],
            *content
        ],
    ])


if __name__ == "__main__":
    options = parse_args()
    data = datagen(options.seed)
    app = create_app(data)
    app.run()
