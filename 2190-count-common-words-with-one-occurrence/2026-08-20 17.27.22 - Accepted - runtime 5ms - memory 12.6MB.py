class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        dic={}
        t=[]
        s=0
        for i in words1:
            dic[i]=dic.get(i,0)+1
        
        for j in dic:
            if dic[j]==1:
                t.append(j)
        
        for k in words2:
            dic[k]=dic.get(k,0)+1
        
        for m in t:
            if dic[m]==2:
                s=s+1
        return s
        
        