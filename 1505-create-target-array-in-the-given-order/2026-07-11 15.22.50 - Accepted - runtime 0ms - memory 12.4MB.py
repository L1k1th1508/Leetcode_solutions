class Solution(object):
    def createTargetArray(self, nums, index):

        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        target=[]
        i=0
        j=0
        while i<len(index) and j <len(nums):
            target.insert(index[i],nums[j])
            i=i+1
            j=j+1
        return target

        
    