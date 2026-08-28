class Solution(object):
    
            
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead
        """
        def move(nums,l,r):
            while l<r:
                nums[l],nums[r]=nums[r],nums[l]
                l=l+1
                r=r-1
        k=k%len(nums)
        
        move(nums,0,len(nums)-1)
        move(nums,0,k-1)
        move(nums,k,len(nums)-1)
        return nums
        
        

        
    
        
        
