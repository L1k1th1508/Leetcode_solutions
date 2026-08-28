class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        a=s.split()
        result=[""]*len(a)
        for i in a:
            ind= int(i[-1])-1
            result[ind]=i[:-1]
        return " ".join(result)   
        