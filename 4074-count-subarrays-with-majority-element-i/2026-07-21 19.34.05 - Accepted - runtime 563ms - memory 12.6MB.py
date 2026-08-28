class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        count=0
        sums=0
        dic={0:1}
        for num in nums:
            if num==target:
                sums+=1
            else:
                sums-=1
            for subs,freq in dic.items():
                if subs<sums:
                    count+=freq
            dic[sums]=dic.get(sums,0)+1
        return count


        