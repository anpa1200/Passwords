"""Tests for phone_numbers_gen module."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from phone_numbers_gen import generate_phone_numbers, DEFAULT_PREFIXES


def test_generate_phone_numbers_limit(tmp_path):
    out = tmp_path / "out.txt"
    n = generate_phone_numbers(out, prefixes=["050"], digits_after_prefix=2, limit=5, verbose=False)
    assert n == 5
    lines = out.read_text().strip().split("\n")
    assert lines == ["05000", "05001", "05002", "05003", "05004"]


def test_generate_phone_numbers_prefixes(tmp_path):
    out = tmp_path / "out.txt"
    n = generate_phone_numbers(
        out, prefixes=["09"], digits_after_prefix=1, limit=3, verbose=False
    )
    assert n == 3
    assert out.read_text().strip().split("\n") == ["090", "091", "092"]


def test_default_prefixes():
    assert "050" in DEFAULT_PREFIXES
    assert len(DEFAULT_PREFIXES) == 9
