class Solution(object):
    def minimalKSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        """
        sums=0

        dicti=list(set(nums))
        dicti.sort()
        for num in dicti:
            if num<=k:
                k=k+1
                sums=sums+num
            else:
                break
        return k*(k+1)//2-sums

        