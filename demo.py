import  selenium
print('test')

a= [10, 20, 30, 40, 50]
l = ('a', 10, 'alas', 1.3)

print(l)


a.append((19))

print(a)

a.insert(3, 'akash')
print(a)


new = {
    'first': 'akash',
    'second':'Krishnan'
}



print(new)
print(new['first'])


new['common'] = 'testing automation'

print(new)

l = []
print(type(l))

l = [10,2.5,"hello", 10, [20,30]]

print(type(l))
print(l)

l = list()

print(type(l))
print(l)




def show(x,y): #non default argument
    print("x ", x)
    print("y ", y)

show(10,20) #positional argument

show(x = 'x', y = 'k') # keyword argument
#show(x =20, y = 30, z = 40)
# positonal arguments should be before keyword argument
show(10, y = 20)




D = {'A': 'APple', 'e101': 'Akash', 'chris': '10', 1.5 : 1000}
print(D)
D['e101'] = 'new'
D['CA'] = 78
print(D)


del D[1.5]
print(D)


print(D['A']) # if the key is in the dictionay then will return the  value else it will throw error

print(D.get('A','not found'))
print(D.get('B','not found'))