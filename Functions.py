import math


def sum(a,b):
    return a+b

sum = sum(2,3)
print(sum)

def sqrt(num) :

    low = 0
    high = num
    while low < high :
        mid = (low+high)//2

        if mid * mid == num :
            return mid
        elif mid * mid > num :
            high = mid - 1
        else:
            low = mid + 1

    return high
 
print(sqrt(144))
print(math.sqrt(144))