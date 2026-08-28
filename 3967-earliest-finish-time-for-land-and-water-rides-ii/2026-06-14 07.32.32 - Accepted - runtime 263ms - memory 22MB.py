class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        def solve(a,b,c,d):
            result =1000000
            for i in range(len(a)):
                result=min(result,a[i]+b[i])
            result1=1000000
            for j in range(len(c)):
                result1=min(result1,max(result,c[j])+d[j])
            return result1
        l_w=solve(landStartTime, landDuration, waterStartTime, waterDuration)
        w_l=solve(waterStartTime, waterDuration, landStartTime, landDuration)
        return min(l_w,w_l)

        