import heapq
class Solution(object):
    def minDifference(self, nums):
        heapq.heapify(nums)
        small=heapq.nsmallest(4,nums)
        large=heapq.nlargest(4,nums)
        large.reverse()
        return min(x-y for x , y in zip(large,small))
        




        """
        :type nums: List[int]
        :rtype: int
        """

        