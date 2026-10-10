class Solution:
    def isValid(self, s: str) -> bool:

        d = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []

        for i in range (len(s)):

            if not s[i] in d:
                stack.append(s[i])

            else:
                if len(stack) == 0 or stack[-1] != d[s[i]]:
                    return False
                stack.pop()

        return len(stack) == 0
