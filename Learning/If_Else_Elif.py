x = int(input())

if x % 2 == 0:
    print("Even")
elif x % 2 == 1:
    print("Odd")
else:
    print("not valid")



# match in python or switch in other language

match x :
    case 1:
        print("one")
    case  2:
        print("two")
    case  3:
        print("three")
    case  4:
        print("four")
    case 5:
        print("five")
    case _:
        print("incorrect")

