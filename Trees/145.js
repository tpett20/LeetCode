// 145. Binary Tree Postorder Traversal
// Given the root of a binary tree, return the postorder traversal of its nodes' values.

var postorderTraversal = function(root) {
    const traveled = []
    if (root) {
        traveled.push(...postorderTraversal(root.left))
        traveled.push(...postorderTraversal(root.right))
        traveled.push(root.val)
    }
    return traveled
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

console.log(postorderTraversal(testCase))