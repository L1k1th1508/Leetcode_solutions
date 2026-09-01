class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        count=0
        ans=[]
        for char in s:
            print(char)
            if char=='(':
                if count>0:
                    ans.append(char)
                
                count=count+1

            else:
                count=count-1
                if count>0:
                    ans.append(char)
                
        a="".join(ans)
        return a 

              
            

        
                

        
        

        