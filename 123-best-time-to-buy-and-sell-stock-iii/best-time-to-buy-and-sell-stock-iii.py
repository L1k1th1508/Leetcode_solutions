class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy1=float("inf")
        sell1=0
        buy2=float("inf")
        sell2=0
        for i in prices:
            if i < buy1:
                buy1=i
            if i-buy1>sell1:
                sell1=i-buy1
            if i-sell1<buy2:
                buy2=i-sell1
            if i-buy2>sell2:
                sell2=i-buy2
        return sell2

            


        