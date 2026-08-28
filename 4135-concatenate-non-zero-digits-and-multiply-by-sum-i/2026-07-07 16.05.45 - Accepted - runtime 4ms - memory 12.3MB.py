class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        result=[]
        sums=0
        if n==0:
            return 0
        ans=0
        while n>0:

        
            
            ans=n%10
            n=n/10
            if ans==0:
                continue
            else:
                result.append(ans)
        sums=sum(result)
        result.reverse()
        ans="".join(map(str,result))  
        l=int(ans)
        return l*sums
         
            
                
    
        
        

            




        

        