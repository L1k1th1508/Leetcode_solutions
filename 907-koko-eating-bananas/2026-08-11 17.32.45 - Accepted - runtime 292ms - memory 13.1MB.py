class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def trys(piles,mid,h):
            s=0
            for k in range(len(piles)):
                if piles[k]%mid!=0:
                    s=s+((piles[k]//mid)+1)
                else:
                    s=s+(piles[k]//mid)
            if s<=h:
                return -1
            else:
                return 1
            
        piles.sort()
        i=1
        j=piles[-1]
        mid=(i+j)//2
        while i<=j:
            mid=(i+j)//2
            a=trys(piles,mid,h)
            if a==-1:
                j=mid-1
            else:
                i=mid+1
        return i
        

        
        


         







        


        