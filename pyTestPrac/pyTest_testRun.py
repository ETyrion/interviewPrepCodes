import pytest


def test_method_one():
    print("I am in method one")

def test_method_two():
    print("I am in method 2")

@pytest.Mark.three
def test_method_three():
    print("Method 3")