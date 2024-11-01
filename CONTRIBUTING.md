# Contributing

Contributions are very welcome;
please contact us [by email][email] or by filing an issue in [our repository][repo].
All contributors must abide by our [Code of Conduct](./CODE_OF_CONDUCT.md).

## Setup

-   Install [uv][uv].
-   Create a virtual environment by running `uv venv` in the root directory.
-   Activate it by running `source .venv/bin/activate` in your shell.
-   Install dependencies by running `uv pip install -r pyproject.toml`.

## Operation

-   Run `make` in the root directory to display operations:
    -   `make commands`: show available commands
    -   `make clean`: clean up
    -   `make build`: regenerate HTML in `./docs`
    -   `make lint`: check code and project
    -   `make serve`: serve generated HTML
    -   `make stats`: basic site statistics
-   See the `Run` section of each lesson's `index.md` file for more specific instructions.

## Contributions

Please use [Conventional Commits][conventional] style for pull requests
by using `feature:`, `fix:`, or `refactor:` as the first word
in the title of the commit message.

## Notes

1.  Each lesson has a `static` directory lesson-specific files needed by the browser.
    Each `static` directory also has a symbolic link to the `shared` directory in the project root,
    which contains files shared between lessons.
    This pattern allows us to configure a single static path in [Flask][flask]
    and then refer to lesson-specific files as `/static/whatever`
    and shared static files as `/static/shared/whatever`.
    Thanks to `__init__.py` files in `shared` and each `static` directory,
    it also allows us to import `static.shared.whatever` in Python.

## FAQ

Do you need any help?
:   Yes: please see the issues in [our repository][repo].

What sort of feedback would be useful?
:   Everything is welcome,
    from pointing out mistakes in the code to suggesting better examples or explanations.

Can I add a new section?
:   Probably: please [reach out][email] before doing so.

Why is this material free to read?
:   Because if we all give a little, we all get a lot.

## Contributors

-   [*Greg Wilson*][wilson-greg] is a programmer, author, and educator based in Toronto.
    He was the co-founder and first Executive Director of Software Carpentry
    and received ACM SIGSOFT's Influential Educator Award in 2020.

[conventional]: https://www.conventionalcommits.org/
[email]: mailto:gvwilson@third-bit.com
[flask]: https://flask.palletsprojects.com/
[repo]: https://github.com/gvwilson/doris
[uv]: https://github.com/astral-sh/uv
[wilson-greg]: https://third-bit.com/
