n = 5
fact = 1
while n > 0:
    fact *= n
    n = n - 1

print(fact)

def factorial(x):
   if x <= 1:
       return 1

   return x * factorial(x-1)

print(factorial(5))