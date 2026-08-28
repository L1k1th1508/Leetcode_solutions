class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count=0
        dic={0:1}
        sums=0
        for i in range(len(nums)):
            sums=sums+nums[i]
            a=sums-k
            if a in dic:
                count=count+dic[a]
            dic[sums]=dic.get(sums,0)+1
        return count

            
           

                

        
    

        
        
        
        



        