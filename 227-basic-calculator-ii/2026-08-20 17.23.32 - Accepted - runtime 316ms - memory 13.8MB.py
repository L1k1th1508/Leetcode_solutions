class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def order(char):
            if char=='/'or char=='*':
                return 1
            elif char=='+' or char=='-':
                return 0
        def operation(char,b,a):
            if char=='+':
                return a+b
            elif char=='-':
                return a-b
            elif char == '*':
                return a*b
            elif char=='/':
                return a//b
        def score(s):
            val=[]
            op=[]
            nu=""
            for i in s:
                if i ==" ":
                    continue
                if i.isdigit():
                    nu=nu+i
                else:
                    val.append(int(nu))
                    nu=""
                    while len(op)!=0 and order(op[-1])>=order(i):
                        operator=op.pop()
                        val_A=val.pop()
                        val_B=val.pop()
                        a=operation(operator,val_A,val_B)
                        val.append(a)
                    
                    op.append(i)
                
                    
            val.append(int(nu))
            
            while len(op)!=0:
                operator=op.pop()
                val_A=val.pop()
                val_B=val.pop()
                a=operation(operator,val_A,val_B)
                val.append(a)
                

            return val[-1]
        
        return score(s)
        

                

                