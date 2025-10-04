def partition(nums, low, high):
    pivot = nums[low]
    i = low
    j = high
    while i < j:
        while nums[i] <= pivot  and i <= high - 1 :
            i+=1
        while nums[j] > pivot and j >= low + 1:
            j-=1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]

    #place the pivot to right position
    nums[low], nums[j] = nums[j], nums[low]
    return j

def quickSort(nums, low, high):
    if low < high:
        p = partition(nums, low, high)
        quickSort(nums, low, p - 1)
        quickSort(nums, p + 1, high)


arr = [3,4,5,1,5,6,7,0]
quickSort(arr,0,len(arr)-1)
print(arr)