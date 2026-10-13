class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapi={}
        left=0
        cur_length=0
        wind_length=cur_length
        
        for right in range(len(s)):

            if s[right] not in mapi:
                mapi[s[right]]=right
                cur_length=right-left+1
                wind_length=max(cur_length,wind_length)
            elif s[right] in mapi:
                if mapi[s[right]]>=left:
                    left=mapi[s[right]]+1
                mapi[s[right]]=right
                cur_length=right-left+1
                wind_length=max(wind_length,cur_length)
        return wind_length


        
            
                
        

        


            

        