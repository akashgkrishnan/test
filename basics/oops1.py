class calculator:
    num = 100

    def getData(self):
        print('i am a method')

c = calculator()
c.getData()
print(c.num)

class Species:
    def __init__(self):
        return 'name'


class Person:
    species = 'Human'
    def __init__(self, name, roll, age):
        self.name = name
        self.roll = roll
        self.age = age

    def getage(self):
        return  self.age

    def getroll(self):
        return self.roll

    def getname(self):
        return self.name

    def __str__(self):
        return f'''my name is {self.name} \n My roll is {self.roll} \n I am {self.age} years old 
            i am {Person.species}'''

akash = Person(name='Akash',roll=10, age=17)

print(akash)

print('my age is' , akash.getage())
