arr = [2,5,8,4,1,7,9]

def bubbleSort(arr):
    for i in range (len(arr)-1):
        for j in range (len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]



print(arr)
bubbleSort(arr)
print(arr)