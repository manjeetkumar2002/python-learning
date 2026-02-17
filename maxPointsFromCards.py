class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        left_sum = 0
        right_sum = 0
        maxi = 0

        for i in range(0, k):
            left_sum += cardPoints[i]

        maxi = left_sum

        right_idx = n - 1
        for i in range(k - 1, -1, -1):
            right_sum += cardPoints[right_idx]
            left_sum -= cardPoints[i]
            right_idx -= 1
            maxi = max(maxi, right_sum + left_sum)

        return maxi


# leetcode 1423