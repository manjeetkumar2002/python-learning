#brute force
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxi = 0
        n = len(fruits)
        for i in range(n):
            s = set()
            for j in range(i,n):
                s.add(fruits[j])
                if len(s)> 2:
                    break
                maxi = max(maxi,j-i+1)
        return maxi


#better
class Solution:
    def totalFruit(self, nums: List[int]) -> int:
        maxi = 0
        n = len(nums)
        left = 0
        right = 0
        my_dict = dict()
        while right<n:
            my_dict[nums[right]] = my_dict.get(nums[right], 0) + 1
            while len(my_dict) > 2:
                my_dict[nums[left]]-=1
                if my_dict[nums[left]] == 0:
                    del my_dict[nums[left]]
                left+=1

            if len(my_dict) <= 2:
                maxi = max(maxi , right-left+1)
            right+=1
        return maxi


class Solution:
    def totalFruit(self, nums: List[int]) -> int:
        maxi = 0
        n = len(nums)
        left = 0
        right = 0
        my_dict = dict()
        while right<n:
            my_dict[nums[right]] = my_dict.get(nums[right], 0) + 1
            if len(my_dict) > 2:
                my_dict[nums[left]]-=1
                if my_dict[nums[left]] == 0:
                    del my_dict[nums[left]]
                left+=1

            if len(my_dict) <= 2:
                maxi = max(maxi , right-left+1)
            right+=1
        return maxi