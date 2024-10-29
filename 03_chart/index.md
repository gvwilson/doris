# Create a Chart

-   Use [Chart.xkcd][chartxkcd] to display chart
    -   Create a button and an empty SVG
    -   When button clicked, fetch data and pass to `chartXkcd.XY(…)` in [`static/dashboard.js`](static/dashboard.js)
-   Modify the `/data` route in the [Flask][flask] application to return JSON data
    -   Format it in the server rather than sending columns and reorganizing in the browser
-   Put the chart in a `div` whose maximum width is set in CSS

## Run

1.  `python server.py --seed 12345`
1.  Go to <http://127.0.0.1/5000>
1.  Click the button to fetch data and display chart

[chartxkcd]: https://timqian.com/chart.xkcd/
[flask]: https://flask.palletsprojects.com/
