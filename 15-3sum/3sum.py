class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        arr=[]
        n=len(nums)
        nums.sort()

        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=n-1
            while j < k:
                sums=nums[i]+nums[j]+nums[k]
                if sums==0:
                    arr.append([nums[i],nums[j],nums[k]])
                    while j<k and nums[j]==nums[j+1]:
                        j=j+1
                    while j<k and nums[k]==nums[k-1]:
                        k=k-1
                    j=j+1
                    k=k-1
                else:
                    if sums>0:
                        k=k-1
                    else:
                        j=j+1
        return arr

                


        