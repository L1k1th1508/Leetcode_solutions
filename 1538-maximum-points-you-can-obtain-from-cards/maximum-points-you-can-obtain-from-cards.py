class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        total=sum(cardPoints)
        window_size=len(cardPoints)-k
        left=0
        right=window_size
        new_sum=sum(cardPoints[left:right])
        min_window_sum=new_sum
        for i in range(right,len(cardPoints)):
            new_sum=new_sum+cardPoints[i]-cardPoints[i-right]
            min_window_sum=min(new_sum,min_window_sum)
        max_sum=total-min_window_sum
        return max_sum
       
            
            


        
        