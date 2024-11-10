"""Register callback functions to handle chart updates."""

from flask import request
import htpy as h
from pathlib import Path

from static.shared import datagen, util
from doris import Doris


def create_app(data):
    """Create Flask application."""
    app = Doris(data, static_folder=Path("static").resolve(), static_url_path="/static")

    @app.get("/")
    def get_root():
        """Display home page."""
        return app.make_page(
            h.h1[app.title],
            app.make_chart("example"),
            make_controls(app, data, "example"),
        )

    @app.register("example")
    def handle_example(data):
        """Callback handler for example chart."""
        return [
            {"label": key, "data": util.select_data(data, "sex", key, x="weight", y="length")}
            for key in util.interesting_keys(request)
        ]

    return app


def make_controls(app, data, name):
    """Create form controls for chart."""
    buttons = []
    for sex in util.ordered_unique(data, "sex"):
        buttons.append(h.label(for_=sex)[sex])
        buttons.append(
            h.input(
                type="checkbox",
                id=f"check-{name}-{sex}",
                name=sex,
                value=sex,
                checked=True,
                onclick=app.make_onclick(name),
            )
        )
    return app.make_controls(name, buttons)


if __name__ == "__main__":
    options = util.parse_args()
    data = datagen.generate(options.seed)
    app = create_app(data)
    app.run()
