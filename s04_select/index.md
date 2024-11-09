# Select Data

<p id="terms"></p>

-   [`server.py`](./server.py) creates a [form](g:form) with checkboxes for every sex in the data
-   Add `onload` [event handler](g:event-handler) to `body` element to display chart when browser first loads page
    -   Use the default settings in the form to ensure consistent behavior
-   [`static/dashboard.js`](static/dashboard.js) turns form data into [query parameters](g:query-param)
    and appends them to the [URL](g:url)
    -   Checkbox's value is only present if it is ticked
-   `select_data(…)` in [`../shared/util.py`](../shared/util.py) selects data based on those query parameters
    -   Partition data according to sex
    -   Doesn't specify colors, so point colors may change when data subsetted

## Run

1.  `python server.py --seed 12345`
1.  Go to <http://127.0.0.1/5000>
1.  Change the checkboxes
1.  Click the button to fetch data and redisplay chart
