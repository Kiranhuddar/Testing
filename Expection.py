Itemsincart = 0
# if Itemsincart != 2:
#     raise Exception('products cart count not matching')
#
# if Itemsincart != 2:
#     pass

#assert (Itemsincart == 2)

try :
    with open('text.txt','r')as file:
        print(file.read())

except Exception as e:
    print(e)

finally:
    print('cleaning up resource')


