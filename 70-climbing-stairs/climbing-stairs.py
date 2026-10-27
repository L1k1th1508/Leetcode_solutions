class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        hash_map={}
        def recursive(n):
            if n==1:
                return 1
            if n==2:
                return 2
            if n in hash_map:
                return hash_map[n]
            a=recursive(n-1)+recursive(n-2)
            hash_map[n]=a
            return a
        return recursive(n)
            
        
        

        