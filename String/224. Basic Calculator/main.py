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

# s = '2-1+2'
# s = '1+1'
# s = '47'
s = '-2-1'
sol = Solution()
ans = sol.calculate(s)
print(f'ans: {ans}')

