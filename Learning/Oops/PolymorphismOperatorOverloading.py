from typing import overload


class Vehical:

    def __init__(self,typeOfVehicle):
        self.typeOfVehicle = typeOfVehicle

#----------overloading in python is traditional not like java.---------

#   <------ overloading based on  the car color-------->

    def start(self, color=None):
        if color:
            print(color , self.typeOfVehicle ,"is starting")
        else :
            print(self.typeOfVehicle ,"is starting")


#   <------ overloading based on  the car color-------->


    def stop(self , color=None):
        if color:
            print(color , self.typeOfVehicle ,"is stopping")
        else:
            print(self.typeOfVehicle ,"stopping")




class Car(Vehical):

    def __init__(self , color, wheels , typeOfVehicle):
        super().__init__(typeOfVehicle)
        self.color = color
        self.wheels = wheels

    def details(self):
        print("details : " , self.typeOfVehicle, 'has a', self.wheels ,'wheels with color', self.color  )


#obj of car
obj  = Car('black' , 4 , 'car')

#overloading based on  the car color is given in param.
obj.start()
obj.start('black')


obj.details()

#overloading based on  the car color is given in param.
obj.stop()
obj.stop('blue')
