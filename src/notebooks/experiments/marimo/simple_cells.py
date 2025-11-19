#!/usr/bin/env python3
"""Demonstration of simple cells in Marimo."""

import marimo


__generated_with = "0.17.7"
app = marimo.App()


@app.cell
def _definition():
    a = 1
    return (a,)


@app.cell
def _output(a):
    a
