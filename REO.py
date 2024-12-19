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

file = open('Me.txt','r')
for x in file:
    print(x.strip())
