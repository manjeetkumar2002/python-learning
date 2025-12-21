list = [1,2,3,2,3,1,4]

def unique(list):
    hash_dict = {}
    for i in range(len(list)):
        hash_dict[list[i]] = hash_dict.get(list[i],0) + 1

    for key ,value in hash_dict.items():
        if value == 1:
            return key

    return None

def unique_using_xor(list):
    ans = 0
    for i in range(len(list)):
        ans = ans ^ list[i]
    return ans
print(unique(list))
print(unique_using_xor(list))