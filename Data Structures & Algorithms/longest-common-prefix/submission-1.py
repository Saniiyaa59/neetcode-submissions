class TrieNode:
    def __init__(self):
        self.children = {} #ch -> TrieNode

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, s):
        curr = self.root
        for ch in s:
            if not ch in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]

    def compare(self, s):
        curr = self.root
        for i in range(len(s)):
            ch = s[i]
            if not ch in curr.children:
                return i
            curr = curr.children[ch]
        return len(s)
        

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        trie = Trie()
        trie.add(strs[0])

        p = len(strs[0])

        for i in range (1, len(strs)):
            p = min(p, trie.compare(strs[i]))
            if p == 0:
                return ""

        return strs[0][:p]

        



        