# User function Template for python3

class Solution:
    def find(self, idx, str, result):
        if idx == len(str) - 1:
            result.add("".join(str))
            return

        for i in range(idx, len(str)):
            str[idx], str[i] = str[i], str[idx]
            self.find(idx + 1, str, result)
            str[idx], str[i] = str[i], str[idx]

    def findPermutation(self, s):
        # Code here
        result = set()
        str = list(s)
        self.find(0, str, result)
        return list(result)

