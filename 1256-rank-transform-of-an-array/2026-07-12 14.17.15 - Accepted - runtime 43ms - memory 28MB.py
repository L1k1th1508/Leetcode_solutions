class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        new=sorted(set(arr))
        result=[]
        map={}
        for count,item in enumerate(new,start=1):
            map[item]=count
        for item in arr:
            result.append(map[item])
        return result

        


        