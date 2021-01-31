# first try
# idea: transform to postfix then calculate the result
class Solution:
    def __init__(self):
        self.precedence = {'+':1, '-':1, '*':2, '/':2}

    def strnum_to_dec(self, s):
        cur_val = 0
        lst = []
        for char in s:
            if char == ' ':
                continue
            elif char.isdigit():
                cur_val = cur_val * 10 + int(char)
            else:
                lst.append(cur_val)
                lst.append(char)
                cur_val = 0

        if cur_val: lst.append(cur_val)
        return lst

    def cal_postfix(self, lst):
        stack = []
        if not lst: lst.append(0) # lst is empty
        for item in lst:
            if isinstance(item, int):
                stack.append(item)
            else:
                v1 = stack.pop()
                v2 = stack.pop() if stack else 0
                if item == '+':
                    v2 += v1
                elif item == '-':
                    v2 -= v1
                elif item == '*':
                    v2 *= v1
                elif item == '/':
                    v2 = v2 // v1
                stack.append(v2)
        return stack[0]

    def infix_to_postfix(self, lst):
        stack = []
        output = []
        for item in lst:
            # print(item)
            if isinstance(item, int):
                output.append(item)
            elif item == '(':
                stack.append(item)
            elif item == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                if stack: stack.pop() # pop '('
            else: # operator
                while stack and self.precedence[stack[-1]] >= self.precedence[item]:
                    output.append(stack.pop())
                stack.append(item)
            # print(f'{stack} {output}')

        while stack:
            output.append(stack.pop())

        return output

    def calculate(self, s: str) -> int:
        s = self.strnum_to_dec(s)
        # print(s)
        s = self.infix_to_postfix(s)
        # print(s)
        return self.cal_postfix(s)

s = '3+21*2'
# s = '0'
# s = '1-1+1'
sol = Solution()
ans = sol.calculate(s)
print(f'ans: {ans}')