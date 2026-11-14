class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        min_sum=float("inf")
        for i in range(len(nums)):
            start=i+l-1
            end=min(len(nums),i+r)
            for j in range(start,end):
                in_sum=sum(nums[i:j+1])
                if in_sum<=0:
                    continue
                else:
                    min_sum=min(min_sum,in_sum)
                    
                
        if min_sum<=0 or min_sum==float("inf"):
            return -1
        else:
            return min_sum

        