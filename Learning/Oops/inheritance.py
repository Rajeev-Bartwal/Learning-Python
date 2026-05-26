class animal:

    def __init__(self,name, color):
        self.name = name
        self.color = color

    def eat(self):
        print(self.name , "eat")

    def sleep(self):
        print(self.name ,"sleep")

class dog(animal):

    def __init__(self, name, color,breed):
        super().__init__(name, color)
        self.breed = breed

    def details(self):
        print("details" , self.breed , self.color , self.name )


# obj1 = dog ("Julian", 'black', 'Labrador')
# obj1.eat()
# obj1.sleep()
# obj1.details()


class father:
    def love(self):
        print("fathers love")

class mother:
    def love(self):
        print("mothers love")

class child (father,mother):
    def __init__(self, name):
        self.name = name

    def love(self):
        super().love()


obj = child("rajeev")

#it will call mothers love using the child obj.
mother.love(obj)

#it will call fathers cause of MRO. Method resolution order
obj.love()
