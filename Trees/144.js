// 144. Binary Tree Preorder Traversal
// Given the root of a binary tree, return the preorder traversal of its nodes' values.

var preorderTraversal = function(node) {
    if (!node) return []
    const visited = [node.val]
    visited.push(...preorderTraversal(node.left))
    visited.push(...preorderTraversal(node.right))
    return visited
};

class TreeNode {
    constructor(val, left, right) {
        this.val = (val === undefined ? 0 : val)
        this.left = (left === undefined ? null : left)
        this.right = (right === undefined ? null : right)
    }
}

const testCase = new TreeNode(1)
testCase.left = new TreeNode(2)
testCase.right = new TreeNode(3)
testCase.left.left = new TreeNode(4)
testCase.left.right = new TreeNode(5)

console.log(preorderTraversal(testCase))