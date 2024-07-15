# 2196. Create Binary Tree From Descriptions
# You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,
    # If isLefti == 1, then childi is the left child of parenti.
    # If isLefti == 0, then childi is the right child of parenti.
# Construct the binary tree described by descriptions and return its root.
# The test cases will be generated such that the binary tree is valid.

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        children = set()
        tree_data = {}
        for description in descriptions:
            parent, child, is_left = description
            direction = "l" if is_left else "r"
            if parent in tree_data:
                tree_data[parent][direction] = child
            else:
                tree_data[parent] = {direction: child}
            children.add(child)
        
        def build_nodes(val):
            node = TreeNode(val)
            if val not in tree_data:
                return node
            if "l" in tree_data[val]:
                node.left = build_nodes(tree_data[val]["l"])
            else:
                node.left = None
            if "r" in tree_data[val]:
                node.right = build_nodes(tree_data[val]["r"])
            else:
                node.right = None
            return node
        
        root_val = None
        for parent_val in tree_data:
            if parent_val not in children:
                root_val = parent_val
                break
        return build_nodes(root_val)