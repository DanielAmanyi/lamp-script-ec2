import pytest
from twttr import shorten


def test_shorten():
    assert shorten("hello") == "hll"

def test_capson():
    assert shorten("HELLO WORLD") == "HLL WRLD"

def test_camel_case():
    assert shorten("HEllo wOrlD") == "Hll WrlD"

def main():
    test_shorten()
    test_capson()
    test_camel_case()

if __name__ == __main__:
    main()
