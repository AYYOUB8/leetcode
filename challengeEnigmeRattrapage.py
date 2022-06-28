#!/usr/bin/env python
# coding: utf-8

# # EXERCICE 1 
# 

# In[ ]:


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return ans
        


# # EXERCICE 2

# In[ ]:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.val == root.left.val + root.right.val
        


# # EXERCICE 3

# In[ ]:


class Solution:
    def minimumSum(self, num: int) -> int:
        temp = str(num)
        sep = list(temp)
        for i in range(len(sep)):
            sep[i] = int(sep[i])
        sep.sort()
        return sep[0]*10 + sep[3] + sep[1]*10+sep[2]
        
        

