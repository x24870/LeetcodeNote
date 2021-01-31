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


# refered solution: https://leetcode.com/problems/basic-calculator-ii/solution/
# idea: Use stack.
#       We don't need to consider parenthesses in this question
# faster than previous solution, but this solution not consider parenthesses
class Solution2:
    def calculate(self, s: str) -> int:
        stack = []
        cur_val = 0
        operator = '+'
        for char in s:
            print(char)
            if char == ' ':
                continue
            elif char.isdigit():
                cur_val = cur_val * 10 + int(char)
            else:
                if operator in '*/':
                    val = stack.pop()
                    if operator == '*':
                        val *= cur_val
                    else:
                        val = int(val / cur_val)
                    stack.append(val)
                else:
                    if operator == '-':
                        cur_val *= -1
                    stack.append(cur_val)

                operator = char
                cur_val = 0
            print(f'{stack}, {cur_val}, {operator}')

        # deal with last operator
        val = stack.pop() if stack else 0
        if operator == '+':
            val += cur_val
        elif operator == '-':
            val -= cur_val
        elif operator == '*':
            val *= cur_val
        else:
            val /= cur_val
            val = int(val)
        cur_val = 0
        stack.append(val)

        # sum up all valus in stack
        while stack:
            cur_val += stack.pop()
        return cur_val


# refered solution: https://leetcode.com/problems/basic-calculator-ii/solution/
# idea: the idea is same as previous solution but without stack
#       Use 'last_val' and 'result' to track values
class Solution3:
    def calculate(self, s: str) -> int:
        result = cur_val = last_val = 0
        operator = '+'
        for char in s:
            if char == ' ':
                continue
            elif char.isdigit():
                cur_val = cur_val * 10 + int(char)
            else:
                if operator in '+-':
                    result += last_val
                    if operator == '-': cur_val *= -1
                    last_val = cur_val
                elif operator == '*':
                    last_val *= cur_val
                else:
                    last_val = int(last_val / cur_val)
                cur_val = 0
                operator = char
        
        if operator == '+':
            last_val += cur_val
        elif operator == '-':
            last_val -= cur_val
        elif operator == '*':
            last_val *= cur_val
        else:
            last_val = int(last_val/cur_val)

        return result + last_val

# s = '3+21*2'
#s = '0'
# s = '1'
s = '14-3/2'
# s = '1*2-3/4+5*6-7*8+9/10'
sol = Solution3()
ans = sol.calculate(s)
print(f'ans: {ans}')