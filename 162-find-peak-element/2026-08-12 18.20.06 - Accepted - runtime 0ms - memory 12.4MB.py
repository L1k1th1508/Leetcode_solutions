class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        j=len(nums)-1
        while i < j:
            mid=(i+j)//2
            if nums[mid]>nums[j]:
                j=j-1
            elif nums[mid]<nums[j]:
                i=i+1
            else:
                j=j-1
        return j