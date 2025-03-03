import pytest
from hello import hello_world

def test_hello_word():
    assert hello_world() == "Hello, world"
    