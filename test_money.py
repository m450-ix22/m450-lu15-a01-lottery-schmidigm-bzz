"""
Test Money
"""
import pytest
from person import Person
from money import transfer_money


def test_valid_deposit(monkeypatch):
    person = Person("John", "securepassword", 50.0)
    inputs = iter(["E", "10.0", "Z"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    transfer_money(person)
    assert person.balance == 60.0


def test_invalid_transaction(monkeypatch):
    person = Person("John", "securepassword", 90.0)
    inputs = iter(["E", "15.0", "Z"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with pytest.raises(ValueError):
        transfer_money(person)
