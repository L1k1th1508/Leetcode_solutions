class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        M=max(nums)
        m=min(nums)
        dic=set(nums)
        a=[]
        for i in range(m,M+1):
            if i in dic:
                continue
            else:
                a.append(i)
        return a


        