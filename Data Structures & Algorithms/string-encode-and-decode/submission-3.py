class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "*"
            res+=s
            
        return res


    def decode(self, s: str) -> List[str]:

        res = []
        l = 0
        while l < len(s):

            dig = ""
            while  l < len(s) and s[l] >= "0" and s[l] <= "9":
                dig+=s[l]
                l+=1

            l+=1 #skip *
            d = int(dig)
            stop = l+d
            
            temp = ""
            while l < stop:
                temp += s[l]
                l+=1

            res.append(temp)

        return res





        return res
