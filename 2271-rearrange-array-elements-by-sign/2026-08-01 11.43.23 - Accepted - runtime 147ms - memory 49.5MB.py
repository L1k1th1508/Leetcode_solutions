class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[]
        b=[]
        for num in nums:
            if num>0:
                a.append(num)
            else:
                b.append(num)
        i=0
        j=0
        get=[]
        while i <len(a) and j <len(b):
            for k in range(len(nums)):
                if k%2==0:
                    get.append(a[i])
                    i=i+1
                else:
                    get.append(b[j])
                    j=j+1
        return get

            
        