# Generate HTML

-   Introduce some tools we will use
-   [`server.py`](server.py): [Flask][flask] application
    -   Use [htpy][htpy] to generate HTML
    -   Convert [dataframe](g:dataframe) to HTML table and insert directly
    -   Get the RNG seed from the command line if one is given
-   [`../shared/datagen.py`](../shared/datagen.py): generate a dataset as [Polars][polars] dataframe
    -   Female, male, or indeterminate snails
    -   Weight depends on sex
    -   Length correlates with sex and weight
-   `./static` contains symbolic link to `../shared`
    -   [Static files](g:static-file) shared between lessons are in `../shared`
    -   Making it appear under `./static` simplifies configuration of static directory in [Flask][flask]

## Run

1.  `python server.py --seed 12345`
1.  Go to <http://127.0.0.1/5000>

[flask]: https://flask.palletsprojects.com/
[htpy]: https://htpy.dev/
[polars]: https://pola.rs/
