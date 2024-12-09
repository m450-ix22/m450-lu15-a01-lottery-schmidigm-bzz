"""
Test Authenticate
"""
from lottery import create_ticket
from person import Person


def test_valid_ticket_creation(monkeypatch):
    person = Person("John", "securepassword", 10.0)
    inputs = iter(["1", "2", "3", "4", "5", "6", "3"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    create_ticket(person)
    assert person.balance == 8.0
