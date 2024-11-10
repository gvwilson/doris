# Trigger Events

<p id="terms"></p>

-   Eliminate clumsiness of explicit form submission by adding on-click event handlers to checkboxes
-   Remove `submit` handler from form
    -   But keep the ID so that `display(…)` knows what data to submit
-   Add `make_onclick(…)` method to [`doris.py`](./doris.py) to create `onclick` event handler
    -   Just a call to `display(…)` with the name of the form
    -   Form still used to group controls
-   Add `onclick=…` attribute when creating control `make_controls(…)` in [`server.py`](./server.py)

## Run

1.  `python server.py --seed 12345`
1.  Go to <http://127.0.0.1/5000>
1.  Change the checkboxes
