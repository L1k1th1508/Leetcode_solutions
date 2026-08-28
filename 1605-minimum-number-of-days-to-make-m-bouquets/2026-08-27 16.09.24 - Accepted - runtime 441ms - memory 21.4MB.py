class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        def minimum_count(bloomDay,mid,m,k):
            bouquet_count=0
            contiguous=0
            for num in bloomDay:
                if num<=mid:
                    contiguous=contiguous+1
                    if contiguous==k:
                        bouquet_count=bouquet_count+1
                        contiguous=0
                else:
                    contiguous=0
            return bouquet_count >= m
        if len(bloomDay)<m*k:
            return -1
        i=min(bloomDay)
        j=max(bloomDay)
        ans=0
        while i <= j:
            mid=(i+j)//2
            a=minimum_count(bloomDay,mid,m,k)
            
            if a==True:
                ans=mid
                j=mid-1
            
            else:
                i=mid+1
            print(ans)
        return ans



        
            
        
        
        