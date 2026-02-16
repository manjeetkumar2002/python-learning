# BRUTE FORCE
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxi = 0

        for i in range(len(nums)):
            zeros = 0
            for j in range(i, len(nums)):
                if (nums[j] == 0):
                    zeros += 1
                if (zeros > k):
                    break

                maxi = max(maxi, j - i + 1)

        return maxi


#better
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxi = 0
        left = 0
        right = 0
        zeros = 0
        while right < len(nums):
            if nums[right] == 0:
                zeros += 1

            if zeros > k:
                while zeros != k:
                    if nums[left] == 0:
                        zeros -= 1
                    left += 1

            maxi = max(maxi, right - left + 1)
            right += 1

        return maxi


#optimal
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxi = 0
        left = 0
        right = 0
        zeros = 0
        while right < len(nums):
            if nums[right] == 0:
                zeros += 1

            if zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            if zeros <= k:
                maxi = max(maxi, right - left + 1)
            right += 1

        return maxi