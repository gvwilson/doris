"""Dashboard application class."""

from flask import Flask, request
from flask_cors import CORS
import htpy as h

from static.shared.util import select_colors


CHART_KEY = "_chart"
TITLE = "Doris"


class Doris(Flask):
    """Application class."""

    def __init__(self, data, *args, **kwargs):
        """Construct."""
        super().__init__(TITLE, *args, **kwargs)
        self.data = data
        self.callbacks = {}
        self.title = TITLE
        self.chart_key = CHART_KEY
        CORS(self)

        @self.get("/data")
        def get_data():
            """Invoke callback to get data for chart."""
            chartId = request.args[self.chart_key]
            datasets = self.callbacks[chartId](self.data)
            return {
                self.chart_key: chartId,
                "data": {
                    "datasets": datasets
                },
                "options": {
                    "dataColors": select_colors(data, "sex", [d["label"] for d in datasets])
                }
            }

    def chart_name(self, name):
        """Make HTML name for chart."""
        return f"chart-{name}"

    def controls_name(self, name):
        """Make HTML name for form controlling chart."""
        return f"controls-{name}"

    def make_chart(self, name):
        """Create placeholder for chart."""
        chartName = self.chart_name(name)
        return h.div(".chart-container")[
            h.svg(f"#{chartName}", class_="chart"),
        ]

    def make_controls(self, name, controls):
        """Create form controlling chart."""
        controls_name = self.controls_name(name)
        callback = f"display('#{controls_name}'); return false;"
        return h.form(f"#{controls_name}", class_="controls", onsubmit=callback)[
            *controls,
            h.input(type="hidden", name=self.chart_key, value=self.chart_name(name)),
        ]

    def make_head(self):
        """Make head of page."""
        return h.head[
            h.title[self.title],
            h.link(rel="icon", type="image/x-icon", href="/static/shared/favicon.ico"),
            h.link(rel="stylesheet", href="/static/shared/dashboard.css"),
            h.script(src="/static/shared/runtime.js"),
            h.script(src="/static/shared/chart.xkcd.min.js"),
            h.script(src="/static/dashboard.js"),
        ]

    def make_onclick(self, name):
        """Make onclick handler for control."""
        controls_name = self.controls_name(name)
        return f"display('#{controls_name}')"

    def make_page(self, *elements):
        return str(h.html[
            self.make_head(),
            h.body(onload="displayAll()")[*elements],
        ])

    def register(self, name):
        """Register callback function."""
        def decorator(func):
            self.callbacks[self.chart_name(name)] = func
            return func
        return decorator
