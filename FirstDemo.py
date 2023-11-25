print('hello')

#Here are the comments i have defined
a = 3
print(a)

str = 'Hello good morinng '
print(str)

b, c, d = 5, 6.4, 'great'
print()

print('{} {}'.format('value is',b))

values = [1, 2, 'rahul', 4, 5]

for i in range(len(values)) :
    print(values[3])

print(values[::])
values.insert(3,'sheety')
print(values)
values.append('kiran')
print(values)
values.insert(-2,'sushmita')
print(values)
values[2] = 'Rahul'
print(values)
del values[0]
print(values)

val = (1, 2, 'rahul', 4.50)

print(val[2])
#val[2] = 'Rahul'
print(val)

a = {1 :'first name', 2 : "Second name", 'age': "third name"}
print(a[1])
print(a.values())
print(a.keys())
print(a[2])
print(a['age'])

dict = {}
dict['first name '] = 'Rahul'
dict['last name'] = 'shetty'
print(dict)
dict['gender']='male'
print(dict)

a = 'Good morning'
print(a.title())

str = 'hello hi world'
str3 = 'hello'
if str3 in str:
    print('True')
else:
    print('kiran')

