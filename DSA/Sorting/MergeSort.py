arr = [2,5,8,4,1,7,9]

def mergeSort(arr , low , high ):

        if low >= high :
            return

        mid = (low + high) // 2

        mergeSort(arr , low , mid )
        mergeSort(arr , mid + 1 , high )
        merge(arr , low , mid, high )


def merge(arr , low , mid , high ):
    i = low
    j = mid+1
    n = len(arr)
    ans = []

    while i <= mid and j <= high:
        if arr[i] <= arr[j] :
           ans.append(arr[i])
           i += 1
        else :
            ans.append(arr[j])
            j += 1

    while i <= mid :
        ans.append(arr[i])
        i += 1

    while j <= high :
        ans.append(arr[j])
        j += 1

    for k in range(len(ans)):
        arr[low + k] = ans[k]

print(arr)
mergeSort(arr , 0 , (len(arr)-1))
print(arr)
