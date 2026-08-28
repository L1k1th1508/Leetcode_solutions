class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums)==1:
            return sum(nums)
        if len(nums)==k:
            return max(nums)
        def finder(mid):
            count=1
            items=0
            for num in nums:
                items=items+num
                if items<=mid:
                    continue
                else:
                    count=count+1
                    items=num
            if count<=k:
                return True
            else:
                return False
        i=max(nums)
        j=sum(nums)
        while i<=j:
            mid=(i+j)//2
            if finder(mid):
                j=mid-1
            else:
                i=mid+1
        return i
        
        
        