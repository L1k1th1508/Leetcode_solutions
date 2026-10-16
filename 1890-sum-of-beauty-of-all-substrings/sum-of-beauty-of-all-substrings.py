class Solution(object):
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """
        beauty=0
        n=len(s)
        in_beauty=0
        for i in range(n-1):
            hash_map={}
            for j in range(i,n):
                if s[j] not in hash_map:
                    hash_map[s[j]]=1
                elif s[j]  in hash_map:
                    hash_map[s[j]]=hash_map[s[j]]+1
                mini_frequency=min(hash_map.values())
                max_frequency=max(hash_map.values())
                in_beauty=max_frequency- mini_frequency
                beauty=beauty+in_beauty
        return beauty
