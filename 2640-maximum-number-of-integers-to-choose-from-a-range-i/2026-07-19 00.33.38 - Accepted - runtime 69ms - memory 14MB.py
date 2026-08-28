class Solution(object):
    def maxCount(self, banned, n, maxSum):
        """
        :type banned: List[int]
        :type n: int
        :type maxSum: int
        :rtype: int
        """
        banned_s=set(banned)
        count=0
        sums=0
        for i in range(1,n+1):
            if i not in banned_s:
                sums=sums+i
                if sums<=maxSum:
                    count=count+1
            else:
                continue
        return count
    


    



        