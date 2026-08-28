class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        all=[]
        for i in range(1,5000):
            all.append(i)
        print(len(all))
        def reduction(arr,all):
            for num in arr:
                i=0
                j=len(all)
                while i<=j:
                    mid=(i+j)//2
                    if num==all[mid]:
                        all.pop(mid)
                        break
                    elif num<all[mid]:

                        j=mid-1
                    else:
                        i=mid+1
            return all
        a=reduction(arr,all)
        print(all)

        return all[k-1]
                



        