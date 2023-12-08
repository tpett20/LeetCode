// 606. Construct String from Binary Tree
// Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way, and return it.
// Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.

var tree2str = function(node) {
    let output = node.val.toString()
    if (node.left) output += "(" + tree2str(node.left) + ")"
    else if (node.right) output += "()"
    if (node.right) output += "(" + tree2str(node.right) + ")"
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
testCase1.left = new TreeNode(2)
testCase1.right = new TreeNode(3)
testCase1.left.left = new TreeNode(4)
console.log(tree2str(testCase1))

const testCase2 = new TreeNode(1)
testCase2.left = new TreeNode(2)
testCase2.right = new TreeNode(3)
testCase2.left.right = new TreeNode(4)
console.log(tree2str(testCase2))