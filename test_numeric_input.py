"""
Test Numeric Input
"""
from numeric_input import read_int, read_float


def test_read_int_valid(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "10")
    assert read_int("Test Prompt", 1, 20) == 10


def test_read_int_invalid(monkeypatch):
    inputs = iter(["abc", "-1", "21", "15"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert read_int("Test Prompt", 1, 20) == 15


def test_read_int_edge(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "1")
    assert read_int("Test Prompt", 1, 20) == 1
    monkeypatch.setattr('builtins.input', lambda _: "20")
    assert read_int("Test Prompt", 1, 20) == 20


def test_read_float_valid(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "10.5")
    assert read_float("Test Prompt", 1.0, 20.0) == 10.5


def test_read_float_invalid(monkeypatch):
    inputs = iter(["abc", "-1", "21", "15.5"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert read_float("Test Prompt", 1.0, 20.0) == 15.5


def test_read_float_edge(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "1.0")
    assert read_float("Test Prompt", 1.0, 20.0) == 1.0
    monkeypatch.setattr('builtins.input', lambda _: "20.0")
    assert read_float("Test Prompt", 1.0, 20.0) == 20.0
