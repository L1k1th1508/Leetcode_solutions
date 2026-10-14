class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        hash_map={}
        left=0
        cur_len=0
        wind_len=cur_len
        for right in range(len(fruits)):
            if fruits[right] not in hash_map:
                hash_map[fruits[right]]=1
            elif fruits[right] in hash_map:
                hash_map[fruits[right]]=hash_map[fruits[right]]+1
            
            
            while len(hash_map)>2:
                hash_map[fruits[left]]=hash_map[fruits[left]]-1
                if hash_map[fruits[left]]==0:
                    hash_map.pop(fruits[left])
                
                left=left+1
            cur_len=right-left+1
            wind_len=max(cur_len,wind_len)
                
        return wind_len



        
        