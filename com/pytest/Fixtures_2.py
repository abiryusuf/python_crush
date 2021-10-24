import pytest

"""
@pytest.yield_fixture()
Execute specific method before and after every test method
"""

@pytest.yield_fixture()
def setup():
    print(" Once before every method")
    yield
    print(" Once After every method")

def testMethod_1(setup):
    print("This is test method 1")

def testMethod_2(setup):
    print("This is test method 2")
