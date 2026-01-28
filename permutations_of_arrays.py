class Solution:
    def find(self, idx, arr, result):
        if idx == len(arr) - 1:
            result.add(tuple(arr[:]))
            return

        for i in range(idx, len(arr)):
            arr[idx], arr[i] = arr[i], arr[idx]
            self.find(idx + 1, arr, result)
            arr[idx], arr[i] = arr[i], arr[idx]

    def uniquePerms(self, arr):
        # code here
        result = set()
        self.find(0, arr, result)
        return sorted(list(result))