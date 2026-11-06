class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        min_cost=[]
        
        for i in range(len(cost)+1):
            min_cost.append(0)
        n=len(min_cost)
        for j in range(2,len(cost)+1):
            min_cost[j]=min(min_cost[j-1]+cost[j-1],min_cost[j-2]+cost[j-2])
            
        return min_cost[n-1]



        