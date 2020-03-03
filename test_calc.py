import pytest
from calc import add
from calc import raise_error
from calc import MyError
from calc import sqrt
from calc import csqrt


def test_add_value():
    assert add(1, 3) == 4


def test_add_wrong_value():
    assert add(1, 3) != 5


def test_add_wrong_type():
    with pytest.raises(TypeError):
        add(1, "3")


def test_raise_error():
    with pytest.raises(MyError) as excp_info:
        raise_error()
    assert "something went wrong" in str(excp_info.value)


def test_sqrt_correct_value():
    assert sqrt(4) == 2


def test_sqrt_negative_value():
    with pytest.raises(ValueError):
        sqrt(-1)


def test_sqrt_wrong_type():
    with pytest.raises(TypeError):
        sqrt("4")


def test_csqrt_negative():
    assert csqrt(-1) == 1j