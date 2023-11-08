// 104. Maximum Depth of Binary Tree
// Given the root of a binary tree, return its maximum depth.
// A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

var maxDepth = function(root) {
    if (!root) return 0
    if (!root.left && !root.right) return 1
    function traverse(node) {
        let leftDepth = node.left ? traverse(node.left) : 0
        let rightDepth = node.right ? traverse(node.right) : 0
        return 1 + Math.max(leftDepth, rightDepth)
    }
    return traverse(root)
};

class TreeNode {
    constructor(val, left, right) {
        this.val = (val === undefined ? 0 : val)
        this.left = (left === undefined ? null : left)
        this.right = (right === undefined ? null : right)
    }

    // BST Insert Method
    insert(val) {
        const newNode = new TreeNode(val)
        let walker = this
        while (true) {
            if (val < walker.val) {
                if (!walker.left) {
                    walker.left = newNode
                    return this
                }
                walker = walker.left
            } else if (val > walker.val) {
                if (!walker.right) {
                    walker.right = newNode
                    return this
                }
                walker = walker.right
            } else return this
        }
    }
}

const testCase1 = new TreeNode(5)
testCase1.insert(2)
testCase1.insert(7)
testCase1.insert(1)
testCase1.insert(3)
testCase1.insert(4)
console.log(maxDepth(testCase1))

const testCase2 = new TreeNode(1)
testCase2.insert(2)
console.log(maxDepth(testCase2))