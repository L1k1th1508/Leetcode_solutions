class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        j=len(nums)-1
        if len(nums)==1:
            return nums[0]
        while(i <j and len(nums)>2):
            if nums[i]==nums[i+1] and nums[j]==nums[j-1]:
                i=i+2
                j=j-2
            else:
                if nums[i]!=nums[i+1]:
                    return nums[i]
                elif nums[j]!=nums[j-1]:
                    return nums[j]
        if i==j:
            return i