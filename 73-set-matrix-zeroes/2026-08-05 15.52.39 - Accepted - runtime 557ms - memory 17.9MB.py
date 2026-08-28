class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        def setr(m):
            for i in range(len(matrix[m])):
                matrix[m][i] = 0

        def setc(n):
            for i in range(len(matrix)):
                matrix[i][n] = 0
        m = len(matrix)
        n = len(matrix[0])
        o=set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    o.add((i,j))
        for i in o:
            setr(i[0])
            setc(i[1])
        
        







        