class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dup=0
        for i in range(1,len(nums)):
            if nums[dup]!=nums[i]:
                dup=dup+1
                nums[dup]=nums[i]

        return dup+1

          
        
        