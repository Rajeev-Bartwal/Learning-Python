class Computer:

    #this is a class variable
    brand = "Bartwal"


    # init is used to initialize the variables of fields of a class
    # get called automatically when the object is created.
    # When you want to work with the instance variable then use instance method's
    def __init__(self, cpu, name, ram , ssd):
        self.cpu = cpu
        self.name = name
        self.ram = ram
        self.ssd = ssd


    #Instance method
    # When you want to work with the instance variable then use instance method's
    def config(self):
        print(self.name , " config with -:" ,  self.cpu , self.ram , self.ssd)


    #class method should accept a cls argument and always have a @classmethod decorator on top of it
    #When you want to work with the class var then use class method's
    @classmethod
    def info(cls):
        print(cls.brand)



    #static methods
    #when you want a  function that is not linked with any type of variable class or instance
    #it's like a utility method for some work/proccessing but not with the class or instance variables
    @staticmethod
    def show():
        print('in static show')

    @staticmethod
    def gb_to_bytes(gb):
        return gb * (1024 ** 3)

com = Computer("i5" , 'ASUS' , '16GB' , '512GB')
com1 = Computer("i7" , 'Lenovo' , '18GB' , '512GB')


com1.config()
com.config()

Computer.info()
print( "for obj 1" , Computer.gb_to_bytes(int(com.ram[0 : 2])))
print( "for obj 2" , Computer.gb_to_bytes(int(com1.ram[0 : 2])))


