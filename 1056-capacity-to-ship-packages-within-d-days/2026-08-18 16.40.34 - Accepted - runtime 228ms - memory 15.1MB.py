class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        def best(capacity):
            indi_count=0
            count=1
            for i in weights:
                if indi_count+i>capacity:
                    count=count+1
                    indi_count=0
                indi_count=indi_count+i
            return count<=days
        i=max(weights)
        j=sum(weights)
        while i < j:
            mid=(i+j)//2
            
            if best(mid):
                j=mid
            else:
                i=mid+1
        return i




            
            
        
            
        
        
            
        


        