# Register Callbacks

-   Let developers define [callback functions](g:callback) to get data for particular charts
    -   Getting closer to an [application framework](g:app-framework) that runs application-specific functions
-   In [`server.py`](./server.py):
    -   Lookup table `Callbacks` maps chart name to callback function
    -   [Decorator](g:decorator) function `register(…)` adds entry
    -   `get_data(…)` uses the chart ID in the query parameters to select a callback function
-   Note that the decorator doesn't change the function: it just adds it to a lookup table
-   No changes to [`static/dashboard.js`](./static/dashboard.js)

## Run

1.  `python server.py --seed 12345`
1.  Go to <http://127.0.0.1/5000>
1.  Change the checkboxes.
1.  Click the button to fetch data and redisplay chart
