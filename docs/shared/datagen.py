"""Data generator."""

import polars as pl
import random
import sys


NUM = 10
SEX = {
    "F": 0.48,
    "M": 0.47,
    "X": 0.05,
}
WEIGHT = {
    "F": 6.3,
    "M": 6.1,
    "X": 6.2,
}
WEIGHT_STD = 0.4
LENGTH = {
    "F": 0.50,
    "M": 0.54,
    "X": 0.52,
}
LENGTH_STD = 0.08
PRECISION = 2


def generate(seed):
    """Generate data."""
    random.seed(seed)
    data = []
    for _ in range(NUM):
        sex = gen_sex()
        weight = gen_weight(sex)
        length = gen_length(sex, weight)
        data.append([sex, weight, length])
    return pl.DataFrame(data, schema=["sex", "weight", "length"], orient="row")


def gen_length(sex, weight):
    """Generate length."""
    return round(random.gauss(weight * LENGTH[sex], LENGTH_STD), PRECISION)


def gen_sex():
    """Generate sex."""
    return random.choices(list(SEX.keys()), SEX.values(), k=1)[0]


def gen_weight(sex):
    """Generate weight."""
    return round(random.gauss(WEIGHT[sex], WEIGHT_STD), PRECISION)


if __name__ == "__main__":
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else None
    df = generate(seed)
    df.write_csv(sys.stdout)
