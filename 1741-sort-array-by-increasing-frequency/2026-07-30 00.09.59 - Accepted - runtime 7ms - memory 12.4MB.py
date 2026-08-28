class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count=Counter(nums)
        def count_sort(num):
            return (count[num],-num)
        nums.sort(key=count_sort)
        return nums
        