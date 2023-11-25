from loops import calculator

class childclass(calculator):
    num2 = 200

    def __init__(self):
        calculator.__init__(self,2,10)

    def getcompletedata(self):
        return self.num2+self.num+self.first_number+self.second_number+self.sub()


obj2 = childclass()
print(obj2.getcompletedata())

