class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi=0
        count=0
        for num in nums:
            if num==1:
                count=count+1
            elif num==0:
                if maxi<count:
                    maxi=count
                count=0
        if maxi>count:
            return maxi
        else:
            return count
            
            
        