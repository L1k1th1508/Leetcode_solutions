class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        a=max(nums[0:len(nums)])
        b=min(nums[0:len(nums)])
        r=a-b
        result=r*k
        return result
        

       

        