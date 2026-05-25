class ABC:

    def __init__(self):
        print("init called")

    def __new__(cls):
        print("constructor called")
        return super().__new__(cls)


    def show(self):
        print("in show")

obj = ABC()
obj.show()

obj1 = ABC.__new__(ABC)
obj1.show()