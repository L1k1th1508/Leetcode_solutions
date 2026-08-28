class Solution(object):
    def smallestNumber(self, n, t):

        """
        :type n: int
        :type t: int
        :rtype: int
        """
        
        def recursive(n):

            mul=1
            while n>0:

                mul=mul*(n%10)
                n=n//10
                if mul==0:
                    break
            return mul%t==0
        while not recursive(n):
            n=n+1
        return n
        
            
        
        