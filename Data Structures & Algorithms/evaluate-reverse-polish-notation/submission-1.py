class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operand = []

        for token in tokens:

            if token == "+":
                operand.append(operand.pop() + operand.pop())

            elif token == "-":
                f = operand.pop()
                s = operand.pop()
                operand.append(s - f)
            
            elif token == "*":
                operand.append(operand.pop() * operand.pop())

            elif token == "/":
                f = operand.pop()
                s = operand.pop()
                operand.append(int(s / f))
            
            else:
                operand.append(int(token))

        return operand.pop()

            

            
                    
            
            

