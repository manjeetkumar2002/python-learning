# class Solution:
#     def solve(self,index,total,subset,result,target,nums):
#         if total == target:
#             result.append(subset.copy())
#             return
#         if total > target:
#             return
#         if index >= len(nums):
#             return
#
#         subset.append(nums[index])
#         sum = total + nums[index]
#         # pick the same element
#         self.solve(index+1,sum,subset,result,target,nums)
#         # not pick this element
#         sum = total
#         subset.pop()
#         # Skip current element and all duplicates
#         while index + 1 < len(nums) and nums[index] == nums[index + 1]:
#             index += 1
#         self.solve(index+1,sum,subset,result,target,nums)
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         candidates.sort()
#         result = []
#         self.solve(0,0,[],result,target,candidates)
#         return result


class Solution:
    def solve(self,index,total,subset,result,nums):
        if total == 0:
            result.add(tuple(subset.copy()))
            return
        if total <0:
            return
        if index >= len(nums):
            return

        for i in range(index,len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            subset.append(nums[i])
            sum = total - nums[i]
            self.solve(i+1,sum,subset,result,nums)
            subset.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = set()
        self.solve(0,target,[],result,candidates)
        return [list(x) for x in result]
