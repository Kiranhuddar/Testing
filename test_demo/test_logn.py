import pytest


def test_first(setup):
    print("hello world")
@pytest.mark.smoke
@pytest.mark.skip
def test_creditcard(setup):
    print("how are you ?")