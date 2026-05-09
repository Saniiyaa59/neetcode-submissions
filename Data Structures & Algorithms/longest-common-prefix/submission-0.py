class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        #compare each char of prefix to strs[i]
        def compare(p, curr):
            length = min(len(p), len(curr))
            res = ""
            for i in range (length):
                if(p[i] == curr[i]):
                    res+=p[i]
                else:
                    return res
            return res


        prefix = strs[0]
        i = 1
        while(i < len(strs)):
            prefix = compare(prefix, strs[i])
            i+=1
        return prefix
        