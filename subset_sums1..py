class Solution:
    def solve(self, index, total, arr, result):
        if index >= len(arr):
            result.append(total)
            return

        sum = total + arr[index]
        self.solve(index + 1, sum, arr, result)
        sum = total
        self.solve(index + 1, sum, arr, result)

        def subsetSums(self, arr):
            # code here
            result = []
            self.solve(0, 0, arr, result)
            return result