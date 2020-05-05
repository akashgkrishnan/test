from oops1 import Person

class newPerson(Person):
    def __init__(self, name, age, roll, gender):
        self.gender = gender
        Person.__init__(self, name=name, age=age, roll=roll)

    def __str__(self):
        return f' {self.name}, {self.roll}, {self.age} {self.gender}'


new = newPerson(name='newAkash', age=24, roll=2, gender='male')
print(new)