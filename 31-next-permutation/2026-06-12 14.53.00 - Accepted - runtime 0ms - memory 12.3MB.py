class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pivot =-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                pivot=i
                break
        if pivot!=-1:
            for j in range(len(nums)-1,pivot,-1):
                if nums[j]>nums[pivot]:
                    nums[j],nums[pivot]=nums[pivot],nums[j]
                    break
                                                
        nums[pivot+1:]=nums[pivot+1:][::-1]

