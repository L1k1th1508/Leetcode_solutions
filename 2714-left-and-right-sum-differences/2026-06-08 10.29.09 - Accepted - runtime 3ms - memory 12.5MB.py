class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total=sum(nums)
        left=0
        result=[]
        for i in nums:
            total=total-i
            result.append(abs(left-total))
            left=left+i
        return result

        
        