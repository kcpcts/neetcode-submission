# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # at current node
        # if p or q is on the left and p or q is on the right:
        # this node is the LCA

        # if p or q is on the left but not right: return it
        # if p or q is on the right but not left: return it

        # if neither p or q are on the left or right: return None
        def dfs(node):
            if not node:
                return None
            if node == p: return p
            if node == q: return q

            # check subtree at current
            left = dfs(node.left)
            right = dfs(node.right)

            if left and right: # p or q is on the left AND right
                return node # this is the LCA

            
            if left: return left # only runs if right is None
            if right: return right # only runs if left is None
        
        ans = dfs(root)
        return ans






