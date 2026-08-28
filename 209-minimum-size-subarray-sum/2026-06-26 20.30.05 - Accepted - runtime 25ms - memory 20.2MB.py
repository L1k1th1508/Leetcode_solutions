class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        result=1000001
        mins=0
        i=0
        for j in range(len(nums)):
                mins=mins+nums[j]
                while mins>=target:
                    result=min(result,j-i+1)
                    mins=mins-nums[i]
                    i=i+1
        if result==1000001:
            return 0
            
        return result

        

        
             
            

            

                




        