from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def hash(s):
            arr = [0]*26
            for ch in s:
                arr[ord(ch)-97] +=1
            return str(arr)

        d = defaultdict(list)
        for s in strs:
            key = hash(s)
            d[key].append(s)
        
        result = []
        for k in d:
            result.append(d[k])

        return result

