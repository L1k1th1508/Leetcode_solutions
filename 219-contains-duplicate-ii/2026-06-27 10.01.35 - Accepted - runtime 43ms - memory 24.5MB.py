class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        result= set()
        for i,num in enumerate(nums):
            if num in result:
                return True
            result.add(num)
            if len(result)>k:
                result.remove(nums[i-k])
        return False

        