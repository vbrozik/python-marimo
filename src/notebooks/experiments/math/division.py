"""Experiment with mathematical algorithms related to division."""

from __future__ import annotations

import marimo


__generated_with = "0.18.4"
app = marimo.App(width="full")

with app.setup:
    from typing import Sequence

    import marimo as mo
    import polars as pl


@app.cell
def _md_introduction():
    mo.md(r"""
    # Experiment with mathematical algorithms related to division
    """)
    return


@app.function
def gcd(a: int, b: int) -> int:
    """Compute the greatest common divisor of a and b using the Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a


@app.function
def factorization(n: int) -> Sequence[int]:
    """Return the prime factorization of n as a list of prime factors."""
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


@app.function
def common_factors(factors_a: Sequence[int], factors_b: Sequence[int]) -> Sequence[int]:
    """Return the common factors of two sorted lists of factors."""
    i, j = 0, 0
    common = []
    while i < len(factors_a) and j < len(factors_b):
        if factors_a[i] < factors_b[j]:
            i += 1
        elif factors_a[i] > factors_b[j]:
            j += 1
        else:
            common.append(factors_a[i])
            i += 1
            j += 1
    return common


@app.function
def gcd_table(data: Sequence[tuple[int, int]]) -> pl.DataFrame:
    """Generate a table of unique pairs of a and b for the gcd function."""
    gcd_values = [gcd(a, b) for a, b in data]
    fact_a = [factorization(a) for a, b in data]
    fact_b = [factorization(b) for a, b in data]
    common_factors_ab = [common_factors(fa, fb) for fa, fb in zip(fact_a, fact_b)]

    return pl.DataFrame({
        "a": [a for a, b in data],
        "b": [b for a, b in data],
        "gcd": gcd_values,
        "factorization_a": fact_a,
        "factorization_b": fact_b,
        "common_factors": common_factors_ab,
    })


@app.cell
def _example_data():
    # WIP: Make the testing data editable.
    # See https://docs.marimo.io/api/inputs/data_editor/
    example_data = (
        (48, 18),
        (56, 24),
        (101, 17),
        (1001, 7),
        (5, 25),
    )
    # Compatible table format has to be used for example_data to be editable.
    mo.ui.data_editor(example_data, label="Example Data for GCD Calculation")
    return (example_data,)


@app.cell
def _gcd_table_example(example_data):
    gcd_df = gcd_table(example_data)
    gcd_df
    return


if __name__ == "__main__":
    app.run()
