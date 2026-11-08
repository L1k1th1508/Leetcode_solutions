class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit=0
        bought_price=prices[0]
        for i in range(1,len(prices)):
            if prices[i]<bought_price:
                bought_price=prices[i]
                
            else:
                profit=prices[i]-bought_price
                if profit>max_profit:
                    max_profit=profit
        return max_profit


       



        