class Solution(object):
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefixgcd=[]
        hell=[]
        l=0
        r=len(nums)-1
        maxi=0
        sums=0
        def recursive(a,b):
            if b==0:
                return a
            else:
                return recursive(b,a%b)

        for i in range(len(nums)):
            if maxi<nums[i]:
                maxi=nums[i]
        
            
            ant=recursive(nums[i],maxi)
            prefixgcd.append(ant)
        prefixgcd.sort()
        while l<r:
            sums=sums+recursive(prefixgcd[l],prefixgcd[r])
            l=l+1
            r=r-1
        
        return sums




        