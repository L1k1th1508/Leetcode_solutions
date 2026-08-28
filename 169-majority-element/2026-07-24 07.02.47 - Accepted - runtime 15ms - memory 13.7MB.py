class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic={}
        nums.sort()
        for num in set(nums):
            dic[num]=0
        for num in nums:
            dic[num]=dic[num]+1   
        maxi=max(dic,key=dic.get)
        return maxi

        