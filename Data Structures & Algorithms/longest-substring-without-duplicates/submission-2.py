class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        r = 0
        d = set()
        res = 0

        while r < len(s):

            while s[r] in d:
                d.remove(s[l])
                l+=1
            d.add(s[r])
            res = max(res, r-l+1)
            r+=1

        return res
            


