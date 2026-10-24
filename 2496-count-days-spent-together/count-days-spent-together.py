class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        def conversion(s):
            dates=[31,28,31,30,31,30,31,31,30,31,30,31]
            result=s.split('-')
            month=int(result[0])
            day=int(result[1])
            half=sum(dates[0:month-1])
            r=half+day
            return r
        alicefirst=conversion(arriveAlice)
        aliceend=conversion(leaveAlice)
        bobfirst=conversion(arriveBob)
        bobend=conversion(leaveBob)
        maxdate=max(alicefirst,bobfirst)
        mindate=min(aliceend,bobend)
        if mindate<maxdate:
            return 0
        else:
            return mindate-maxdate+1




        