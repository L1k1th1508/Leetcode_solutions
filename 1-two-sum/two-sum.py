class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic={}
        
        for i in range(len(nums)):
            a=target-nums[i]
            if a in dic:
                
                return [dic[a],i]
                
            else:
                dic[nums[i]]=i
            
            

        