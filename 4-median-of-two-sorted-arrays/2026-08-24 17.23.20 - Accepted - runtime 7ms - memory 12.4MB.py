class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def merge(nums1,nums2):
            k=0
            i=0
            j=0
            arr=[0]*(len(nums1)+len(nums2))
            while i<len(nums1) and j <len(nums2):
                if nums1[i]<=nums2[j]:
                    arr[k]=nums1[i]
                    i=i+1
                    
                else:
                    arr[k]=nums2[j]
                    j=j+1
                k=k+1
                
            
            while i <len(nums1):
                    
                arr[k]=nums1[i]
                i=i+1
                k=k+1
            

            while j <len(nums2):
                
                arr[k]=nums2[j]
                j=j+1
                k=k+1
            return arr
        nums=merge(nums1,nums2)
        n=len(nums)
        mid=n//2
        if n%2==0:
            return (nums[mid-1]+nums[mid])/2.0
        else:
            return float(nums[mid])


            

        
        