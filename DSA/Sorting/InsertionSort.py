arr = [2,5,3,7,9,1,8,2]

def insertionSort(arr):

    n = len(arr)
    for i in range (n):
        j = i
        while j > 0 :
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1] , arr[j]

            j -= 1


print(arr)
insertionSort(arr)
print(arr)
