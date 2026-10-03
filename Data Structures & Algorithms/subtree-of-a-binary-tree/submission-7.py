# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if left or right is subtree, then this is a subtree.
        # if the current value = subtree root value, then:
        # check left subtree with subtree.left
        # check right subtree with subtree.right
        
        def sameTree(root1,root2):
            if not root1 and not root2:
                return True
            if (root1 and not root2) or (root2 and not root1):
                return False
            
            if root1.val == root2.val and sameTree(root1.left,root2.left) and sameTree(root1.right,root2.right):
                return True

            return False
        
        if sameTree(root,subRoot):
            return True
        else:
            if root:
                return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        return False
        
        