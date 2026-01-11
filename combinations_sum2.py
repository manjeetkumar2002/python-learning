class Solution:
    def solve(self,index,total,subset,result,target,nums):
        if total == target:
            result.append(subset.copy())
            return
        if total > target:
            return
        if index >= len(nums):
            return

        subset.append(nums[index])
        sum = total + nums[index]
        # pick the same element
        self.solve(index+1,sum,subset,result,target,nums)
        # not pick this element
        sum = total
        subset.pop()
        # Skip current element and all duplicates
        while index + 1 < len(nums) and nums[index] == nums[index + 1]:
            index += 1
        self.solve(index+1,sum,subset,result,target,nums)
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        self.solve(0,0,[],result,target,candidates)
        return result