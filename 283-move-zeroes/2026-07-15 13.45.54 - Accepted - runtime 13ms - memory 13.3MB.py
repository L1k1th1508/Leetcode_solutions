class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        i=0
        j=1
        while i<j and j<len(nums):
            if len(nums)<3 and nums[i]!=0:
                return nums
            
            if nums[i]==0 and nums[j]==0:
                j=j+1
            elif nums[i]==0:
                nums[i],nums[j]=nums[j],nums[i]
                i=i+1
                j=j+1
            elif nums[j]==0 or (nums[i]!=0 and nums[j]!=0):
                i=i+1
                j=j+1
            
                
            
        return nums

            

                
        