class Solution(object):
    def findMin(self, nums):

        """
        :type nums: List[int]
        :rtype: int
        """
        right=0
        left=len(nums)-1
        while(right<left):
            mid=(right+left)//2
            if nums[mid]>nums[left]:
                right=mid+1
            elif nums[mid]<nums[left]:
                left=mid
        return nums[right]
        
        
        
    

