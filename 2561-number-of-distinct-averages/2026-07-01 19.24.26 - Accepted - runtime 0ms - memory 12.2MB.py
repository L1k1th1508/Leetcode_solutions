class Solution(object):
    def distinctAverages(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        right=len(nums)-1
        nums.sort()
        result=[]
        
        while left<=right:
            average=nums[left]+nums[right]
            result.append(average)
            left=left+1
            right=right-1
        a=set(result)
        return len(a)

        