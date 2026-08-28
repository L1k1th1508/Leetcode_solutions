class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)==1:
            return True
        def score(i,j):
            if i >j :
                return 0
            if i==j:
                return nums[i]
            val_i=nums[i]+min(score(i+2,j),score(i+1,j-1))
            val_j=nums[j]+min(score(i+1,j-1),score(i,j-2))

            return max(val_i,val_j)
        a=score(0,len(nums)-1)
        return a>=sum(nums)-a
        