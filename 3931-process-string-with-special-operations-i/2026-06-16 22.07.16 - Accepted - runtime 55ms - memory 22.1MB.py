class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        result =[]
        for i in s:
            if i=='*':
                if result:
                    result.pop()
            elif i=="#":
                result.extend(result)
            elif i=="%":
                result.reverse()
            else:
                result.append(i)
        return "".join(result)
        
            

            
