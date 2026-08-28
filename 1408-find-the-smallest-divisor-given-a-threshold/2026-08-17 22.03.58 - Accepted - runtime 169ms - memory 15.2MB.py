class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        def summation(mid):
            s=0
            for i in nums:
                if i%mid==0 and mid!=0:
                    s=s+(i//mid)
                else:
                    s=s+((i//mid)+1)
            if s==threshold:
                return 0

            if s>threshold:
                return 1
            else:
                return -1
            
        
        i=1
        j=max(nums)
        while i <=j:
            mid=(i+j)//2
            a=summation(mid)
            if a==1:
                i=mid+1
            else:
                j=mid-1
        return i

            

        