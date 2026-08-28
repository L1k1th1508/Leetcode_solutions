class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length=len(nums)
        count=1
        if len(nums)==1:
            return True
        
        nums.extend(nums)
        


        for i in range(1,2*length):
            if nums[(i-1)%length]<=nums[i%length]:
                count=count+1
            else:
                count=1
            if count==length:
                return True
            else:
                continue
        return False
        
            


        
        