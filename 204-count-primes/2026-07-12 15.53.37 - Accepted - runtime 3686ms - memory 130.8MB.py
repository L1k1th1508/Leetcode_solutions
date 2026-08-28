class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return 0
        end=[]
        result=[True]*(n)
        result[0]=False
        result[1]=False
        for i in range(2,int(n**0.5)+1):
            if result[i]==False:
                continue
            for j in range(2*i,n,i):
                result[j]=False
        k=2
        
        
        while(k<n):
            if result[k]==True:
                end.append(k)
                k=k+1
            else:
                k=k+1
        return len(end)



        