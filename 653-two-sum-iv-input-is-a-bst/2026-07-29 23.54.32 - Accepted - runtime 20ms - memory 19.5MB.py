# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):

        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        def inorder(node,arr):
            if not node:
                return
            inorder(node.left,arr)
            arr.append(node.val)
            inorder(node.right,arr)
        nums=[]
        inorder(root,nums)
        i=0
        j=len(nums)-1
        while i < j:
            m=nums[i]+nums[j]
            if m==k:
                return True
            elif m>k:
                j=j-1
            else:
                i=i+1
        return False

    
        



            



        