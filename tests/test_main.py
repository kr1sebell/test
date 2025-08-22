"""Тесты для функции `hello`."""

from testproject import hello


def test_hello_default():
    assert hello() == "Привет, мир!"


def test_hello_custom():
    assert hello("Алиса") == "Привет, Алиса!"
