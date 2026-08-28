class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr=[]
        prod=1
        while n>0:
            digit=n%10
            arr.append(digit)
            n=n/10
        arr.sort()
        for i in range(len(arr)):
            if i==len(arr)-1:
                prod=arr[i]*arr[i-1]
        return prod
        