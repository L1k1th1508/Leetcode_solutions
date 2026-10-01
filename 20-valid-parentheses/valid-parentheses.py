class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        parenthesis={")":"(","}":"{","]":"["}
        for i in s:
            if i in parenthesis:
                if  stack and stack[-1]==parenthesis[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False



         
        