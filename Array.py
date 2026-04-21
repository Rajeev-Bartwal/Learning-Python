from array import *

# arr = array('i',[1,2,3,4,5,6,7,8,9])
# print(type(arr))
#
# arr1 = array(arr.typecode , arr.tolist())
# arr[2] = 67
# print(arr)
# print(arr1)

arr1 = array('i' ,)



for i in range(5):
    print(f"enter {i} th elements of array")
    arr1.append(int(input()))

print(arr1.tolist())