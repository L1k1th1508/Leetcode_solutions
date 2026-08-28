class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        a=nums[::-1]
        total=sum(nums)
        result=[]
        val=0
        for i in a:
            val=val+i
            result.append(i)
            if val>total-val:
                break
                
        return result

        