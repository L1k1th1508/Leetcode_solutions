class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsum=nums[0]
        start=0
        subarraysum=0
        k=-1
        j=-1
        for i in range(len(nums)):

            if subarraysum<0:
                
                subarraysum=0
                start=i
            
            subarraysum=subarraysum+nums[i]
            if subarraysum>maxsum:
                maxsum=subarraysum
                k=start
                j=i
            
        return maxsum
    

            



        