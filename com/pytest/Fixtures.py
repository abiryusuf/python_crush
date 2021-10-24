"""
How to work with PyTest Fixtures
Fixtures are function, which will run before each test function to
which it is applied.
@pytest.fixture()
Execute specific method before every test method

@pytest.yield_fixture()
Execute specific method before and after every test method

purpose: Fixtures are used to feed some data to the tests such as database connections,
URLs to test and some sort of input data. Therefore, instead of running the same code
for every test, we can attach fixture function to the tests and it will run
and return the data to the test before executing each test.
"""
import pytest
@pytest.fixture()
def setUp():
    print("Once before every Method")

def test_1(setUp):
    print("This is test_1")

def test_2(setUp):
    print("This is test_2")