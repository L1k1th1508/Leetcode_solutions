class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum1=n*n
        sum2=n*(n+1)
        def recursive(k,m):
            if m==0:
                return k
            else:
                return recursive(m,k%m)
        return recursive(sum1,sum2)
        