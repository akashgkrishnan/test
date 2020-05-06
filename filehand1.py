file = open('test.txt')
print(file.read(2))

print(file.readline())
print(file.readlines())
print('1')
print(file.read(), 'new')
file.seek(0)
print('1')
print(file.readlines())
print(file.seek(3))
print(file.read())

file.close()

with open('test.txt', 'r') as file:
    new = file.readlines()
    reversed(new)
    with open('test.txt', 'w') as write:
        for line in reversed(new):
            write.write(line)


print('hi')

