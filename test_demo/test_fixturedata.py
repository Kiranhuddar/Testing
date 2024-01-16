import pytest


@pytest.mark.usefixtures("dataload")
class testexample2:

    def editProfile(self,dataload):
        self.dataload = dataload
        print(dataload[0])
