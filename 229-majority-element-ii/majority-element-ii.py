class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic={}
        arr=[]
        n=len(nums)
        for num in nums:
            dic[num]=dic.get(num,0)+1
        for i in dic:
            if dic[i]>n/3:
                arr.append(i)
            
        return arr