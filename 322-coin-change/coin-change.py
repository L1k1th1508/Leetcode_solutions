class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp=[]
        for i in range(amount+1):
            dp.append(amount+1)
        dp[0]=0
        k=0
        for j in range(1,amount+1):
            
            for coin in coins:
                if coin<=j:
                    dp[j]=min(dp[j],(1+dp[j-coin]))
        
        if dp[amount]>amount:
            return -1
        else:
            return dp[amount]




            



        
            



        
