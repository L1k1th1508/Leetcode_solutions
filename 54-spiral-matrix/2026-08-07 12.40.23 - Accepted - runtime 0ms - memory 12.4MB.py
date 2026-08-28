class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        arr=[]
        m=len(matrix)
        n=len(matrix[0])
        top=0
        bottom=m-1
        right=0
        left=n-1
        
                
        
        def first_row(top,right,left):
            for i in range(right,left+1):
            
                arr.append(matrix[top][i])
            return top+1        
        def last_column(top,bottom,left):
            for i in range(top,bottom+1):
                
                arr.append(matrix[i][left])
            return left-1

                    
        def last_row(left,right,bottom):
            for i in range(left,right-1,-1):
                arr.append(matrix[bottom][i])
            return bottom-1
                
                    
        def first_column(bottom,top,right):
            for i in range(bottom,top-1,-1):
                arr.append(matrix[i][right])
                    
            return right+1
        
        while top<=bottom and right<=left:
            top=first_row(top,right,left)
            if top<=bottom and right<=left:
                left=last_column(top,bottom,left)
            if top<=bottom and right<=left:
                bottom=last_row(left,right,bottom)
            if top<=bottom and right<=left:
                right=first_column(bottom,top,right)
             
        
        return arr

        