import pytest
from twttr import shorten


def test_shorten():
    assert shorten("hello") == "hll"


def test_capson():
    assert shorten("HELLO WORLD") == "HELLO WORLD"

def test_camel_case():
    assert shorten("HEllo wOrlD") == "Hello World"
