class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b_value=prices[0]
        max_profit=0
        for i in prices:
            max_profit=max(max_profit,i-b_value)
            #print(max_profit)
            b_value=min(b_value,i)
        return max_profit
        
