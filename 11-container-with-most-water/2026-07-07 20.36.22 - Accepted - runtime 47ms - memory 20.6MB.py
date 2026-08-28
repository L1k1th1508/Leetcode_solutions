class Solution(object):
    def maxArea(self, height):

        """
        :type height: List[int]
        :rtype: int
        """
    
        area=0
        left=0
        right=len(height)-1
        while left<right:
            result=0
            if height[left]<=height[right]:
                result=height[left]*(right-left)
                left=left+1
            else:
                result=height[right]*(right-left)
                right=right-1
            if result>area:
                area=result
        return area



        