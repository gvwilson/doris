# Create a Framework

-   Separate generic/reusable code from application-specific code
-   [`doris.py`](./doris.py) is derived from [Flask][flask] application
    -   Store callbacks
    -   Provide a decorator method to register callbacks
    -   And helper methods to make the page, placeholders for charts, etc.
-   Application-specific code remains in [`server.py`](./server.py)
    -   Page elements
    -   Callback to get data (because of filtering and rearrangement)
    -   Helper function to make controls (which are then wrapped as a form)
-   Again, no changes to [`static/dashboard.js`](./static/dashboard.js)

## Run

1.  `python server.py --seed 12345`
1.  Go to <http://127.0.0.1/5000>
1.  Change the checkboxes
1.  Click the button to fetch data and redisplay chart

[flask]: https://flask.palletsprojects.com/
