class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_in=1
        max_count=1
        count_out=1
        max_count_out=1
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                count_in=count_in+1
                if count_in>max_count:
                    max_count=count_in
            else:
                count_in=1
        for j in range(len(nums)-1):
            if nums[j]>nums[j+1]:
                count_out=count_out+1
                if count_out>max_count_out:
                    max_count_out=count_out
            else:
                count_out=1
        return max(max_count,max_count_out)


            

            


        