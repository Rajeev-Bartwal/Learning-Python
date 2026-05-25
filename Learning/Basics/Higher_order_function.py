
def square(n):
    return n * n

def cube(n):
    return n * n * n

def operate(num, operator_func):   #operate is a higher order function where it is accepting a func as a parameter
    return operator_func(num)


def operate1(nums, operator_func):   #operate1 is a higher order function where it is accepting a func as a parameter
    ans = []
    for i in nums:
        ans.append(operator_func(i))

    print(ans)


value = 6
nums = [1, 2, 3, 4, 5]

result = operate(value , cube)
print(result)

operate1(nums, cube)
