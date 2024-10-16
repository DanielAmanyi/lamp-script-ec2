import pytest
from twttr import shorten


def test_shorten():
    assert "hello" == "hll"

def test_capson():
    assert "HELLO WORLD" == "HELLO WORLD"

def test_camel_case():
    assert "HEllo wOrlD" == "Hello World"
