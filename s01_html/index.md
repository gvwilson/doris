# Generate HTML

<p id="terms"></p>

-   Introduce some tools we will use
-   [`server.py`](server.py): [Flask][flask] application
    -   Use [htpy][htpy] to generate HTML
    -   Convert [dataframe](g:dataframe) to HTML table and insert in page
    -   Get the random number generation [seed](g:rng-seed) from the command line if one is given
-   [`../shared/datagen.py`](../shared/datagen.py): generate a dataset as [Polars][polars] dataframe
    -   Sex is female, male, or indeterminate
    -   Weight depends on sex
    -   Length correlates with sex and weight
-   `./static` contains [symbolic link](g:symlink) to `../shared`
    -   [Static files](g:static-file) shared between lessons are in `../shared`
    -   Making it appear under `./static` simplifies configuration of [static directory](g:static-dir) in [Flask][flask]

## Run

1.  `python server.py --seed 12345`
1.  Go to <http://127.0.0.1/5000>

[flask]: https://flask.palletsprojects.com/
[htpy]: https://htpy.dev/
[polars]: https://pola.rs/
