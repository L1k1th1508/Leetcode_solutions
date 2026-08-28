class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        t=[]
        n=len(s)
        mid=n//2
        string =list(s)
        string[0:mid]=sorted(string[0:mid])

        for i in range(mid):
            string[n-1-i]=string[i]
        s=''.join(string)
        return s
        
        


        