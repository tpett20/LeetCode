// 94. Binary Tree Inorder Traversal
// Given the root of a binary tree, return the inorder traversal of its nodes' values.

var inorderTraversal = function(node) {
    if (!node) return []
    const output = []
    if (node.left) output.push(...inorderTraversal(node.left))
    output.push(node.val)
    if (node.right) output.push(...inorderTraversal(node.right))
    return output
};

class TreeNode {
    constructor(val, left, right) {
        this.val = (val === undefined ? 0 : val)
        this.left = (left === undefined ? null : left)
        this.right = (right === undefined ? null : right)
    }
}

const testCase1 = new TreeNode(1)
testCase1.right = new TreeNode(2)
testCase1.right.left = new TreeNode(3)
console.log(inorderTraversal(testCase1))

const testCase2 = new TreeNode(1)
testCase2.left = new TreeNode(2)
testCase2.right = new TreeNode(3)
console.log(inorderTraversal(testCase2))