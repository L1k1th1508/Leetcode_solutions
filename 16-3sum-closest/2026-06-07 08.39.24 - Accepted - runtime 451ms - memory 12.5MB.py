class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
    
        nums.sort()
        a=nums[0]+nums[1]+nums[2]
        
        

        for i in range(len(nums)-2):
            j=i+1
            k=len(nums)-1
            
            while(j<k):

            
                sum=nums[i]+nums[j]+nums[k]
                if abs(sum-target)<abs(a-target):
                    a=sum
                if sum<target:
                    j=j+1
                elif sum>target:
                    k=k-1
                else:
                    return sum
        

                  
                
                    
                
                
        return a

        