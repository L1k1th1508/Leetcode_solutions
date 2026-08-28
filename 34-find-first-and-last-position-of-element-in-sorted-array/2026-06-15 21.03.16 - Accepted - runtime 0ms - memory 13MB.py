class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m=-1
        M=-1
        i=0
        j=len(nums)-1
        while(i<=j):
            mid=(i+j)//2
            if nums[mid]==target:
                m=mid
                break
            elif nums[mid]<target:
                i=mid+1
            elif nums[mid]>target:
                j=mid-1
        
        if m!=-1:
            while m>0 and nums[m-1]==target:
                m=m-1

            M=m
            while M<len(nums)-1 and nums[M+1]==target:
                M=M+1
        
            
        return [m,M]

        