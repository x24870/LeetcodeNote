# peek
# first try
class Solution:
    def cal_sub_exp(self, stack):
        cur_val = op = None
        if not isinstance(stack[-1], int):
            stack.append(0)
        while stack:
            item = stack.pop()
            if item == ')':
                if cur_val == None: cur_val = 0
                stack.append(cur_val)
                break
            elif cur_val == None:
                cur_val = item
            elif op == None:
                op = item
            else:
                if op == '+':
                    cur_val += item
                else: #op == '-'
                    cur_val -= item
                op = None

    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        s = list(s)
        stack = []
        dec = cur_val = 0
        while s:
            char = s.pop()
            # print(f'char: {char}')
            if char in '0123456789':
                cur_val += 10 ** dec * int(char)
                dec += 1
                if not s or s[-1] not in '0123456789':
                    # print(f'push val: {cur_val}')
                    stack.append(cur_val)
                    cur_val = dec = 0
            elif char in '+-)':
                stack.append(char)
            else: # char == (
                self.cal_sub_exp(stack)
            # print(stack)

        if len(stack) > 1:
            stack.insert(0, ')')
            # print(f'not empty: {stack} ')
            self.cal_sub_exp(stack)
        
        return stack[0]


# reference solution from: https://leetcode.com/problems/basic-calculator/solution/
# cleaner solution
# idea is same as previous solution
# reverse traversal the string
class Solution2:
    def evaluate_expr(self, stack):
        if stack and not isinstance(stack[-1], int):
            stack.append(0)

        res = stack.pop()
        # Evaluate the expression till we get corresponding ')'
        while stack and stack[-1] != ')':
            sign = stack.pop()
            if sign == '+':
                res += stack.pop()
            else:
                res -= stack.pop()
        return res

    def calculate(self, s: str) -> int:
        stack = []
        n, operand = 0, 0

        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            if ch.isdigit():
                # Forming the operand - in reverse order.
                operand = (10**n * int(ch)) + operand
                n += 1
            elif ch != " ":
                if n:
                    # Save the operand on the stack
                    # As we encounter some non-digit.
                    stack.append(operand)
                    n, operand = 0, 0
                if ch == '(':         
                    res = self.evaluate_expr(stack)
                    stack.pop() # pop ')'
                    # Append the evaluated result to the stack.
                    # This result could be of a sub-expression within the parenthesis.
                    stack.append(res)
                # For other non-digits just push onto the stack.
                else:
                    stack.append(ch)

        # Push the last operand to stack, if any.
        if n:
            stack.append(operand)

        # Evaluate any left overs in the stack.
        return self.evaluate_expr(stack)

# faster than solution 1 & 2 and more readable
# treat '-' operator as minus numbers
# for example '1 -2 + 3' --> '1 + (-2) + 3'
class Solution3:
    def calculate(self, s: str) -> int:
        stack = []
        operand = 0
        res = 0 # For the on-going result
        sign = 1 # 1 means positive, -1 means negative  

        for ch in s:
            if ch.isdigit():
                # Forming operand, since it could be more than one digit
                operand = (operand * 10) + int(ch)

            elif ch == '+':
                # Evaluate the expression to the left,
                # with result, sign, operand
                res += sign * operand

                # Save the recently encountered '+' sign
                sign = 1

                # Reset operand
                operand = 0

            elif ch == '-':
                res += sign * operand
                sign = -1
                operand = 0

            elif ch == '(':
                # Push the result and sign on to the stack, for later
                # We push the result first, then sign
                stack.append(res)
                stack.append(sign)

                # Reset operand and result, as if new evaluation begins for the new sub-expression
                sign = 1
                res = 0

            elif ch == ')':
                # Evaluate the expression to the left
                # with result, sign and operand
                res += sign * operand

                # ')' marks end of expression within a set of parenthesis
                # Its result is multiplied with sign on top of stack
                # as stack.pop() is the sign before the parenthesis
                res *= stack.pop() # stack pop 1, sign

                # Then add to the next operand on the top.
                # as stack.pop() is the result calculated before this parenthesis
                # (operand on stack) + (sign on stack * (result from parenthesis))
                res += stack.pop() # stack pop 2, operand

                # Reset the operand
                operand = 0

        return res + sign * operand

# s = '2-1+2'
# s = '1+1'
# s = '47'
s = '-2-1'
sol = Solution2()
ans = sol.calculate(s)
print(f'ans: {ans}')