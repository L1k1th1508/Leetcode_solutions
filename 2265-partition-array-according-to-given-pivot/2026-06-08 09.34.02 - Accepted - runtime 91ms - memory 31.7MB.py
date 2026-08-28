class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        less=[]
        equal=[]
        more=[]
        i=0
        
        for i in range(len(nums)):
            if nums[i]<pivot:
                
                less.append(nums[i])
            elif nums[i]>pivot:
                more.append(nums[i])
            else:
                equal.append(nums[i])
        return less+equal+more

            
        


        