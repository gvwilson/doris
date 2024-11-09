# Trigger Events

-   Eliminate need for explicit form submission by adding event handlers to checkboxes
-   Remove `submit` handler from form (but keep ID)
-   Add `make_onclick(…)` to [`doris.py`](./doris.py) to create `onclick` event handler
-   Add `onclick=…` when creating control in [`server.py`](./server.py)

## Run

1.  `python server.py --seed 12345`
1.  Go to <http://127.0.0.1/5000>
1.  Change the checkboxes
