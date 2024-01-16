import pytest


@pytest.fixture(scope='class')
def setup():
    print("i will be executed first")
    yield
    print("i will be executed last")

def test_fixtureDemo(setup):
    print("i will be execute steps in fixture demo method")

@pytest.fixture()
def dataload():
    print("user profile data is being created")
    return ["rahul","shetty","Pinogy.com"]

@pytest.fixture(params=[("chrome","kiran","Huddar"),("Firefox","kiran"),("IE","prabhakar")])
def crossBrowser(request):
    return request.param


