import pytest
from bank import value


def test_value():
    assert value("hello") == "$0"


def test_notvalue():
    assert value("*") == "$100"

def test_h():
    assert value("h")    == "$20"

def test_not_Hello():
    assert value("Hello") == "$0"  # Check for "Hello"
    assert value("H") == "$20"      # Check for "H"
