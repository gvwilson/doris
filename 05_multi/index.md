# Handle Multiple Charts

-   Generalize what we built in [the previous lesson](../04_select/index.md)
    -   Multiple charts with multiple controls
-   [`server.py`](./server.py) defines functions to create controls and placeholders for charts
    -   Whatever generates the page must create the right controls
    -   Whatever serves data must format it for the right kind of chart
-   Include a hidden `input` in the form tying it to its chart
    -   Passed to server and returned in data
    -   Used to select the chart element
-   [`static/dashboard.js`](./static/dashboard.js) has a new function `displayAll(…)`
    -   Find all forms with class `controls` and send default settings to server
        to cause initial display of charts

## Run

1.  `python server.py --seed 12345`
1.  Go to <http://127.0.0.1/5000>
1.  Change the checkboxes.
1.  Click the button to fetch data and redisplay chart
