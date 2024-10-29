# create a class called Person, with name,age,gender
# as the attributes. have a
# constructor method, a normal method and three objects

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def display(self):
        print(f'Your name is {self.name}, you are {self.age} and you are a {self.gender}.')

person1 = Person(name="Ashlynn", age=20, gender='female')
person2 = Person(name='Ben', age=16, gender='male')
person3 = Person(name='Gwen', age=16, gender='female')
person1.display()
person2.display()
person3.display()