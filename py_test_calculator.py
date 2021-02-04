"""
PyTest framework for part 2
Command to run: python -m pytest py_test_calculator.py
"""

import pytest

def addition(a, b):
    return round(a + b, 2)

def subtraction(a, b):
    return round(a - b, 2)

def multiplication(a, b):
    return round(a * b, 2)

def division(a, b):
    return round(a / b, 2)

class TestCalculator:
    def test_addition(self):
        assert addition(2, 3) == 5

    def test_subtraction(self):
        assert subtraction(9, 3) == 6

    def test_multiplication(self):
        assert multiplication(4, 5) == 20

    def test_division(self):
        assert division(4, 2) == 2