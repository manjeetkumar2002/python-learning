def partition(arr,low,high):
    pivot = arr[low]
    i = low
    j = high
    while i < j:
        while arr[i] <= pivot  and i <= high - 1 :
            i+=1
        while arr[j] > pivot and j >= low + 1:
            j-=1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    #place the pivot to right position
    arr[low], arr[j] = arr[j], arr[low]
    return j

def quickSort(arr,low,high):
    if low < high:
        p = partition(arr,low,high)
        quickSort(arr,low,p-1)
        quickSort(arr,p+1,high)


arr = [3,4,5,1,5,6,7,0]
quickSort(arr,0,len(arr)-1)
print(arr)