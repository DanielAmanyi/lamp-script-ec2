import pytest
from twttr import shorten


def test_shorten():
    assert shorten("hello") == "hll"

def test_capson():
    assert shorten("HELLO WORLD") == "HLL WRLD"

def test_camel_case():
    assert shorten("HEllo wOrlD") == "Hll wrlD"

def test_int():
    assert shorten("1") == "1"
    assert shorten("daniel-1") == "dnl-1"


# def main():
#     test_shorten()
#     test_capson()
#     test_camel_case()

# if __name__ == __main__:
#     main()
