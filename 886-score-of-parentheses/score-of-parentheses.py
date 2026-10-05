class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        left=0
        sums=0
        for i in range(len(s)):
            if s[i]=='(':
                left=left+1
            else:
                left=left-1
                if s[i-1]=='(':
                    sums=sums+(2**left)  
        return sums

        