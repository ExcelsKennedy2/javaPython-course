class Fruits:
    # constructor method
    def __init__(self, name, price, color):
        self.name = name
        self.price = price
        self.color = color


        # normal method
    def display(self):
        print(f'I like eating {self.name}, it costs {self.price} '
              f'and it is {self.color} in color')

# instance of a class

myobj = Fruits('Banana', 20, 'yellow')
myobj.display()
myobj2 = Fruits("Watermelon", 50, "Red")
myobj2.display()