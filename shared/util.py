"""Utility functions."""

import argparse

COLORS = [
    "#ff4040",
    "#40ff40",
    "#4040ff",
]


def interesting_keys(request):
    """Return ordered interesting keys."""
    return [key for key in sorted(request.args.keys()) if not key.startswith("_")]


def ordered_unique(df, col):
    """Return ordered unique values in dataframe column."""
    return sorted(df[col].unique())


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=None, help="RNG seed")
    return parser.parse_args()


def select_colors(df, col, actual):
    """Create reproducible list of colors."""
    temp = {
        c: COLORS[i] for i, c in enumerate(ordered_unique(df, col))
    }
    return [temp[a] for a in actual]


def select_data(df, col, required, **args):
    """Select a subset of data."""
    result = []
    for row in df.rows(named=True):
        if row[col] == required:
            record = {}
            for new, old in args.items():
                record[new] = row[old]
            result.append(record)
    return result
