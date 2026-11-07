from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def hashWord(word):

            arr = [0]*26
            for ch in word:
                idx = ord(ch) - 97
                arr[idx]+=1
            return str(arr)

        d = defaultdict(list)

        for s in strs:

            key = hashWord(s)
            d[key].append(s)

        return list(d.values())
        