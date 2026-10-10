class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        d = [0]*26
        l = 0
        r = 0
        most_freq = 0
        res = 0
        
        while r < len(s):

            d[ord(s[r])-65]+=1
            most_freq = max(most_freq, d[ord(s[r])-65])

            diff = (r-l+1) - most_freq

            while diff > k:
                d[ord(s[l])-65] -= 1
                l+=1
                most_freq = max(d)
                diff = (r-l+1) - most_freq

            res = max(res, r-l+1)
            r+=1

        return res




        