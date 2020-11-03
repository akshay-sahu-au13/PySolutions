## https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ##### TLE ####
        # pr = []
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         profit = prices[j] - prices[i]
        #         if profit > 0:
        #             pr.append(profit)
        # # print(pr)
        # return max(pr) if pr else 0
        res = 0
        Max = 0
        for i in range(len(prices)-1,-1,-1):
            Max = max(Max,prices[i])
            res = max(res, Max-prices[i])
        return res
            
                
            