class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(len(nums)):
            if i==len(nums)-1:
                return (nums[i]-1)*(nums[i-1]-1)
        