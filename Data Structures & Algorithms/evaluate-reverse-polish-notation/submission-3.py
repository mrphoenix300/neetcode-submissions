import operator

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}

class Solution:
    def calculate(self, op_string: str, a: int, b: int) -> int:
        return int(ops[op_string](a, b))


    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in "+-*/":
                stack.append(int(tokens[i]))
            else:
                operator1 = tokens[i]
                b = stack.pop()
                a = stack.pop()
                stack.append(self.calculate(operator1, a, b))
        
        return stack[-1]

            

        