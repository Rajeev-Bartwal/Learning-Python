a = 10  #global var


def change():

    globals()['a'] = 77   #local var
    
    print("inside ",a)

change()

print("outside ",a)
