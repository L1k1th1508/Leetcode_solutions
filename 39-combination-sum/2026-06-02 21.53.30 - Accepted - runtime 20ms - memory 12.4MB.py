class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result=[]
        def recursive(start,current,remaining):
            if remaining==0:
                result.append(list(current))
                return
            if remaining <0:
                return
            for i in range (start,len(candidates)):
                current.append(candidates[i])
                recursive(i,current,remaining-candidates[i])
                current.pop()

        recursive(0,[],target)
        return result


        