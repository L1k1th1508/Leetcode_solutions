class Solution(object):
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        """
        :type nums: List[int]
        :type firstLen: int
        :type secondLen: int
        :rtype: int
        """
        def result(x,y):
            sum1=sum(nums[0:x])
            sum2=sum(nums[x:x+y])

            max_sum1=sum1
            max_total=max_sum1+sum2

            left=0
            right=x
            for i in range(x+y,len(nums)):
                sum2+=nums[i]-nums[right]
                right=right+1

                sum1+=nums[right-1]-nums[left]
                left=left+1

                max_sum1=max(max_sum1,sum1)
                max_total=max(max_total,max_sum1+sum2)
            return max_total
        return max(result(firstLen,secondLen),result(secondLen,firstLen))



        