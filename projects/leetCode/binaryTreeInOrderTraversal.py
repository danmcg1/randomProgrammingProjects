# Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

# Example 1:
# Input: root = [1,null,2,3]
# Output: [1,3,2]

# Example 2:
# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
# Output: [4,2,6,5,7,1,3,9,8]

# Example 3:
# Input: root = []
# Output: []

# Example 4:
# Input: root = [1]
# Output: [1]

# Constraints:

#     The number of nodes in the tree is in the range [0, 100].
#     -100 <= Node.val <= 100


root = [1,2,3,4,5,None,8,None,None,6,7,9]


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(root):
    if not root:
        return None
    
    nodes = [TreeNode(val) if val is not None else None for val in root]

    for i in range(len(nodes)):
        if nodes[i] is not None:
            left_idx = 2 * i + 1
            right_idx = 2 * i + 2

            if left_idx < len(nodes):
                nodes[i].left = nodes[left_idx]
            if right_idx < len(nodes):
                nodes[i].right = nodes[right_idx]

    return nodes[0]



class Solution(object):
    def inorderTraversal(self, root):
        res = []  
        
        def inOrder(node):
            if node is None:
                return

            inOrder(node.left)     
            res.append(node.val)   
            inOrder(node.right)    

        inOrder(root)  
        return res

answer = Solution()

tree = buildTree(root)
print(answer.inorderTraversal(tree))

