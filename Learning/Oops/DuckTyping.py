#Duck Typing

# in python objects are determined by their behavior not by the type
#So if a class C expects an object with certain method like write. (or A obj.)
#Then any object wether A or B that implement that method can be used
# (or B also have same method so its obj can be also used in place of A's).



class A:     #Duck
    def write(self):
        print("A is writing")

class B:     #walk and quack like duck so  it is  a duck.
    def write(self):
        print("B is writing")


class C:
    def process(self , obj : A):
        obj.write()

obj = C()

#C needed the obj of A and it is working
obj.process(A())

#but because of duck typing it is working with the object of B as well
obj.process(B())
