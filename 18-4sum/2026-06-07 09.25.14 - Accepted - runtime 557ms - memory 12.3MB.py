class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result=[]
        nums.sort()
        for i in range(len(nums)-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                
                
                k=j+1
                l=len(nums)-1
                while(k<l):
                    sum=nums[i]+nums[j]+nums[k]+nums[l]
                    if sum==target:
                        result.append([nums[i],nums[j],nums[k],nums[l]])
                    
                        while(k<l and nums[k]==nums[k+1]):
                            k=k+1
                    
                    
                        while(k<l and nums[l]==nums[l-1]):
                            l=l-1
                        k=k+1
                        l=l-1
                    
                    elif sum<target:
                        k=k+1
                    else:
                        l=l-1
        return result
                
                

            

