"""
Test Person
"""
import pytest
from person import Person


def test_valid_person():
    person = Person("John", "securepassword", 50.0)
    assert person.givenname == "John"
    assert person.password == "securepassword"
    assert person.balance == 50.0


def test_invalid_balance():
    with pytest.raises(ValueError):
        Person("John", "securepassword", "not_a_number")
