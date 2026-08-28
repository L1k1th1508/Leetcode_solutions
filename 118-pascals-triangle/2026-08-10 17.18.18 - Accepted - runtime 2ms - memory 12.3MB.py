import math
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        arr=[]
        for i in range(numRows):
            key=[]
            for j in range(i+1):
                combination=math.factorial(i)//(math.factorial(j)*math.factorial(i-j))
                key.append(combination)
            arr.append(key)
        return arr


        
            
        
                    

        