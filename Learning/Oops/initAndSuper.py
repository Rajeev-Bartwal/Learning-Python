class Animal:

    def __init__(self,name, color):
        print("animal init")
        self.name = name
        self.color = color

    def eat(self):
        print(self.name , "eat")

    def sleep(self):
        print(self.name ,"sleep")

class Dog(Animal):

    def __init__(self, name=None, color = None, breed = None):
        print("dog init")
        #this is if you want to give default values as none or any
        super().__init__(name if name is not None else 'default',
                         color if color is not None else 'red')


        #simple super calling init.
        super().__init__(name,color)
        self.breed = breed

    def details(self):
        print("details : " ,self.name, 'is a', self.breed ,'with color', self.color  )


obj1 = Dog ("Julian", 'black', 'Labrador')
obj = Dog(breed='wild')

obj1.details()
obj.details()