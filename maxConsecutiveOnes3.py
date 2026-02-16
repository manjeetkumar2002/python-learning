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