class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a=s.split()
        i=0
        j=len(a)-1
        while i < j:
            a[i],a[j]=a[j],a[i]
            i=i+1
            j=j-1
        return join(a)

        
        

        