class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        arr=[]
        def shorten(n):
            while n>0:
                a=n%10
                arr.append(a)
                n=n//10
            return arr
                
          
        def product(arr):
            i=1
            for num in arr:
                i=i*num
            return i
        
        def sums(arr):
            j=0
            for num in arr:
                j=j+num
            return j
        
        
        a=shorten(n)
        ab=sums(a)
        abc=product(a)
        ac=ab+abc
        if ac==0:
            return False
        if n%ac==0:
            return True
        else:
            return False

        