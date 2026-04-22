

nums = [1,2,4,2,30,6,4,3,2,24,57,4,]

result = list(filter(lambda n:n%3 == 0, nums))  #filter is an inbuilt func that work to filter the values you have to
# pass the 2 parameters , 1 function and 2 iterable or data_structures


print(result)