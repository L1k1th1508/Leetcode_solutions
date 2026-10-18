class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        hash_map_1={}
        result=""
        left=0
        count=0
        min_length=float("inf")
        start=0
        for i in t:
            if i not in hash_map_1:
                hash_map_1[i]=1
            elif i in hash_map_1:
                hash_map_1[i]=hash_map_1[i]+1
        char_c=len(hash_map_1)
        inside_freq={}

        for right in range(len(s)):
            if s[right] in hash_map_1:
                inside_freq[s[right]]=inside_freq.get(s[right],0)+1
                
                if inside_freq[s[right]]==hash_map_1[s[right]]:

                    count=count+1
            
            
            while count==char_c:
                length_c=right-left+1
                if length_c<min_length:
                    min_length=length_c
                    start=left
                
                if s[left] in hash_map_1:
                    inside_freq[s[left]]=inside_freq[s[left]]-1
                    if inside_freq[s[left]]<hash_map_1[s[left]]:
                        count=count-1
                left=left+1
        if min_length==float("inf"):
            return ""



        return s[start:start+min_length]
                

        
                


        