"""Utility functions."""

import argparse


def ordered_unique(df, col):
    """Return ordered unique values in dataframe column."""
    return sorted(df[col].unique())


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=None, help="RNG seed")
    return parser.parse_args()


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
