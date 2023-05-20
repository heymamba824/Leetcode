class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        mapping = ['+','-','*','/']
        stack = []
        for i in tokens:
            if i == "+":
                second = int(stack.pop())
                first = int(stack.pop())
                stack.append(second + first)
            elif i == '-':
                second = int(stack.pop())
                first = int(stack.pop())
                stack.append(first - second)
            elif i == '*':
                second = int(stack.pop())
                first = int(stack.pop())
                stack.append(second * first)
            elif i == '/':
                second = int(stack.pop())
                first = int(stack.pop())
                stack.append(int(first/second))
            else:
                stack.append(i)
        return int(stack.pop())