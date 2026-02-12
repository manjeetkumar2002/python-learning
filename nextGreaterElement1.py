class Solution:
    def nextLargerElement(self, arr):
        ans = [-1] * len(arr)
        stack = []

        for i in range(len(arr)):
            if len(stack) == 0:
                stack.append(i)
            else:
                while stack and arr[stack[-1]] < arr[i]:
                    ans[stack[-1]] = arr[i]
                    stack.pop()
                stack.append(i)

        return ans
