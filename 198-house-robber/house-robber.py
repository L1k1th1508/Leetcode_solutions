class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_map={}
        def recursive(n):
            if n >=len(nums):
                return 0
            if n in hash_map:
                return hash_map[n]
            else:
                a=nums[n]+recursive(n+2)
                b=recursive(n+1)
                hash_map[n]=max(a,b)
            return hash_map[n]
        return recursive(0)

            
        