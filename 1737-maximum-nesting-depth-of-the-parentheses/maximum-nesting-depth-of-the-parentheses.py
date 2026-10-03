class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        sums=0
        left=0
        for i in s:
            if i=='(':
                left=left+1
            elif i==')':
                left=left-1
            sums=max(sums,left)
        return sums
        