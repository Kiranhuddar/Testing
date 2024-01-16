import pytest


@pytest.mark.usefixtures("setup")
class Testexample:

    def test_fixtureDemo(self):
        print("i will be excuting first")

    def test_fixtureDemo1(self):
        print("i will be excuting first")

    def test_fixtureDemo2(self):
        print("i will be excuting first")

    def test_fixtureDemo3(self):
        print("i will be excuting first")