import pytest
from bank import value


def test_value():
    assert value("Hello") == "$0"

def test_h():
    assert value("H")     == "$20"

def test_not_Hello():
    assert value("Hello") or value("H") != "$100"
