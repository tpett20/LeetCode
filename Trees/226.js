// 226. Invert Binary Tree
// Given the root of a binary tree, invert the tree, and return its root.

var invertTree = function(node) {
    if (!node) return node
    if (node.left || node.right) {
        const temp = node.left
        node.left = node.right
        node.right = temp
        if (node.left) invertTree(node.left)
        if (node.right) invertTree(node.right)
    } 
    return node
};

class TreeNode {
    constructor(val, left, right) {
        this.val = (val === undefined ? 0 : val)
        this.left = (left === undefined ? null : left)
        this.right = (right === undefined ? null : right)
    }
}

const testCase1 = new TreeNode(4)
testCase1.left = new TreeNode(2)
testCase1.right = new TreeNode(7)
testCase1.left.left = new TreeNode(1)
testCase1.left.right = new TreeNode(3)
testCase1.right.left = new TreeNode(6)
testCase1.right.right = new TreeNode(9)
console.log('Test Case 1:', invertTree(testCase1))

const testCase2 = new TreeNode(2)
testCase2.left = new TreeNode(1)
testCase2.right = new TreeNode(3)
console.log('Test Case 2:', invertTree(testCase2))