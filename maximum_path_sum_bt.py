# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = float("-inf")
    def solve(self,root):
        if root is None :
            return 0
        #leftsum
        left  = self.solve(root.left)
        if left< 0:
            left = 0
        #right sum
        right = self.solve(root.right)
        if right < 0:
            right = 0
        self.res = max(self.res,root.val+left+right)
        return root.val + max(left,right)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.solve(root)
        return self.res