arr = [2,5,3,7,9,1,8,2]

def selectionSort(arr):
    for i in range (len(arr)-1):
        min_index = i
        for j in range ( i+1 ,len(arr)):
            if arr[j] < arr[min_index]:
                arr[min_index],arr[j] = arr[j],arr[min_index]

print(arr)
selectionSort(arr)
print(arr)