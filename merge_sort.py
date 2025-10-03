numbers = input("Enter a list of numbers separated by space: ")
numbers_list = numbers.split(" ")

for idx in range(len(numbers_list)):
    numbers_list[idx] = int(numbers_list[idx])

def merge(arr,lb1,ub1,lb2,ub2):
    temp  = []
    i = lb1
    j = lb2
    while i <=ub1 and j <=ub2:
        if arr[i] <=arr[j]:
            temp.append(arr[i])
            i+=1
        elif arr[i] > arr[j]:
            temp.append(arr[j])
            j+=1
    while i <=ub1:
        temp.append(arr[i])
        i += 1
    while j <=ub2:
        temp.append(arr[j])
        j += 1

    k = 0
    for i in range(lb1,ub2+1) :
        arr[i] = temp[k]
        k += 1


def merge_sort(arr,left,right):
    if left < right:
        # divide
        mid = (left + right) // 2
        merge_sort(arr,left,mid)
        merge_sort(arr,mid+1,right)
        # merge
        merge(arr,left,mid,mid+1,right)


merge_sort(numbers_list,0,len(numbers_list)-1)
print(numbers_list)