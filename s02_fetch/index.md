# Fetch Data

<p id="terms"></p>

-   [`server.py`](./server.py): page initially has button and empty `div`
-   When button clicked, JavaScript in [`static/dashboard.js`](static/dashboard.js)
    sends a [`GET`](g:http-get) [request](g:http-request) to a new [route](g:route) in the [Flask][flask] server
    -   An asynchronous function
-   Response is [JSON](g:json) containing HTML string representation of table
    -   Have to do some substring operations to extract it from what the dataframe generates
-   Assign that string to the inner HTML of the `div`

## Run

1.  `python server.py --seed 12345`
1.  Go to <http://127.0.0.1/5000>
1.  Click the button to fetch and display HTML

[flask]: https://flask.palletsprojects.com/
