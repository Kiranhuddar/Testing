file = open('text.txt')
#read all contents of file
#read n number of character by passing parameter
#print(file.read(5))

#to read one single line at a time
#print(file.readlines())
line = file.readline()
while line != '':
    print(line)
    line=file.readline()


with open('text.txt','r')as reader:
    content = reader.readlines() #it will store in list formate
    reversed(content)
    with open('text.txt','w') as writer :
        for line in reversed(content):
            writer.write(line)





