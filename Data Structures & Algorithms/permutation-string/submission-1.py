class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        d1 = [0]*26
        for ch in s1:
            d1[ord(ch)-97]+=1

        key1 = str(d1)

        d2 = [0]*26

        l = 0
        r = 0

        while r < len(s2):

            d2[ord(s2[r])-97] += 1

            if r-l+1 == len(s1):
                key2 = str(d2)
                if key1 == key2:
                    return True
                d2[ord(s2[l])-97] -= 1
                l+=1

            r+=1

        return False