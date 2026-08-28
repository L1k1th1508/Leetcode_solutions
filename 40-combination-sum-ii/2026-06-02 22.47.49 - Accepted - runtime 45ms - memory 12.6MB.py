class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()
        def recursive(start,current,remaining):
            if remaining ==0:
                result.append(list(current))
                return
            if remaining <0:
                return
            for i in range(start, len(candidates)):
                if i >start and candidates[i]==candidates[i-1]:
                    continue
                current.append(candidates[i])
                recursive(i+1,current,remaining-candidates[i])
                current.pop()
        recursive(0,[],target)
        return result
