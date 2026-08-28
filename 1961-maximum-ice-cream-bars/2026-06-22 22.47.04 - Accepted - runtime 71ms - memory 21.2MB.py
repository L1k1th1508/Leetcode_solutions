class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        if not costs:
            return 0
        m=max(costs)
        count=[0]*(m+1)
        for i in costs:
            count[i]=count[i]+1
        
        
        
        sums=0
        for j in range(m+1):
            if count[j]==0:
                continue
            while count[j]>0 and coins>=j:
                coins=coins-j
                sums=sums+1
                count[j]=count[j]-1
            if coins<j:
                break
        return sums

            
        
