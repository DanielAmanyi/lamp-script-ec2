import pytest
from bank import value


def test_value():
    assert value("Hello") == "$0"
    assert value("H")     == "$20"
    assert value("Hello") or value("H") != "$100"
