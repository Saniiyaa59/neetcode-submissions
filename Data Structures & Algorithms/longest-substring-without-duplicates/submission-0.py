class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        r = 0
        d = set()
        maxLen = 0

        while r < len(s):

            while s[r] in d:
                d.remove(s[l])
                l+=1

            d.add(s[r])
            maxLen = max(maxLen, r-l+1)
            r+=1

        return maxLen

