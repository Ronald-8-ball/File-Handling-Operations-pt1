file = open('Me.txt','r')
print(file.read())
file.close()

file = open('Me.txt','r')
print(file.read(10))
file.close()

file = open('Me.txt','r')
print(file.readline())
file.close()

file = open('Me.txt','r')
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

with open('Me.txt','r') as file:
    file.readlines()
    for x in file:
        data = x.split()
        print(data)
file.close()





