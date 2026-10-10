class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        operator = {'+', '-', '*', '/'}

        for tok in tokens:

            if not tok in operator:
                stack.append(int(tok))
                continue

            else:
                if tok == '+':
                    stack.append(stack.pop() + stack.pop())
                elif tok == '-':
                    stack.append(-(stack.pop() - stack.pop()))
                elif tok == '*':
                    stack.append(stack.pop() * stack.pop())
                else:
                    f = stack.pop()
                    s = stack.pop()
                    stack.append(int(s / f))

        return stack[-1]

            

