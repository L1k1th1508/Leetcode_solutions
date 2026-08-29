class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        arr=[]
        nums.sort()
        n=len(nums)
        for i in range(n-1):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                
                k=j+1
                l=n-1
                while k < l:
                    
                    sums=nums[i]+nums[j]+nums[k]+nums[l]
                    if sums==target:
                        arr.append([nums[i],nums[j],nums[k],nums[l]])
                        while k<l and nums[k]==nums[k+1]:
                            k=k+1
                        while k<l and nums[l]==nums[l-1]:
                            l=l-1
                        k=k+1
                        l=l-1
                    else:
                        if sums>target:
                            l=l-1
                        else:
                            k=k+1
        return arr
                


                

        