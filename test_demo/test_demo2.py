import pytest

@pytest.mark.smoke
def test_second_programme():
    msg = "hello"
    assert msg == 'hi',"Test failed becaused string not matched"

@pytest.mark.xfail
def test_creditcard():
    a = 4
    b = 8
    assert a+2 == 6,"addtion equal"


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])