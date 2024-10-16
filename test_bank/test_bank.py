import pytest
from bank import value


def test_value():
    assert value("hello").lower() == "$0"


def test_notvalue():
    assert value("*") == "$100"

def test_h():
    assert value("h").lower()     == "$20"

def test_not_Hello():
    assert value("Hello") or value("H").lower() != "$100"
