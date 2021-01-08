#peek
#buttom up
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        max_amount = amount + 1
        amount_lst = [max_amount] * max_amount
        amount_lst[0] = 0 # no coin in list

        for i in range(1, max_amount):
            for c in coins:
                if c <= i:
                    amount_lst[i] = min(amount_lst[i], amount_lst[i-c] + 1)

        return amount_lst[amount] if amount_lst[amount] < max_amount else -1

#top down
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        max_amount = amount + 1
        amount_lst = [0] * max_amount

        def search_amount_lst(amount, lst):
            if amount < 0: return -1
            if amount == 0: return 0
            if lst[amount] != 0: return lst[amount]
            minumun = max_amount
            for c in coins:
                ret = search_amount_lst(amount-c, lst)
                if ret >= 0 and ret < minumun:
                    minumun = ret + 1
            
            lst[amount] = -1 if minumun == max_amount else minumun
            return lst[amount]
                
        return search_amount_lst(amount, amount_lst)