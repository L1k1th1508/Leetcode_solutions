class Solution(object):
    def sortColors(self, nums):

        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
   
        left=0
        mid=0
        right=len(nums)-1
        while mid <=right:
            
            if nums[mid]==0:
                nums[left],nums[mid]=nums[mid],nums[left]
                left=left+1
                mid=mid+1
            elif nums[mid]==1:
                 mid=mid+1
            else:
                nums[right],nums[mid]=nums[mid],nums[right]
                right=right-1
            
