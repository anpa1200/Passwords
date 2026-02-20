"""Tests for base64_matches module."""

import base64
import tempfile
from pathlib import Path

import pytest

# Import after path setup if needed
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from base64_matches import encode_basic_auth, process_pairs, read_lines


def test_encode_basic_auth():
    assert encode_basic_auth("user", "pass") == base64.b64encode(b"user:pass").decode("utf-8")
    assert encode_basic_auth("", "p") == base64.b64encode(b":p").decode("utf-8")


def test_process_pairs():
    usernames = ["a", "b"]
    passwords = ["1", "2"]
    result = process_pairs(usernames, passwords)
    assert len(result) == 4
    decoded = [base64.b64decode(s).decode("utf-8") for s in result]
    assert set(decoded) == {"a:1", "a:2", "b:1", "b:2"}


def test_read_lines(tmp_path):
    f = tmp_path / "lines.txt"
    f.write_text("  a  \nb\n\nc\n")
    assert read_lines(f) == ["a", "b", "c"]
