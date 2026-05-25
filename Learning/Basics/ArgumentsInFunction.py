

def add(x=0,y=1):  #Default arguments
   return x+y

print(add(6,7))

def add(num , *num2):  #variable length args
   sum = num
   for arg in num2:
      sum += arg
   return sum

print(add(2,3,4))
print(add(6,7,4,5,2,2,3,2,4))

# Keyword args
def person(name,age):
   print('name ',name)
   print('age ',age)

#this is a bug
person(22,'rajeev')

#so we can pass keyword arguments

person(name = "Rajeev Bartwal" , age = 22)  #keyword args

#Variable length keyword args **kwargs
def person(**kwargs):
   for key, value in kwargs.items():
      print(key," : ",value)

person(name = "Rajeev Bartwal" , age = 22, location = "Gurugram" , address = "sector 40", pin = 675342) #this is how it works