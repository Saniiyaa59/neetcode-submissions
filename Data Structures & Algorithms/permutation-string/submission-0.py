class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1):
            return False

        l = 0
        r = 0

        a1 = [0]*26
        a2 = [0]*26

        for ch in s1:
            a1[ord(ch)-97]+=1

        while r < len(s2):

            if r >= len(s1):
                a2[ord(s2[l])-97]-=1
                l+=1

            a2[ord(s2[r])-97]+=1
            if str(a1) == str(a2):
                return True
            r+=1


        return False
