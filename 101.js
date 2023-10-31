// 101. Symmetric Tree
// Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

var isSymmetric = function(root) {
    if (!root.left && !root.right) return true
    if (!root.left || !root.right) return false

    function DFSLeft(node) {
        const values = []
        function traverse(node) {
            values.push(node.val)
            if (node.left) traverse(node.left)
            else values.push(null)
            if (node.right) traverse(node.right)
            else values.push(null)
        }
        traverse(node)
        return values
    }

    function DFSRight(node) {
        const values = []
        function traverse(node) {
            values.push(node.val)
            if (node.right) traverse(node.right)
            else values.push(null)
            if (node.left) traverse(node.left)
            else values.push(null)
        }
        traverse(node)
        return values
    }

    const leftArr = DFSLeft(root.left)
    const rightArr = DFSRight(root.right)
    if (leftArr.length !== rightArr.length) return false
    for (let i = 0; i < leftArr.length; i++) {
        if (leftArr[i] !== rightArr[i]) return false
    }
    return true
}

class TreeNode {
    constructor(val, left, right) {
        this.val = (val === undefined ? 0 : val)
        this.left = (left === undefined ? null : left)
        this.right = (right === undefined ? null : right)
    }
}

const testCase1 = new TreeNode(1)
testCase1.left = new TreeNode(2)
testCase1.right = new TreeNode(2)
testCase1.left.left = new TreeNode(3)
testCase1.left.right = new TreeNode(4)
testCase1.right.left = new TreeNode(4)
testCase1.right.right = new TreeNode(3)
console.log(isSymmetric(testCase1))

const testCase2 = new TreeNode(1)
testCase2.left = new TreeNode(2)
testCase2.right = new TreeNode(2)
testCase2.left.right = new TreeNode(3)
testCase2.right.right = new TreeNode(3)
console.log(isSymmetric(testCase2))