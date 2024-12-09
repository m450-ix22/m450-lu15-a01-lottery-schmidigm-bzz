"""
Test Ticket
"""
import pytest
from ticket import Ticket


def test_valid_ticket():
    ticket = Ticket(5, [1, 2, 3, 4, 5, 6])
    assert ticket.joker == 5
    assert ticket.numbers == [1, 2, 3, 4, 5, 6]


def test_invalid_joker():
    with pytest.raises(ValueError):
        Ticket("not_a_number", [1, 2, 3, 4, 5, 6])
