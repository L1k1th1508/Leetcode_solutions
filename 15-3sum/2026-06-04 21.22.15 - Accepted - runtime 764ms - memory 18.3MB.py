class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        nums.sort()
        for i in range(0,len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            while j<k:
                sum=nums[i]+nums[j]+nums[k]
                if sum==0:
                    result.append([nums[i],nums[j],nums[k]])
                
                    while j<k and nums[j]==nums[j+1]:
                        j=j+1
                    while j<k and nums[k]==nums[k-1]:
                        k=k-1
                    j=j+1
                    k=k-1
                elif sum<0:
                    j=j+1
                else:
                    k=k-1

        return result
                
            
                