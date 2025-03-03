import pytest
from square import square_num

def test_square_name():
    assert square_num(6) == 36
    assert square_num(7) == 49
    assert square_num(9) == 81
    assert square_num(4) == 16
    assert square_num(0) == 0
    assert square_num(-3) == 9