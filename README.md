# Python marimo playground

This repository contains a simple playground for experimenting with the `marimo` library in Python. The `marimo` library is designed for building and managing data pipelines with ease.

## Installation

First install `uv` then install `marimo`:

``` bash
curl -LsSf https://astral.sh/uv/install.sh | sh

git clone https://github.com/vbrozik/python-marimo.git
cd python-marimo
uv sync
source .venv/bin/activate
```

## Usage

Example usage:

``` bash
marimo run experiments/math/complex_exponentiation.py
```
