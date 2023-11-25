greeting = 'good morning'
if greeting == 'good morning':
    {print('yes it is good')
     }
else:
    {print('Not matching')}

print('is else conditon satisfied')

#for loop
obj = [2, 3, 5, 7, 9]
for i in obj :
    print(i*2)
sum = 0
for i in range (1,6):
    sum += i
print(sum)

for m in range (10):
    print(m)

it = 10
# while it < 10:
#     print('i am genius')
#     it += 1

# while it >1:
#     if it == 3:
#         it =it -1
#         continue
#     if it ==9:
#         print(it)

#group of related statement that perform a specific task is called function
def kiran(name):
    print('good morning'+" "+ name)
    #Function calling
def add_interger(a,b):
    return a+b

kiran("rahul shetty ")

print(add_interger(5, 4))

#class is a blueprint
#sum,sub,multiplication,division,constant
#methods , class variables, instances variable
class calculator:
    num = 100

    def __init__(self,a,b):
        self.first_number = a
        self.second_number = b
        print('i am called automatically when object is created')

    def add(self,a,b):
        self.a = a
        self.b = b
        print('i am now executing as a method in class',self.a+self.b)

    def sub(self):
        return self.first_number -self.second_number+self.num

obj = calculator(2, 3) #syntax to create objects in python
obj.add(5,6,)
print(obj.num)

obj1 = calculator(9,5)
print(obj1.sub())










