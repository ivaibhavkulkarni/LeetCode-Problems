class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
    
        for token in tokens:
            if token in "+-*/":
                # Pop two operands from the stack
                b = stack.pop()
                a = stack.pop()
                
                # Perform the operation based on the operator
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # Truncate toward zero
                    if a * b < 0 and a % b != 0:
                        stack.append(a // b + 1)
                    else:
                        stack.append(a // b)
            else:
                # If it's a number, push it to the stack
                stack.append(int(token))
        
        # The result will be the only element in the stack
        return stack[0]