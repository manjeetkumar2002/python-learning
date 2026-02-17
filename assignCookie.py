class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i = 0
        j = 0
        g.sort()
        s.sort()
        count  = 0
        while i < len(g) and j < len(s):
            # can i gave the cookie
            if s[j]>=g[i]:
                i+=1
                j+=1
                count+=1
            # when cokkie is small size than greed
            else:
                j+=1

        return count