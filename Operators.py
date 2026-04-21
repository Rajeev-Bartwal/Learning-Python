from unittest import case

def calcuate(x , y, z):

    operator = z

    match operator:
       case "+": return x + y
       case "-": return x - y
       case "*": return x * y

a = calcuate(2,3,"+")
print(a)