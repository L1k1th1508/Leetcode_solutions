class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        sums=0
        left=0
        
        for i in range(len(s)):
            if s[i]=='(':
                sums=sums+1
            elif sums >0 and s[i]==')':
                sums=sums-1
            else:
                left=left+1
        return sums+left

                     
            


        