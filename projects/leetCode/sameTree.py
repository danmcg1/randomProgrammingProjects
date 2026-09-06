# Given the roots of two binary trees p and q, 
# write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical,
# and the nodes have the same value.

# Example 1:
# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Example 2:
# Input: p = [1,2], q = [1,null,2]
# Output: false

# Example 3:
# Input: p = [1,2,1], q = [1,1,2]
# Output: false

p = [1,2,1]
q = [1,1,2]

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
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

       # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

answer = Solution()

p_tree = buildTree(p)
q_tree = buildTree(q)

print(p_tree)
print(q_tree)

print(answer.isSameTree(p_tree,q_tree))