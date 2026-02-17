class item:
    def __init__(self, val, wt):
        self.val = val
        self.wt = wt


class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        # code here
        n = len(wt)
        # sort he array on the basis on value/weight (1 unit value)
        arr = []
        for i in range(n):
            arr.append(item(val[i], wt[i]))

        arr.sort(key=lambda x: x.val / x.wt, reverse=True)

        i = 0
        ans = 0
        while capacity > 0 and i < n:
            if capacity >= arr[i].wt:
                ans += arr[i].val
                capacity -= arr[i].wt
            else:
                ans += (arr[i].val / arr[i].wt) * capacity
                capacity = 0
            i += 1

        return ans