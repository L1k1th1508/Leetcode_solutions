class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        maps={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sums=0
        
        for i in range(len(s)):
            
                if i+1<len(s) and maps[s[i]]<maps[s[i+1]]:
                    sums=sums-maps[s[i]]
                else:
                    sums=sums+maps[s[i]]


                

        return sums
