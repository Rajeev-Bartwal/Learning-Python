class Computer:

    # init is used to initialize the variables of fields of a class
    # get called automatically when the object is created.
    def __init__(self, cpu, name, ram , ssd):
        self.cpu = cpu
        self.name = name
        self.ram = ram
        self.ssd = ssd


    def __new__(cls, *args, **kwargs):
        print("in new")
        return super().__new__(cls)

    def config(self):
        print(self.name , " config with -:" ,  self.cpu , self.ram , self.ssd)



com = Computer("i5" , 'ASUS' , '16GB' , '512GB')
com1 = Computer("i7" , 'Lenovo' , '18GB' , '512GB')


com1.config()
com.config()

