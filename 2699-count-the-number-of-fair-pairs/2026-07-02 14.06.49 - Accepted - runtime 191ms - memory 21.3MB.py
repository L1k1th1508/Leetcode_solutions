class Solution(object):
    def countFairPairs(self, nums, lower, upper):


        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        nums.sort()
        def counts(el):

            count=0
            i=0
            j=len(nums)-1
            while i< j:
                if nums[i]+nums[j]<=el:
                    count+=j-i
                    i=i+1
                else:
                    j=j-1
            return count
        
        return counts(upper)-counts(lower-1)


        




        